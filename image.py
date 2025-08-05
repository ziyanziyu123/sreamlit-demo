import streamlit as st
from PIL import Image

image = Image.open('image_text.png')

st.image(image, caption='标题', width=500)