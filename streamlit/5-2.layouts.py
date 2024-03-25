import streamlit as st
st.caption('참조사이트: https://docs.streamlit.io/library/get-started/multipage-apps/create-a-multipage-app')

# 페이지 선언 (🎈 ❄️ 🎉)
def main_page():
    st.title('Main page 🎈')
    st.sidebar.title('Side Main 🎈')

def page2():
    st.title('Page2 ❄️')
    st.sidebar.title('Side2 ❄️')

def page3():
    st.title('Page3 🎉')
    st.sidebar.title('Page3 🎉')
    
# 딕셔너리 선언 {  ‘selectbox항목’ : ‘페이지명’ …  }
page_names_to_funcs = {'Main Page': main_page, 'Page 2': page2, 'Page 3': page3}

# 사이드 바에서 selectbox 선언 & 선택 결과 저장
selected_page = st.sidebar.selectbox('Select a Page', page_names_to_funcs.keys())

# 해당 페이지 부르기
page_names_to_funcs[selected_page]()

# 파일실행: File > New > Terminal(anaconda prompt) → python -m streamlit run streamlit\5-2.layouts.py