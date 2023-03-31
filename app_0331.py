
# -*- coding:utf-8 -*-
import streamlit as st
from eda_app import run_eda_app

# 구조를 app 파일에서 전체 틀을 구성하고 실행파일은 eda_app 파일에서 실행한다.

def main():
    st.markdown("Hello world")
    menu = ["Home", "탐색적 자료분석", "머신러닝", "About"]
    choice = st.sidebar.selectbox("메뉴", menu)

    if choice == "Home":
        st.subheader("Home")
    elif choice =="탐색적 자료분석":
        run_eda_app()
    elif choice == "머신러닝":
        pass
    else:
        st.subheader("About")


if __name__ == "__main__":
    main()