import streamlit as st
st.write('안녕하세요. 스트림릿을 배워 봅시다')

st.title('This is the title')
st.header('This is th header')

# Markdown
st.markdown("#This is a Markdown tittle")  # #넣을 경우 쌍따옴표 
st.markdown("##This is a Markdown tittle")
st.markdown('This is a Markdown')

st.markdown('This is a **Markdown 진하게**')
st.markdown('- item\n')
st.markdown('  - item\n')

# streamlit run test.py