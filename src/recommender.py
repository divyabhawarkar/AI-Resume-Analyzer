import pandas as pd


# ---------------------------------------
# Career Dataset
# ---------------------------------------

CAREER_FILE = "data/careers.csv"


# ---------------------------------------
# Skill Normalization
# ---------------------------------------

SKILL_ALIASES = {
    "good manufacturing practices": "gmp",
    "quality management systems": "qms",
    "quality control microbiology": "microbiology",
    "microsoft excel": "excel",
    "microsoft word": "word",
    "microsoft powerpoint": "powerpoint",
    "novel drug delivery systems": "drug delivery",
}


def normalize_skill(skill):
    """Normalize skill names."""

    skill = str(skill).lower().strip()

    return SKILL_ALIASES.get(skill, skill)


# ---------------------------------------
# Load Career Data
# ---------------------------------------

def load_career_data():
    """Load career dataset."""

    return pd.read_csv(CAREER_FILE)


# ---------------------------------------
# Career Recommendation
# ---------------------------------------

def recommend_careers(resume_skills, top_n=5):
    """
    Recommend careers using skill matching.
    """

    df = load_career_data()

    resume_skills_normalized = {
        normalize_skill(skill)
        for skill in resume_skills
    }

    recommendations = []

    for _, row in df.iterrows():

        career = row["Career"]

        required_skills = [
            skill.strip()
            for skill in str(row["Required Skills"]).split("|")
            if skill.strip()
        ]

        required_skills_normalized = [
            normalize_skill(skill)
            for skill in required_skills
        ]

        matched_skills = []

        for original_skill, normalized_skill in zip(
            required_skills,
            required_skills_normalized
        ):

            if normalized_skill in resume_skills_normalized:

                matched_skills.append(original_skill)

        # ---------------------------------------
        # Match Percentage
        # ---------------------------------------

        total_required = len(required_skills_normalized)

        total_matched = len(matched_skills)

        if total_required > 0:

            match_percentage = (
                total_matched / total_required
            ) * 100

        else:

            match_percentage = 0

        recommendations.append({

            "Career": career,

            "Match": round(
                match_percentage,
                2
            ),

            "Matched Skills": matched_skills,

            "Missing Skills": [
                skill
                for skill in required_skills
                if skill not in matched_skills
            ]

        })

    # ---------------------------------------
    # Sort by highest match
    # ---------------------------------------

    recommendations.sort(
        key=lambda x: x["Match"],
        reverse=True
    )

    return recommendations[:top_n]