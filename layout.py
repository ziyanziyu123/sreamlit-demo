import streamlit as st
 
# 方式1：使用对象表示法添加选择框
add_selectbox = st.sidebar.selectbox(
    "您希望如何联系您？",
    ("电子邮件", "家庭电话", "移动电话")
)
# 方式2：使用“with”语法添加单选按钮
with st.sidebar:
    add_radio = st.radio(
        "选择一种运输方式",
        ("标准（5-15天）", "快递（2-5天）")
    )


st.sidebar.write(add_selectbox)
st.sidebar.write(add_radio)



'''通过调用 st.columns，您可以插入多个多元素容器，并将它们布局为并排的形式。
返回的是一个容器对象的列表，每个对象都可以用来添加元素。您可以选择使用“with”语法（更推荐）
或者直接在容器对象上调用方法来添加元素。'''


col1, col2, col3 = st.columns(3)
with col1:
    st.header("一只猫")
    st.image("https://static.streamlit.io/examples/cat.jpg")
with col2:
    st.header("一只狗")
    st.image("https://static.streamlit.io/examples/dog.jpg")
with col3:
    st.header("一只猫头鹰")
    st.image("https://static.streamlit.io/examples/owl.jpg")


# 使用 st.expander 您可以插入一个可展开或折叠的容器，用于包含多个元素。
with st.expander("查看说明"):
    st.write("""
        上面的图表展示了我为您选择的一些数字。
        这些数字是通过真实的骰子摇出来的，所以它们*保证*是随机的。
    """)
    st.image("https://static.streamlit.io/examples/dice.jpg")