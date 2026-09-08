import re


# ---------------------------------------
# Pharmaceutical Skills
# ---------------------------------------

PHARMA_SKILLS = [
    "Quality Assurance",
    "Quality Control",
    "Regulatory Affairs",
    "Pharmacovigilance",
    "GMP",
    "Good Manufacturing Practices",
    "Documentation",
    "Quality Management Systems",
    "QMS",
    "MSDS",
    "Chemical Safety Handling",
    "Microbiology",
    "Quality Control Microbiology",
    "SOP Documentation",
    "Microsoft Office",
    "Microsoft Word",
    "Microsoft Excel",
    "Microsoft PowerPoint",
    "Word",
    "Excel",
    "PowerPoint",
    "Problem Solving",
    "Analytical Thinking",
    "Laboratory Operations",
    "Regulatory Compliance",
    "Pharmaceutical Quality Systems",
    "Drug Delivery",
    "Novel Drug Delivery Systems",
    "Formulation",
    "Stability Testing",
    "Quality Evaluation"
]


# ---------------------------------------
# Technical / IT Skills
# ---------------------------------------

TECHNICAL_SKILLS = [
    "Python",
    "Java",
    "C++",
    "C#",
    "JavaScript",
    "HTML",
    "CSS",
    "React",
    "Node.js",
    "SQL",
    "MySQL",
    "MongoDB",
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "Data Science",
    "Natural Language Processing",
    "NLP",
    "Computer Vision",
    "TensorFlow",
    "PyTorch",
    "Scikit-learn",
    "OpenCV",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Git",
    "GitHub",
    "Docker",
    "AWS",
    "Azure",
    "Power BI"
]


# ---------------------------------------
# Combine Skills
# ---------------------------------------

SKILLS = PHARMA_SKILLS + TECHNICAL_SKILLS


def extract_skills(resume_text):
    """
    Extract technical and professional skills
    from resume text.
    """

    found_skills = []

    # Normalize text
    text = resume_text.lower()

    for skill in SKILLS:

        skill_lower = skill.lower()

        # Exact phrase matching
        pattern = r"(?<!\w)" + re.escape(skill_lower) + r"(?!\w)"

        if re.search(pattern, text):

            found_skills.append(skill)

    return found_skills