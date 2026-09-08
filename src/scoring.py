def calculate_resume_score(resume_text, skills, analysis):
    """
    Calculate overall resume score.
    """

    score = 0

    # Skills score
    if len(skills) >= 10:
        score += 30
    elif len(skills) >= 5:
        score += 20
    elif len(skills) >= 2:
        score += 10

    # Contact information
    if analysis.get("email") != "Not Found":
        score += 10

    if analysis.get("phone") != "Not Found":
        score += 10

    # Professional summary
    if analysis.get("summary") != "Not Found":
        score += 15

    # Education
    if analysis.get("education") != "Not Found":
        score += 15

    # Experience
    if analysis.get("experience") != "Not Found":
        score += 20

    return min(score, 100)