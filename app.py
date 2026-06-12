import streamlit as st
from PIL import Image

st.title("Photo Editor")
st.write("Upload an image")
uploaded_file = st.file_uploader("Upload image")

if (uploaded_file != None):
    image = Image.open(uploaded_file)
    st.image(image)

button = st.button("Convert to Grayscale")

if button == True:
    grayscale_image = image.convert("L")
    st.image(grayscale_image)