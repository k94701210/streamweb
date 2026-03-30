import streamlit as st
from datetime import date

st.write("提供以下方式呈現")

product=st.text_input(label= "產品名稱", value= "手機")
st.write(f"使用者輸入品項:{product}")

sdate=st.date_input("查詢日期",min_value=date(2026,1,1),max_value=date.today())
st.write(f"從您搜尋的範圍開始:{sdate}")

male=st.checkbox("男性",value=False)
female=st.checkbox("女性",value=False)

if male:
    st.write("你是輸入男性")
if female:
    st.write("你是輸入女性")