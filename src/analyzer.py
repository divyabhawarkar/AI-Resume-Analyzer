import re


def extract_name(resume_text):
    """
    Extract candidate name from the resume.
    """

    lines = [
        line.strip()
        for line in resume_text.splitlines()
        if line.strip()
    ]

    if lines:
        return lines[0]

    return "Not Found"


def extract_email(resume_text):
    """
    Extract email address.
    """

    pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

    match = re.search(pattern, resume_text)

    if match:
        return match.group()

    return "Not Found"


def extract_phone(resume_text):
    """
    Extract Indian phone number.
    """

    pattern = r'(\+91[\s-]?)?[6-9]\d{9}'

    match = re.search(pattern, resume_text)

    if match:
        return match.group()

    return "Not Found"


def extract_section(resume_text, headings):
    """
    Extract content belonging to a resume section.

    headings = possible names of the section
    """

    lines = resume_text.splitlines()

    start_index = -1

    # Find section heading
    for i, line in enumerate(lines):

        clean_line = line.strip().lower()

        for heading in headings:

            if heading.lower() in clean_line:
                start_index = i
                break

        if start_index != -1:
            break

    if start_index == -1:
        return "Not Found"

    section_lines = []

    # Common headings that indicate next section
    next_sections = [
        "professional summary",
        "career objective",
        "objective",
        "summary",
        "education",
        "academic qualification",
        "work experience",
        "experience",
        "internship",
        "training",
        "skills",
        "technical skills",
        "skills & strengths",
        "certifications",
        "projects",
        "project work",
        "languages",
        "achievements",
        "volunteer experience",
        "additional information"
    ]

    for line in lines[start_index + 1:]:

        clean_line = line.strip().lower()

        # Check if another section has started
        is_next_section = False

        for section in next_sections:

            if clean_line == section:
                is_next_section = True
                break

        if is_next_section:
            break

        if line.strip():
            section_lines.append(line.strip())

    if section_lines:
        return " ".join(section_lines)

    return "Not Found"


def analyze_resume(resume_text):
    """
    Analyze important resume information.
    """

    analysis = {}

    analysis["name"] = extract_name(resume_text)

    analysis["email"] = extract_email(resume_text)

    analysis["phone"] = extract_phone(resume_text)

    # Professional Summary
    analysis["summary"] = extract_section(
        resume_text,
        [
            "PROFESSIONAL SUMMARY",
            "CAREER OBJECTIVE",
            "OBJECTIVE",
            "SUMMARY"
        ]
    )

    # Education
    analysis["education"] = extract_section(
        resume_text,
        [
            "EDUCATION",
            "ACADEMIC QUALIFICATION",
            "EDUCATIONAL QUALIFICATION"
        ]
    )

    # Experience / Internship / Training
    analysis["experience"] = extract_section(
        resume_text,
        [
            "WORK EXPERIENCE",
            "WORK EXPERIENCE & INTERNSHIP",
            "EXPERIENCE",
            "INTERNSHIP",
            "TRAINING",
            "TRAINING / INTERNSHIP EXPERIENCE"
        ]
    )

    return analysis