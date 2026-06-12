import streamlit as st
from PIL import Image
import io
from rembg import remove
import cv2
import tempfile


st.title("Photo Editor")
st.write("Upload an image")
uploaded_file = st.file_uploader("Upload image")

if (uploaded_file != None):
    image = Image.open(uploaded_file)
    st.image(image)

    option = st.selectbox(
    "Choose Operation",
    ["Choose Operation", "Convert to Grayscale", "Passport Size", "Remove Background"]
    )

    if option == "Convert to Grayscale":
        grayscale_image = image.convert("L")
        st.image(grayscale_image)

        buffer = io.BytesIO()
        grayscale_image.save(buffer, format="PNG")

        st.download_button(
        "Download Grayscale Image",
        data=buffer.getvalue(),
        file_name="grayscale_image.png",
        mime="image/png")

    if option == "Passport Size":
        passport_image = image.resize((413, 531))
        st.image(passport_image)

        buffer = io.BytesIO()
        passport_image.save(buffer, format="PNG")

        st.download_button(
        "Download Passport sized Image",
        data=buffer.getvalue(),
        file_name="passport_image.png",
        mime="image/png")

    if option == "Remove Background":
            st.write("Removing background...")
            output = remove(image)
            st.image(output)

            buffer = io.BytesIO()
            output.save(buffer, format="PNG")

            st.download_button(
            "Download",
            data=buffer.getvalue(),
            file_name="output.png",
            mime="image/png")



