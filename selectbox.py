import streamlit as st

lang=st.selectbox(f"請選擇:",("Java","Python","C#","JavaScript"))
st.write("你挑選了"{lang}")
         