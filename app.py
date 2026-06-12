import streamlit as st
from PIL import Image
import io
from rembg import remove
import cv2
import tempfile


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Photo Editor",
    page_icon="🖼️",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}

/* Main Title */
h1 {
    text-align: center;
    color: #00E5FF !important;
    font-size: 3rem !important;
    font-weight: bold;
}

/* Headings */
h2, h3, h4, h5, h6 {
    color: white !important;
}

/* Normal text */
p, label, span {
    color: white !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: rgba(255,255,255,0.08);
}

[data-testid="stSidebar"] * {
    color: white !important;
}

/* File Uploader Box */
[data-testid="stFileUploader"] {
    background-color: rgba(255,255,255,0.15);
    border-radius: 15px;
    padding: 15px;
}

/* File Uploader Text */
[data-testid="stFileUploader"] * {
    color: #333333 !important;
}

/* Images */
div[data-testid="stImage"] img {
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.4);
}

/* Buttons */
.stButton > button {
    background-color: #00E5FF;
    color: black;
    border-radius: 10px;
    border: none;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #00B8D4;
    color: white;
}

/* Download Buttons */
.stDownloadButton > button {
    background-color: #00E5FF;
    color: black;
    border-radius: 10px;
    border: none;
    font-weight: bold;
}

.stDownloadButton > button:hover {
    background-color: #00B8D4;
    color: white;
}

/* Success Messages */
[data-testid="stAlert"] {
    border-radius: 10px;
}

/* Selectbox Label */
.stSelectbox label {
    color: white !important;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)



# ---------------- TITLE ---------------- #

st.markdown("""
<h1>🖼️ AI Photo Editor</h1>
<h4 style='text-align:center; color:white;'>
Transform your photos with AI-powered tools
</h4>
""", unsafe_allow_html=True)


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



