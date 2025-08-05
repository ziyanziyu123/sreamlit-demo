import streamlit as st
 
video_file = open('test.mp4', 'rb')
video_bytes = video_file.read()
 
#本地视频
st.video(video_bytes,format="mp4",start_time=2)
#网络视频
st.video("http://www.w3school.com.cn/i/movie.mp4")