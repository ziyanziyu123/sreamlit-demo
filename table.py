'''
st.dataframe()：以表格的形式呈现数据，支持Pandas的特有功能，如排序、过滤等，并且会自动适应数据框的大小，如果数据框太大，它会自动启用滚动条。
参数如下：
①width：UI元素的期望宽度，单位为像素，类型为Int或None，如果是None的话，Streamlit将基于页面宽度计算元素宽度。
②height：UI元素的期望高度，单位为像素，类型为Int或None。

st.table()：用于显示通用表格数据，不仅支持Pandas，还可以处理列表、元组等可迭代数据结构。但st.table仅用于显示数据，而不提供诸如排序和过滤等数据框专有功能。

'''

import streamlit as st
import pandas as pd
import numpy as np
 
random_data = np.random.rand(100, 10)
df = pd.DataFrame(random_data, columns=[f'Col{i}' for i in range(1, 11)])
 
st.dataframe(df)
st.table(df)