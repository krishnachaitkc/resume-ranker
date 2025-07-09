#Resume Ranker for HR Portal

A simple web app to rank resumes based on their similarity to a given job description using Natural Language Processing (TF-IDF + Cosine Similarity).

---

 Features

- Upload multiple resumes (PDF or DOCX)
- Paste job description
- Automatically ranks resumes by relevance
- Displays scores in a clean table
- Built using Streamlit for quick UI

##Tech Stack

- **Frontend**: Streamlit
- **NLP**: scikit-learn, TF-IDF, cosine similarity
- **Parsing**: PyMuPDF (`fitz`), docx2txt
- **Language**: Python

---

##How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
