import streamlit as st
import fitz  # PyMuPDF
from ml_utils import classify_text
from datetime import datetime
import os

st.set_page_config(page_title="Health Record Upload", layout="wide")
st.title("📁 Patient Health Record Uploader")

# Upload PDF
uploaded_file = st.file_uploader("Upload a Health Record (PDF)", type="pdf")

if uploaded_file:
    st.success("✅ File uploaded!")

    # Save File
    os.makedirs("static/uploads", exist_ok=True)
    filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{uploaded_file.name}"
    filepath = os.path.join("static/uploads", filename)
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.info(f"File saved as: {filename}")

    # Extract Text
    pdf_doc = fitz.open(filepath)
    full_text = ""
    for page in pdf_doc:
        full_text += page.get_text()
    st.write("📄 **Extracted Text Preview**:")
    st.text(full_text[:500])

    # Predict Record Type
    predicted_type = classify_text(full_text)
    st.write(f"🧠 **Predicted Record Type**: `{predicted_type}`")
