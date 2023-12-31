#!/usr/bin/env python3

import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import streamlit_authenticator as stauth
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt

import pickle
from yaml.loader import SafeLoader
import yaml

def fetching_data_from_dras():
    """Fetches data from postresql database"""
    db_url1 = "postgresql://dras_db_7ke9_user:rjbBj2JXRshov9Kkbvpz8snTKEt6MmDN@dpg-ckn4olv83ejs739li02g-a.oregon-postgres.render.com/dras_db_7ke9"
    engine = create_engine(db_url1)
    data = pd.read_sql("dras_table", con=engine)
    return data
def download_data(dta, file_name):
    data = dta.to_csv().encode('utf-8')
    st.download_button(
        label="Extract this data",
        data=data,
        file_name= f"{file_name}.csv",
        mime='text/csv',)
    
file_path = Path(__file__).parent/"hashed_pwd_pkl"
with file_path.open('rb') as f:
    pwds = pickle.load(f)
file = Path(__file__).parent/"config.yaml"
with open(file) as file:
    config = yaml.load(file, Loader=SafeLoader)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)
name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status == False:
    st.error("Username/ password incorrect")
else:
    if authentication_status == None:
        st.error("Enter username and/or password incorrect")
    else:
        try:
            st.markdown('<h2 span style="color: blue;">Welcome to DRAS Monitor.</span>', unsafe_allow_html=True)
            data = fetching_data_from_dras()
            data['Status']=None
            data.loc[(data.Prediction==0), 'Status']='Control'
            data.loc[(data.Prediction==1), 'Status']='Case'
            counts = data['Status'].value_counts()
            
            st.markdown('<h4 span style="color: green;">Cases and controls from the predictions.</span>', unsafe_allow_html=True)
            st.write(f"Total participants assessed: {len(data.Prediction)}")
            st.write(f"Total cases: {len(data[data.Prediction==1])}")
            st.write(f"Total controls: {len(data[data.Prediction==0])}")
            fig = plt.figure(figsize=[20,10])
            sns.countplot(x='Status', data=data)
            plt.xlabel('Prediction Outcomes')
            plt.ylabel('Number registered')
            st.pyplot(fig)

            st.markdown('<h4 span style="color: green;">Variable enrolment statistics.</span>', unsafe_allow_html=True)
            fig, ax = plt.subplots()
            fig.set_figheight(20)
            fig.set_figwidth(30)
            data.hist(ax=ax)
            st.pyplot(fig)

            lt, rt, md= st.columns(3)
            lt.markdown('<h4 span style="color: green;">Show prediction dataset</span>', unsafe_allow_html=True)
            check = rt.checkbox("")
            if check:
                st.dataframe(data)
                download_data(data, "Dras predictions")
        except Exception as e:
            st.error(e)
        authenticator.logout("Logout", "main")

hide_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
st.markdown(hide_style, unsafe_allow_html=True)