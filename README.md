# 🖼️ AI Photo Editor

A simple AI-powered Photo Editor built using **Python**, **Streamlit**, **Pillow**, and **RemBG**.

The application allows users to upload images and perform common photo editing operations such as:

* Convert Image to Grayscale
* Generate Passport Size Photos
* Remove Image Background
* Download Processed Images

---

## 🚀 Features

### 📤 Upload Image

Users can upload images directly from their device.

### ⚫ Convert to Grayscale

Transform colored images into black-and-white grayscale images.

### 📸 Passport Size Conversion

Resize uploaded images to passport-photo dimensions.

### ✂️ Background Removal

Remove image backgrounds using AI-powered segmentation.

### 📥 Download Processed Images

Download edited images instantly.

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Pillow (PIL)
* RemBG
* Git & GitHub

---

## 📂 Project Structure

Photo-Editor/

├── app.py

├── .gitignore

├── README.md

└── requirements.txt

---

## 🔄 Application Workflow

1. User uploads an image.
2. Image is displayed in the application.
3. User selects an operation:

   * Convert to Grayscale
   * Passport Size
   * Remove Background
4. Selected operation is applied.
5. Processed image is displayed.
6. User downloads the result.

---

## 📊 Flowchart

Start

↓

Upload Image

↓

Display Uploaded Image

↓

Select Operation

↓

┌──────────────────────┐
│ Grayscale            │
│ Passport Size        │
│ Remove Background    │
└──────────────────────┘

↓

Process Image

↓

Display Result

↓

Download Image

↓

End

---

## ⚙️ Installation

### Clone Repository

git clone https://github.com/Iksha-Goomber/Photo-Editor.git

cd Photo-Editor

### Create Virtual Environment

python -m venv .venv

### Activate Virtual Environment

Windows:

.venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Run Application

streamlit run app.py

---

## 🎯 Future Improvements

* White Background Generator
* Black Background Generator
* Video Processing Support
* Batch Image Processing
* Drag & Drop Interface

---

## 👩‍💻 Author

Iksha Goomber

ENC Student | Thapar University

Python • AI/ML • Data Science Enthusiast
