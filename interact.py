import streamlit as st

# 按钮
if st.button('点我'):
    st.write('今天是个好日子！')

# 多选框
cb = st.checkbox('确认',value=False)
if cb:
    st.write('确认成功')
else:
    st.write('没有确认')



# 单选按钮
sex = st.radio(
    label='请输入您的性别',
    options=('男', '女', '保密'),
    index=2,
    format_func=str,
    help='如果您不想透露，可以选择保密'
)

if sex == '男':
    st.write('男士您好!')
elif sex == '女':
    st.write('女士您好!')
else:
    st.write('您好!')

# 下拉框
sex = st.selectbox(
    label='请输入您的性别',
    options=('男', '女', '保密'),
    index=2,
    format_func=str,
    help='如果您不想透露，可以选择保密'
)

if sex == '男':
    st.write('男士您好!')
elif sex == '女':
    st.write('女士您好!')
else:
    st.write('您好!')


# 多选框
options = st.multiselect(
    label='请问您喜欢吃什么水果',
    options=('橘子', '苹果', '香蕉', '草莓', '葡萄'),
    default=None,
    format_func=str,
    help='选择您喜欢吃的水果'
)

st.write('您喜欢吃的是', options)


# 创建一个滑块，允许用户在一个范围内选择一个数值
age = st.slider(label='请输入您的年龄', 
                min_value=0, 
                max_value=100, 
                value=0, 
                step=1, 
                help="请输入您的年龄"
               )
 
st.write('您的年龄是', age)


# 单行文本输入
name = st.text_input('请输入用户名',  max_chars=100, help='最大长度为100字符')

# 根据用户输入进行操作
st.write('您的用户名是：', name)

# 数字输入框
age = st.number_input(label = '请输入您的年龄',
                       min_value=0,
                       max_value=100,
                       value=0,
                       step=1,
                       help='请输入您的年龄'
                      )
st.write('您的年龄是', age)

# 多行文本输入
text = st.text_area(label = '请输入文本',
                     value='',
                     height=5,
                     max_chars=200,
                     help='最大长度限制为200')
st.write('您的输入是', text)

# 时间输入框
t = st.time_input(label = '请输入一个时间',
                   value=None,
                   help='请输入一个时间')
st.write('您输入的时间是：', t)


# 各种类型提示信息
st.error('错误信息')
st.warning('警告信息')
st.info('提示信息')
st.success('成功信息')
st.exception('异常信息')




#columns参数表示列数
left_column, right_column = st.columns(2)

# 左边列设置
with left_column:
    #返回值为选中的选项值
    chosen = st.radio(
        label='电脑品牌',
        options=('苹果','华为','小米')
    )
    st.write(f'你选择的品牌是: {chosen}')

# 右边列设置
with right_column:
    # 返回值为选中的选项值
    chosen = st.radio(
        label='手机品牌',
        options=('苹果','华为','小米')
    )
    st.write(f'你选择的品牌是: {chosen}')