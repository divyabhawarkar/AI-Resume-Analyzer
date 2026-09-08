# 📄 AI Resume Analyzer & Career Recommendation System

An AI-powered web application that analyzes resumes, extracts important information and skills, calculates a resume score, recommends suitable career paths, and identifies missing skills.

## 🚀 Features

- 📄 Upload Resume in PDF or DOCX format
- 🔍 Extract Resume Text using PDF parsing and OCR
- 👤 Extract Candidate Information
  - Name
  - Email
  - Phone Number
- 📝 Extract Professional Summary
- 🎓 Extract Education Details
- 💼 Extract Work Experience / Internship
- 🛠️ Detect Technical and Professional Skills
- 📊 Calculate Resume Score
- 🎯 Recommend Suitable Career Paths
- 📚 Perform Skill Gap Analysis
- ⚠️ Identify Skills that the candidate should learn
- 🌐 Simple and user-friendly Streamlit interface

## 🧠 How It Works

1. User uploads a resume in PDF or DOCX format.
2. The system extracts the resume text.
3. Important candidate information is identified.
4. Skills are detected from the resume.
5. The resume is evaluated and a score is generated.
6. Suitable career options are recommended.
7. The system compares existing skills with required career skills.
8. Missing skills are displayed as a skill gap.

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- PDFPlumber
- PyMuPDF
- Pytesseract
- Python-DOCX
- Regular Expressions
- OCR

## 📁 Project Structure

```text
AI-Resume-Analyzer/
│
├── data/
│   └── careers.csv
│
├── src/
│   ├── __init__.py
│   ├── parser.py
│   ├── skills.py
│   ├── analyzer.py
│   ├── recommender.py
│   ├── scoring.py
│   └── skill_gap.py
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
