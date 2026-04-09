# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 14:43:22 2026

@author: USER
"""

import streamlit as st
import numpy as np
# My first app
st.title("星空地圖")
st.write("選擇觀測**時間** (24小時制)")
col1, col2 = st.columns([1,1])  # 分2個欄位

a = np.arange(1,25)
b = np.arange(0,61)


with col1:
    hr = st.selectbox("點", a)
    
with col2:
    mins = st.selectbox("分", b)

st.write("""選擇觀測**地點**""")
loca = [st.text_input("國家"),st.text_input("縣市"),st.text_input("鄉鎮市區"),st.text_input("其他(選填)")]

if st.button("go!"):
    st.write("我啥都還沒開始寫，但我可以告訴你你輸入了",hr,"點",mins,"分")
    st.write(loca[0],loca[1],loca[2])

