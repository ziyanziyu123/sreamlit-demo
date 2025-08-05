import streamlit as st
import time 
import pandas as pd
 
@st.cache_data
def fetch_data(url):
    time.sleep(5)
    return pd.read_csv(url)
 
'''
数据表d1需要从url读取数据，而在加载之后被缓存下来，当数据表d2获取数据时，输入的是相同的url参数，
则不会再次执行该函数，而是直接从缓存中读取数据。使用st.cache_data.clear()清空缓存后，d3则需要重新从url读取。
'''


url1 = 'https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data'
st.write('开始执行url1')
d1 = fetch_data(url1)
st.write(d1)
 
url2 = 'https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data'
st.write('开始执行url2')
d2 = fetch_data(url2)
st.write(d2)
 
st.cache_data.clear()
 
url3 = 'https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data'
st.write('开始执行url3')
d3 = fetch_data(url3)
st.write(d3)