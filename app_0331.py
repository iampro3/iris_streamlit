# -*- coding:utf-8 -*-
import streamlit as st
from eda_app import run_eda_app
from home_app import run_home_app
from about_app import run_about_app
from ml_app import run_ml_app


import datetime

# 구조를 app 파일에서 전체 틀을 구성하고 실행파일은 eda_app 파일에서 실행한다.

def main():
    st.markdown("자료 분석 사이트")
    menu = ["Home", "탐색적 자료분석", "머신러닝", "About"]
    choice = st.sidebar.selectbox("메뉴", menu)

    if choice == "Sunny.Cho's Bigdata Analysis Study Home":        
        #st.subheader("Home")
        run_home_app()

    elif choice =="탐색적 자료분석":
        run_eda_app()
    elif choice == "머신러닝":
        run_ml_app()
    else:
        st.subheader("About")
        run_about_app()






if __name__ == "__main__":
    main()