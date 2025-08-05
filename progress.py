import streamlit as st
import time
st.write("模拟长时间的计算...")
 
# 创建一个动态显示数据的容器，用于动态显示进度条的进度数值
value = st.empty()
#创建进度条，进度条初始值为0
bar = st.progress(0)
for i in range(50):
    #这是动态显示的数值
    value.text(f'Iteration {i+1}')
    # 更新进度条
    bar.progress(i+1)
    time.sleep(0.1)
st.write('运行结束!')


#侧边栏下拉框
add_selectbox = st.sidebar.selectbox(
    label="通讯方式选项",
    options=('微信', 'QQ', '手机', '邮件')
)
#获取下拉选项
st.write("下拉选项: ", add_selectbox)

#侧边栏滑块
add_slider = st.sidebar.slider(
    label="选择一个范围的值",
    min_value=0.0, max_value=100.0, value=(25.0, 75.0)
)
#获取滑块的值
st.write("值的范围: ", add_slider)