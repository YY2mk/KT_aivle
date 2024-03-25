import streamlit as st
import folium
import pandas as pd

# '.\streamlit\covid_map.csv' 읽어서 map_data에 저장하기
map_data = pd.read_csv('covid_map.csv')

# 1. 타이틀과 캡션 표시하기
# 타이틀 : 'Covid-19 감염현황'
# 캡션 : 'Displaying geographical data on a map using Streamlit and Folium'
st.title('Covid-19 감염현황')
st.caption('Displaying geographical data on a map using Streamlit and Folium')

# 2. checkbox를 이용하여 checkbox 선택여부에 따라
#    write 코드를 사용하여 화면에 데이터프레임 값 나타내기 
if st.checkbox('Display Data?'):
    st.write(map_data)

# folium.Map(): Folium에서 지도 객체를 생성
# location: 지도가 초기에 어떤 위치에서 시작할지를 정의 (위도-latitude, 경도-longitude)
# map_data['lat'].mean()과 map_data['lon'].mean(): 평균 위도와 경도 위치를 지도 중심으로 설정
# zoom_start: 이 매개변수는 지도의 초기 확대 수준 (default=10, 숫자가 클수록 확대)

my_map = folium.Map( location=[map_data['lat'].mean(), map_data['lon'].mean()], zoom_start=3 )


# 지도에 원형 마커와 값 추가
for index, row in map_data.iterrows(): # 데이터프레임 한 행 씩 index, row에 담아서 처리
    folium.CircleMarker( # 원 표시 선언
    location=[row['lat'], row['lon']], # 원 중심- 위도, 경도
    radius=row['value'] / 5000, # 원의 반지름
    color='pink', # 원의 테두리 색상
    fill=True, # 원을 채움
    fill_opacity=1.0 # 원의 내부를 채울 때의 투명도
    ).add_to(my_map) # my_map에 원형 마커 추가
    folium.Marker( # 값 표시 선언
    location=[row['lat'], row['lon']], # 값 표시 위치- 위도, 경도
    icon=folium.DivIcon(html=f"<div>{row['name']} {row['value']}</div>"), # row['name'], row['value'] 표시
    ).add_to(my_map) # my_map에 값 추가


# 타이틀과 캡션 표시하기
st.title('Map with Location Data')
st.caption('Displaying geographical data on a map using Streamlit and Folium')
# 지도 그리기
# st.components.v1.html : Streamlit 라이브러리의 components 모듈에서 html 함수 사용
# ._repr_html_() : 지도를 HTML 형식으로 표시
st.components.v1.html(my_map._repr_html_(), width=800, height=600)


# 파일실행: File > New > Terminal(anaconda prompt) → python -m streamlit run streamlit\7-3.folium_covid.py