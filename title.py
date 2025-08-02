# 导入streamlit库
import streamlit as st

# 设置标题和子标题
st.title("这是一个标题")
st.header("这是一个较小的标题")
st.subheader("这是一个相对较小的标题")

# 显示文本内容,支持Markdown语法
st.markdown("# 静夜思")
st.markdown("床前**明月**光，疑是**地上**霜。")
st.markdown("**举头**望明月，低头思故乡。")

# 显示文本内容,不支持Markdown语法
st.text("这是一个简单的应用程序。")