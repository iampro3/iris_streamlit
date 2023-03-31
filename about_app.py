# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd
import datetime
from PIL import Image


# 시각화 라이브러리 설치
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

def run_about_app():

    st.subheader("Sunny.Cho's Bigdata Study : 소개 페이지 입니다")

    # image
    image = Image.open('data/flo2.jpg')
    st.image(image, caption='분석 결과 보고 사이트입니다')

    # selectbox 
    programings = ['Python', 'Java', 'HTML', 'CSS', 'JS', 'C, C++']
    choice = st.selectbox('프로그래밍 언어: ', programings)
    st.write(f'{choice} 언어를 선택함')

    spoken_lang =("한국어", "영어", "일본어", "중국어", "독일어")   
    mylangchoice = st.multiselect("언어선택", spoken_lang, default ="영어")
    st.write("선택:", mylangchoice)

       # col1, col2 
    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
        st.session_state.disabled = False
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.checkbox("Disable selectbox widget", key="disabled")
        st.radio(
            "Set selectbox label visibility 👉",
            key="visibility",
            options=["visible", "hidden", "collapsed"],
    )
    with col2:
        option = st.selectbox(
            "연락 방식을 선택하세요",
            ("Email", "Home phone", "Mobile phone"),
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
    )
        
    #color = st.color_picker('색상 선택')
    #st.write(color)

    st.image(image, caption='Java & 빅데이터 과정 커리큘럼)
    image = Image.open('data/info0.jpg')
    image = Image.open('data/info1.jpg')
    image = Image.open('data/info2.jpg')
    image = Image.open('data/info3.jpg')
    
   
