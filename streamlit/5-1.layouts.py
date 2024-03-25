import streamlit as st

st.title('Unit 5. Layouts & Containers')
st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/layout')

# sidebar- with 사용하기 📧  📱  ☎︎
with st.sidebar: 
    st.header('1. Sidebar')

add_selectbox = st.sidebar.selectbox('어떻게 연락을 드릴까요?', 
                                     ('Email', 'Mobile phone', 'Office phone'))

if add_selectbox == 'Email':
    st.sidebar.title('📧')
elif add_selectbox == 'Mobile phone':
    st.sidebar.title('📱')
else:
    st.sidebar.title('☎︎')

# columns  
# 고양이 https://images.pexels.com/photos/2071873/pexels-photo-2071873.jpeg?auto=compress&cs=tinysrgb
# 개     https://images.pexels.com/photos/3361739/pexels-photo-3361739.jpeg?auto=compress&cs=tinysrgb
# 부엉이 https://images.pexels.com/photos/3737300/pexels-photo-3737300.jpeg?auto=compress&cs=tinysrgb

st.header('2. Columns')
col1, col2, col3 = st.columns(3)

with col1:
    st.text('고양이')
    st.image('https://images.pexels.com/photos/2071873/pexels-photo-2071873.jpeg?auto=compress&cs=tinysrgb')

with col2:
    st.text('개')
    st.image('https://images.pexels.com/photos/3361739/pexels-photo-3361739.jpeg?auto=compress&cs=tinysrgb')
    
with col3:
    st.text('올빼미')
    st.image('https://images.pexels.com/photos/3737300/pexels-photo-3737300.jpeg?auto=compress&cs=tinysrgb')
   
# tabs - 
width=200

st.header('3. Tabs')
tab1, tab2, tab3 = st.tabs(['고양이', '개', '올빼미'])

with tab1:
    st.text('Cat')
    st.image('https://images.pexels.com/photos/2071873/pexels-photo-2071873.jpeg?auto=compress&cs=tinysrgb', width=width)

with tab2:
    st.text('Dog')
    st.image('https://images.pexels.com/photos/3361739/pexels-photo-3361739.jpeg?auto=compress&cs=tinysrgb', width=width)

with tab3:
    st.text('Owl')
    st.image('https://images.pexels.com/photos/3737300/pexels-photo-3737300.jpeg?auto=compress&cs=tinysrgb', width=width)
    
# 파일실행: File > New > Terminal(anaconda prompt) → python -m streamlit run streamlit\5-1.layouts.py