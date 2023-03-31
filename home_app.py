# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd
import datetime
from PIL import Image

# 시각화 라이브러리 설치
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

def run_home_app():

    st.subheader("Welcome Sunny.Cho's Bigdata Analysis Study Home")
    d = st.date_input(
        "Today datetime",
        datetime.date(2023, 3, 6))
    st.write('Today is:', d)

    fname = st.text_input('내용을 입력해 주세요')
    st.title(fname)

    # image
    image = Image.open('data/flo1.png')
    st.image(image, caption='분석결과를 시각화합니다')

    # 슬라이더 바
    values = st.slider(
        '진행상황을 선택하세요.',
        0.0, 100.0, (25.0, 75.0))
    st.write('Values:', values)

    st.video('https://www.youtube.com/watch?v=fhdX3Wcxwas')

   