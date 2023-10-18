#!/usr/bin/env python3

import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from sqlalchemy import create_engine, text
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.let_it_rain import rain
from streamlit_extras.badges import badge
import asyncio
import pickle
import redis

st.set_page_config(page_title="Dras",
                   page_icon=":sign-intersection-fill:",
                   layout="wide"
                   )
st.markdown('<h1 span style="color: blue;">DIABETES RISK ASSESSMENT.</span>', unsafe_allow_html=True)
st.warning('Early diagnosis, leads to early prevention and treatment therefore healthy life..')
ysno = ['no', 'yes']

def loadModel(model_file, scaler_file):
    """Loads the model and standard scaler"""
    try:
        #Load Diabetes predictor model
        with open(model_file, 'rb') as file_1:
            model = pickle.load(file_1)
        #Load the scaler 
        with open(scaler_file, 'rb') as file_2:
            scaler = pickle.load(file_2)
        return model, scaler
    except FileNotFoundError as fe:
        st.error("File not found returning: {}".format(fe))
        return None
    except Exception as ex:
        st.error("Error occurred returning: {}".format(fe))
        return None
def redisSet(val):
    """Set diabetes prediction outcome value in the redis server"""
    host = "rediss://red-ckluvjg710pc73eb6ckg"
    port = 6379
    # Create a connection to the Redis server
    try:
        r = redis.StrictRedis(host=host, port=port, decode_responses=True)
        #serialized_df = df.to_msgpack(compress='zlib')
        r.set("Diabete state", val)
    except Exception as e:
        st.error(e)
def redisGet():
    """Gets diabetes prediction outcome values from the redis server"""
    host = "redis://red-ckluvjg710pc73eb6ckg"
    port = 6379
    try:
        r = redis.StrictRedis(host=host, port=port, decode_responses=True)
        #serialized_df = df.to_msgpack(compress='zlib')
        return r.get("Diabete state")
    except Exception as e:
        st.error(e)
        return None
def getEngine():
    """returns a postgresql engine connection instance"""
    db_url1 = "postgresql://dras_db_7ke9_user:rjbBj2JXRshov9Kkbvpz8snTKEt6MmDN@dpg-ckn4olv83ejs739li02g-a.oregon-postgres.render.com/dras_db_7ke9"
    engine = create_engine(db_url1)
    return engine

async def persist_data(x_df):
    #Saves user inputs to the postgresql
    try:
        engine = getEngine()
        Session = sessionmaker(bind=engine)
        session = Session()
        x_df.to_sql('dras_table', con=engine, if_exists='append', index=False)
        session.commit()
        session.close()
        return True
    except Exception as e:
        st.error(e)
        return False

def fetch_data():
    """Fetches data from postresql database"""
    data = pd.read_sql("dras_table", con=getEngine())
    return data

def fetch_data1():
    """Fetches data from postresql database"""
    engine = getEngine()
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        sql = text("SELECT * FROM dras_table")
        result = session.execute(sql)
        for row in result:
            st.write(row)

    except Exception as e:
        st.error(f"An error occurred: {e}")
    finally:
        session.close()

def printResult(pred):
    #Prints results of the Dras model prediction.
    if pred == 1:
        st.markdown('<h4 span style="color: orange;">Our model predicts you might be exposed to diabetes risks.\
            Below are potential causes.</span>', unsafe_allow_html=True)
        risks = st.table(cases)
        st.markdown('<h4 span style="color: orange;">You are therefore required to visit nearest facility for further\
            creening...🏃‍♀️🏃‍♂️</span>', unsafe_allow_html=True)
    elif pred == 0:
        rain(
            emoji="🎈",
            font_size=34,
            falling_speed=5.,
            animation_length="infinite"
        )
        st.markdown('<h4 span style="color: green;">Model returns negative prediction for diabetes assessment🏌️‍♂️.</span>', unsafe_allow_html=True)
        st.markdown('<h5 span style="color: green;">However, other contributing factors may have not been captured as contributors to this prediction\
            therefore there is no certainity the result is perfectly accurate..</span>', unsafe_allow_html=True)
async def schedule(x_df):
    #Schedules syncronous tasks in writing, printing and reading data.
    await persist_data(x_df)
    pred = x_df['Prediction'][0]
    printResult(pred)

def sel_box(label, opts):
    select = st.selectbox(label=label, options=opts)
    return select
def userInput():
    cases:list = []
    bp_rs = 0
    bp = sel_box("How would you rate your blood pressure?", ['','low', 'high'])
    if bp == 'high':
        cases.append("High blood pressure")
        bp_rs = 1
    chl_rs = 0
    chl = sel_box("Do you eat food rich in high cholestrol such as red meat in beef, pork, sausages\
            or been told to have high cholestrol?", ysno)
    if chl == 'yes':
        cases.append("High cholestrol")
        chlk_rs = 1
    chlk_rs = 0
    chlk = sel_box("Have you had your cholestrol checked in the last 5 years?", ysno)
    if chlk == 'Yes':
        cases.append("High cholestrol history")
        chlk_rs = 1
    bmi = st.number_input("What is your body mass index (BMI)?", min_value=10, max_value=60, step=2)
    if bmi < 18.5:
        cases.append(f"Underweight, BMI value {bmi} below healthy range 18.5 to 24.9")
    elif bmi > 25.0:
        cases.append(f"Overweight to Obese, BMI value {bmi} above healthy range 18.5 to 24.9")
    smk_rs = 0
    smk = sel_box('Have you smoked at least 100 cigarettes in your entire life?', ysno)
    if smk == 'yes':
        cases.append("Smoking tobacco sigars with nicotine")
        smk_rs = 1
    stk_rs = 0
    stk = sel_box('Have you ever been told you have a stroke?', ysno)
    if stk == 'yes':
        cases.append("Stroke or diagnosis")
        stk = 1
    hda_rs = 0
    hda = sel_box('Do you have coronary heart disease (CHD) or myocardial infarction (MI)?', ysno)
    if hda == 'yes':
        cases.append("Coronary heart disease (CHD) or myocardial infarction (MI)")
        hda_rs = 1
    psa_rs = 0
    psa = sel_box("Do you actively engage in physical exercises in the past 30 days?", ysno)
    if psa == 'yes':
        cases.append("Poor or lack of body physical excersises and activities")
        psa_rs = 1
    fts_rs = 0
    fts = sel_box("Consume Fruit 1 or more times per day?", ysno)
    if fts == "yes":
        fts_rs = 1
    else:
        cases.append("Poor or lack of fruits")
    vgs_rs = 0
    vgs = sel_box("Consume Vegetables 1 or more times per day?", ysno)
    if vgs == "yes":
        vgs_rs = 1
    else:
        cases.append("Poor or lack of veggies")
    alc_rs = 0
    alc = sel_box("Heavy drinker (adult men having more than 14 drinks per week\
            and adult women having more than 7 drinks per week)?", ysno)
    if alc == 'yes':
        cases.append("Heavy drinking of alcohol")
        alc_rs = 1
    hc_rs = 0
    hc = sel_box("Have any kind of health care coverage, including health insurance,\
            prepaid plans such as HMO, etc?", ysno)
    if hc_rs == 'yes':
        cases.append("Lack of health care coverage, including health insurance")
        hc_rs = 1
    ndc_rs = 0
    ndc = sel_box('Was there a time in the past 12 months when you needed to see a doctor\
            but could not because of cost?', ysno)
    if ndc == 'yes':
        cases.append("Poor or lack of good health services")
        ndc_rs = 1
    gh = st.number_input("Would you say that in general your health is: scale 1-5 with\
            1=excellent, 2=very good, 3=good, 4=fair, 5=poor", min_value=1, max_value=5)
    if gh == 5:
        cases.append("Poor general health state")
    mh = st.number_input("About your mental health, which includes stress, depression,\
            and problems with emotions,for how many days during the past 30 days was your\
            mental health not good? scale 1-30 days?", min_value=1, max_value=30)
    if mh > 14:
        cases.append("Poor mental state")
    ph = st.number_input("Now thinking about your physical health, which includes physical\
            illness and injury, for how many days during the past 30 days was your physical\
            health not good? scale 1-30 days", min_value=1, max_value=30)
    if ph > 14:
        cases.append("Poor Physical health state")
    wc_rs = 0
    wc = sel_box("Do you have serious difficulty walking or climbing stairs?", ysno)
    if wc == 'yes':
        cases.append("Crippled or difficulty in walking and/or climbing")
        wc_rs = 1
    sx_rs = 0
    sx = sel_box('What is your gender', ['','female', 'male'])
    if sx == 'male':
        sx_rs = 1
    age_cat = {'18-24':1,'25-29':2, '30-34':3,'35-39':4,'40-44':5,'45-49':6,'50-54':7,'55-59':8,'60-64':9,
            '65-69':10,'70-74':11,'75-80':12,'Over 80':13}
    age = sel_box('Select your age category', age_cat.keys())
    if age_cat[age] > 6:
        cases.append("Older age category")
    age_rs = age_cat[age]
    edu_cat = {'Never attended school':1, 'Grades 1 through 8':2, 'Grades 9 through 11':3,'Grade 12\
            or GED (High school graduate)':4, 'College 1 year to 3 years':5, 'College 4 years or more':6}
    edu = sel_box('What is your highest education level?', edu_cat.keys())
    edu_rs = edu_cat[edu]

    inc_cat = {'less than $10,000':1,'less than $15,000':2, 'less than $20,000':3, 'less than $25,0000':4,
            'less than $25,000':5, 'less than $50,000':6, 'less than $75,000':7, 'More than $75,000':8}
    inc = sel_box('What is your income scale?', inc_cat.keys())
    if inc_cat[inc] < 4:
        cases.append("Low incoming translating to inadequacy in seeking health services")
    inc_rs = inc_cat[inc]

    elements = {'HighBP':bp, 'HighChol':chl, 'CholCheck':chlk, 'Bmi':bmi, 'Smoker':smk, 'Stroke':stk,
                'HeartDiseaseorAttack':hda, 'PhysActivity':psa, 'Fruits':fts, 'Veggies':vgs, 'HvyAlcoholConsump':alc,
                'AnyHealthcare':hc, 'NoDocbcCost':ndc, 'GenHlth':gh, 'MentHlth':mh, 'PhysHlth':ph,
                'DiffWalk':wc, 'Sex':sx, 'Age':age, 'Education':edu, 'Income':inc}
    inputs = {'HighBP':bp_rs,'HighChol':chl_rs,'CholCheck':chlk_rs, 'Bmi':bmi,'Smoker':smk_rs,
                'Stroke':stk_rs, 'HeartDiseaseorAttack':hda_rs, 'PhysActivity':psa_rs, 'Fruits':fts_rs,
                'Veggies':vgs_rs, 'HvyAlcoholConsump':alc_rs, 'AnyHealthcare':hc_rs, 'NoDocbcCost':ndc_rs,
                'GenHlth':gh, 'MentHlth':mh, 'PhysHlth':ph, 'DiffWalk':wc_rs, 'Sex':sx_rs, 'Age':age_rs,
                'Education':edu_rs, 'Income':inc_rs}
    return elements, inputs, cases
if __name__ == "__main__":
    user_inputs = userInput()
    elements = user_inputs[0]
    inputs = user_inputs[1]
    cases = user_inputs[-1]
    #reset = lt.button("Back")
    lt, rt = st.columns(2)

    predict = rt.button("Query risk status")
    if predict:
        blanks = []
        for k,v in elements.items():
            if v == '' or v is None:
                blanks.append(k)
        if blanks:
            st.error(f"The following inputs are blank: {', '.join(blanks)}")
        else:
            x_df = pd.DataFrame(inputs, index=[0])
            modelscaler = loadModel("Model.pkl", "Scaler.pkl")
            if modelscaler:
                model = modelscaler[0]
                scaler = modelscaler[-1]
                x_feat = scaler.transform(x_df)

                pred = model.predict(x_feat)

                x_df['Prediction'] = pred
                x_df['EntryDate'] = datetime.now()
                with st.spinner("Please wait for the execution to finish ..."):
                    asyncio.run(schedule(x_df))
                stats = st.button('Show more')
                if stats:
                    switch_page("pages/Statistics")
                
    hide_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
    st.markdown(hide_style, unsafe_allow_html=True)
