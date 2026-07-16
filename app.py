import streamlit as st

from utils import extract_text_from_pdf, extract_text_from_image
from llm import explain_text, summarize_text, generate_questions

st.set_page_config(
    page_title="Document Intelligence",
    page_icon="📄",
    layout="centered"
)

st.title("📄 Document Intelligence")
st.subheader("Document Intelligence and Image Analyzer")

uploaded_file = st.file_uploader(
    "Upload PDF or Image",
    type=["pdf", "png", "jpg", "jpeg"]
)

text = ""

if uploaded_file:

    if uploaded_file.name.endswith(".pdf"):
        text = extract_text_from_pdf(uploaded_file)

    else:
        text = extract_text_from_image(uploaded_file)

    st.success("File uploaded successfully.")

    st.subheader("Extract Text")

    if st.button("Extract Text"):
        st.text_area(
            "Extracted Text",
            value=text,
            height=400
        )

    if st.button("Extract Questions"):
        questions = generate_questions(text)
        st.text_area(
            "Questions",
            value=questions,
            height=300
        )
    

    if st.button("Explain"):
        explanation = explain_text(text)
        st.text_area(
            "Explanation",
            value=explanation,
            height=250
        )

    if st.button("Summary"):
        summary = summarize_text(text)
        st.text_area(
            "Summary",
            value=summary,
            height=200
        )