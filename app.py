import requests
import streamlit as st

st.set_page_config(layout="wide")
st.title("Camera input demo app. Take photo and see it toonified!")

col_left, _, col_right = st.columns([5, 1, 5])


with col_left:
    x = st.camera_input(label="AAA", key="camera_input_file")

with col_right:
    if x is not None:
        st.image(x.getvalue(), caption="Your photo", use_column_width=True)
