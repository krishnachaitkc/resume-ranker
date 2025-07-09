import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import docx2txt
import PyPDF2
import pandas as pd

def extract_text(file):
    if file.name.endswith('.pdf'):
        reader = PyPDF2.PdfReader(file)
        return "".join([page.extract_text() or "" for page in reader.pages])
    elif file.name.endswith('.docx'):
        return docx2txt.process(file)
    return ""

st.title("📄 Resume Ranker for HR Portal")
job_desc = st.text_area("Paste Job Description", height=200)

uploaded_files = st.file_uploader("Upload Resumes", accept_multiple_files=True, type=["pdf", "docx"])
if st.button("Rank Resumes") and job_desc and uploaded_files:
    resume_texts = [extract_text(f) for f in uploaded_files]
    tfidf = TfidfVectorizer(stop_words='english')
    vectors = tfidf.fit_transform([job_desc] + resume_texts)
    scores = cosine_similarity(vectors[0:1], vectors[1:])[0]

    df = pd.DataFrame({
        'Resume': [f.name for f in uploaded_files],
        'Score': [round(score * 100, 2) for score in scores]
    }).sort_values(by='Score', ascending=False)

    st.success("Ranking Complete!")
    st.dataframe(df)
else:
    st.info("Please paste a job description and upload resumes.")
