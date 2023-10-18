#!/usr/bin/env python3

import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Dras",
                   page_icon=":sign-intersection-fill:",
                   layout="wide"
                   )
st.markdown('<h1 span style="color: blue;">DIABETES RISK ASSESSMENT.</span>', unsafe_allow_html=True)
st.markdown('<h3 span style="color: green;">CONTEXT.</span>', unsafe_allow_html=True)
st.write("Diabetes is a serious chronic disease in which individuals lose the ability to effectively\
    regulate levels of glucose in the blood, and can lead to reduced quality of life and life expectancy.\
    After different foods are broken down into sugars during digestion, the sugars are then released into\
    the bloodstream. This signals the pancreas to release insulin. Insulin helps enable cells within the body\
    to use those sugars in the bloodstream for energy. Diabetes is generally characterized by either the body\
    not making enough insulin or being unable to use the insulin that is made as effectively as needed.")
st.write("Complications like heart disease, vision loss, lower-limb amputation, and kidney disease are associated\
    with chronically high levels of sugar remaining in the bloodstream for those with diabetes. While there is no\
    cure for diabetes, strategies like losing weight, eating healthily, being active, and receiving medical treatments\
    can mitigate the harms of this disease in many patients.")
st.write("Early diagnosis can lead to lifestyle changes and more effective treatment, making predictive models for\
    diabetes risk important tools for public and public health officials.")
st.markdown('<h3 span style="color: green;">CONTENT.</span>', unsafe_allow_html=True)
st.write("DRAS (Diabetes Risk Assessment system) model is a supervised machine learning model trained using logistic\
    regression model to predict the two classes of Diabetes_binary in BRFSS (Behavioral Risk Factor Surveillance System) dataset obtained from kaggle.\
    Class 0 represents no diabetes while 1 represents prediabetes or diabetes.")
st.markdown('<h3 span style="color: green;">WHY DRAS?</span>', unsafe_allow_html=True)
st.write("1. Early Detection: One of the primary objectives is to identify individuals at risk of developing diabetes at an early stage. Early detection allows\
    for timely intervention and lifestyle modifications, which can help prevent or delay the onset of diabetes.")
st.write("2. Prevention and Intervention: DRAS provides personalized risk profiles for individuals at risk.This information can direct individuals to make informed\
    decisions about their lifestyle, such as adopting healthier diets, increasing physical activity, and managing stress, to reduce their risk of diabetes.")
st.write("3. Education and Awareness: DRAS raises awareness about the risk factors associated with diabetes\
    and help individuals better understand the importance of a healthy lifestyle and regular check-ups.")
st.write("4. Empowerment and Patient Engagement: DRAS can empower individuals to take control of their health by providing them with actionable information\
    and encouraging them to engage in healthier behaviors")
st.markdown('<h3 span style="color: green;">MISSION.</span>', unsafe_allow_html=True)
st.write("To promote early detection, prevention, and management of diabetes by identifying at-risk individuals and potential causes.")

stats = st.button('Show more')
if stats:
        switch_page("Statistics")
hide_style = """
         <style>
         #MainMenu {visibility: hidden;}
         footer {visibility: hidden;}
         header {visibility: hidden;}
         </style>
         """
#st.markdown(hide_style, unsafe_allow_html=True)