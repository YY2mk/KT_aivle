# streamlit, pandas 라이브러리 불러오기 
import streamlit as st
import pandas as pd


st.title('Unit 3. Data display elements')
st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/data')

st.header(' 1. Metric')     # °C
st.metric(label='Temperature', value='30.5°C', delta='2.5°C')
st.metric(label='Temperature', value='28°C', delta='-2.5°C')

st.header('2. columns')     # °C
col1, col2, col3 = st.columns(3)
col1.metric(label='기온', value='30.5°C', delta='2.5°C')
col2.metric(label='풍속', value='9 mph', delta='-8%')
col3.metric(label='습도', value='86%', delta='4%')


st.header('3. Dataframe 조회하기')

# 파일 위치- https://raw.githubusercontent.com/huhshin/streamlit/master/data_titanic.csv
titanic = pd.read_csv('https://raw.githubusercontent.com/huhshin/streamlit/master/data_titanic.csv')

st.markdown('- st.dataframe(상위 15행)')
titanic_15 = titanic.head(15)
st.dataframe(titanic_15) 
st.caption('dataframe, write- 10개 행  기준 스크롤, 열 크기조정, 열 정렬, 테이블  확대')


st.markdown('- st.write(상위 15행)')
st.write(titanic_15) # 문자열 들어갈 수 있음

st.markdown('- st.table(상위 15행)')
st.table(titanic_15)
st.caption('table- 형태 고정')


# 파일실행: File > New > Terminal(anaconda prompt) → python -m streamlit run streamlit\3.data.py