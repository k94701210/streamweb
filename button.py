import streamlit as st
import pandas as pd

st.title("展示 button 的使用方法")

def open_csv():
    path = r"C:\Projects\Olist_repo\dataset\巴西電商資料集\olist_sellers_dataset.csv"
    st.write(f"正在開啟檔案：{path}")
    
    try:
        df = pd.read_csv(path) 
        st.dataframe(df)
    except Exception as e:
        st.error(f"找不到檔案或讀取錯誤：{e}")

click1 = st.button("這是按鈕1", key="btn1", type="primary")
click2 = st.button("這是按鈕2", key="btn2", type="secondary")

click3 = st.button("這是按鈕3 (讀取資料)", key="btn3", type="tertiary")

if click1:
    st.write("點了按鈕1")

if click2:
    st.write("點了按鈕2")

if click3:
    st.write("點了按鈕3，準備讀取 CSV...")
    open_csv()