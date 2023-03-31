# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd
import datetime

# 시각화 라이브러리 설치
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

def run_eda_app():

    st.subheader("탐색적 자료 분석 페이지입니다")
    
    #데이터셋 불러오기
    iris_df = pd.read_csv('data\iris.csv')
    #st.dataframe(iris_df)

    # 메뉴지정
    submenu = st.sidebar.selectbox("Submenu", ['기술통계량', '그래프'])
    if submenu == "기술통계량":
        st.dataframe(iris_df)

        with st.expander("Data types"):
            result = pd.DataFrame(iris_df.dtypes).transpose()
            result.index =["데이터 타입"]
            st.dataframe(result)

        with st.expander("기술 통계량"):
            result2 = pd.DataFrame(iris_df.describe()).transpose()  # tranpose : 테이블의 행과 열의 위치 바꾸기.
            st.dataframe(result2)

        with st.expander("타겟분포"):
            result3 = iris_df['species'].value_counts().transpose()
            st.dataframe(result3)
    
    # 분석 결과를 대시보드로 시각화 한다./보고서 작성
    elif submenu =="그래프":
        st.subheader("Plots")
        fig1 =px.scatter(iris_df,
                         x='sepal_width',
                         y='sepal_length',
                         color='species',
                         size = 'petal_width',
                         hover_data=['petal_length'],
                         title ="산점도 그래프")
        st.plotly_chart(fig1)

        # 레이아웃 분리
        col1, col2 = st.columns(2)
        with col1: 
            #st.subheader("col1") 최초 영역 구분
            with st.expander("박스플롯 with Seaborn"):
                #seaborn 그래프
                fig, ax= plt.subplots()
                sns.boxplot(iris_df, x ='species', y='sepal_length', ax=ax)
                st.pyplot(fig)
        with col2:
            #st.subheader("col2") 최초 영역 구분
            with st.expander("히스토그램 with Seaborn"):
                #seaborn 그래프
                fig, ax= plt.subplots()
                ax.hist(iris_df['sepal_length'], color='green')
                st.pyplot(fig)
        
        tab1, tab2 = st.tabs(['Tab 1', 'Tab 2'])
        with tab1:
            st.write("Tab 1")
            val_species = st.selectbox('종선택', ('Iris-setosa', 'Iris-versicol', 'Iris-virginica'))
            st.write('종 선택 :', val_species)

            result = iris_df[iris_df['species'] == val_species]
            st.dataframe(result)

            fig1 = px.scatter(result, x = 'sepal_width',
                              y='sepal_length',
                              size='petal_width',
                              hover_data=['petal_length'])
            st.plotly_chart(fig1)

        with tab2:
            st.write("Tab 2")


       
            
    else:
        st.write("저 아님")

    