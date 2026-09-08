# ---------------------------------------
# Skill Gap Analysis
# ---------------------------------------


CAREER_SKILLS = {

    "Quality Assurance": [
        "Quality Assurance",
        "GMP",
        "Documentation",
        "QMS",
        "SOP Documentation",
        "Regulatory Compliance"
    ],

    "Regulatory Affairs": [
        "Regulatory Affairs",
        "GMP",
        "Documentation",
        "QMS",
        "Regulatory Compliance"
    ],

    "Pharmacovigilance": [
        "Pharmacovigilance",
        "Documentation",
        "Analytical Thinking",
        "Microsoft Office"
    ],

    "Quality Control": [
        "Quality Control",
        "Microbiology",
        "GMP",
        "MSDS",
        "Documentation"
    ],

    "Clinical Research": [
        "Clinical Research",
        "Documentation",
        "Pharmacovigilance",
        "Analytical Thinking"
    ],

    "Formulation Scientist": [
        "Formulation",
        "Drug Delivery",
        "Stability Testing",
        "Quality Evaluation"
    ],

    "Production Pharmacist": [
        "GMP",
        "Documentation",
        "Quality Control",
        "Good Manufacturing Practices"
    ],

    "Data Analyst": [
        "Python",
        "SQL",
        "Excel",
        "Power BI",
        "Data Analysis"
    ],

    "Machine Learning Engineer": [
        "Python",
        "Machine Learning",
        "Scikit-learn",
        "TensorFlow",
        "NumPy"
    ],

    "Data Scientist": [
        "Python",
        "Machine Learning",
        "Statistics",
        "Pandas",
        "NumPy"
    ],

    "Web Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Git"
    ],

    "Software Developer": [
        "Python",
        "Java",
        "C++",
        "SQL",
        "Git"
    ]
}


# ---------------------------------------
# Normalize Skill
# ---------------------------------------

def normalize_skill(skill):

    aliases = {

        "good manufacturing practices": "gmp",

        "quality management systems": "qms",

        "microsoft excel": "excel",

        "microsoft word": "word",

        "microsoft powerpoint": "powerpoint",

        "novel drug delivery systems": "drug delivery"
    }

    skill = str(skill).lower().strip()

    return aliases.get(skill, skill)


# ---------------------------------------
# Get Matching Skills
# ---------------------------------------

def get_matching_skills(resume_skills, career):

    required_skills = CAREER_SKILLS.get(
        career,
        []
    )

    resume_normalized = {
        normalize_skill(skill)
        for skill in resume_skills
    }

    matching_skills = []

    for skill in required_skills:

        if normalize_skill(skill) in resume_normalized:

            matching_skills.append(skill)

    return matching_skills


# ---------------------------------------
# Get Missing Skills
# ---------------------------------------

def get_skill_gap(resume_skills, career):

    required_skills = CAREER_SKILLS.get(
        career,
        []
    )

    resume_normalized = {
        normalize_skill(skill)
        for skill in resume_skills
    }

    missing_skills = []

    for skill in required_skills:

        if normalize_skill(skill) not in resume_normalized:

            missing_skills.append(skill)

    return missing_skills