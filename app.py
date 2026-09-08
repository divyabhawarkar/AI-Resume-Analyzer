import streamlit as st

from src.parser import extract_resume_text
from src.skills import extract_skills
from src.analyzer import analyze_resume
from src.recommender import recommend_careers
from src.scoring import calculate_resume_score
from src.skill_gap import get_skill_gap, get_matching_skills


# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# -------------------------------
# Main Title
# -------------------------------

st.title("📄 AI Resume Analyzer & Career Recommendation System")

st.write(
    "Upload your resume to extract information, "
    "analyze skills, calculate resume score, "
    "and get career recommendations."
)


# -------------------------------
# Resume Upload
# -------------------------------

uploaded_file = st.file_uploader(
    "📤 Upload your Resume",
    type=["pdf", "docx"]
)


# -------------------------------
# Resume Processing
# -------------------------------

if uploaded_file is not None:

    st.success(
        f"Resume uploaded successfully: {uploaded_file.name}"
    )

    if st.button("🔍 Analyze Resume"):

        with st.spinner("Analyzing your resume..."):

            resume_text = extract_resume_text(uploaded_file)

        if resume_text:

            # -------------------------------
            # Analyze Resume
            # -------------------------------

            analysis = analyze_resume(resume_text)

            # -------------------------------
            # Candidate Information
            # -------------------------------

            st.header("👤 Candidate Information")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.write("**Name**")
                st.info(analysis["name"])

            with col2:
                st.write("**Email**")
                st.info(analysis["email"])

            with col3:
                st.write("**Phone**")
                st.info(analysis["phone"])

            # -------------------------------
            # Professional Summary
            # -------------------------------

            st.header("📝 Professional Summary")

            st.write(analysis["summary"])

            # -------------------------------
            # Skills
            # -------------------------------

            skills = extract_skills(resume_text)

            st.header("🛠️ Skills Detected")

            if skills:

                st.success(
                    f"Found {len(skills)} skills in your resume."
                )

                for skill in skills:
                    st.write(f"✓ {skill}")

            else:

                st.warning(
                    "No technical or professional skills were detected."
                )

            # -------------------------------
            # Resume Score
            # -------------------------------

            resume_score = calculate_resume_score(
                resume_text,
                skills,
                analysis
            )

            st.header("📊 Resume Score")

            st.progress(resume_score)

            st.write(
                f"### Overall Resume Score: {resume_score}/100"
            )

            if resume_score >= 80:

                st.success("Excellent Resume! 🎉")

            elif resume_score >= 60:

                st.info("Good Resume 👍")

            elif resume_score >= 40:

                st.warning(
                    "Resume needs some improvement."
                )

            else:

                st.error(
                    "Resume needs significant improvement."
                )

            # -------------------------------
            # Career Recommendations
            # -------------------------------

            st.header("🎯 Career Recommendations")

            recommendations = recommend_careers(skills)

            if recommendations:

                for index, recommendation in enumerate(
                    recommendations,
                    start=1
                ):

                    career = recommendation["Career"]
                    match = recommendation["Match"]

                    st.subheader(
                        f"{index}. {career}"
                    )

                    st.progress(int(match))

                    st.write(
                        f"Match Score: **{match}%**"
                    )

                    if recommendation["Matched Skills"]:

                        st.write(
                            "Matched Skills:",
                            ", ".join(
                                recommendation["Matched Skills"]
                            )
                        )

                    else:

                        st.write(
                            "Matched Skills: None"
                        )

            else:

                st.warning(
                    "No suitable career found."
                )

            # -------------------------------
            # Skill Gap Analysis
            # -------------------------------

            st.header("📚 Skill Gap Analysis")

            if recommendations:

                top_career = recommendations[0]["Career"]

                st.subheader(
                    f"🎯 Recommended Career: {top_career}"
                )

                matching_skills = get_matching_skills(
                    skills,
                    top_career
                )

                missing_skills = get_skill_gap(
                    skills,
                    top_career
                )

                if matching_skills:

                    st.write(
                        "### ✅ Your Matching Skills"
                    )

                    for skill in matching_skills:

                        st.write(
                            f"✓ {skill}"
                        )

                else:

                    st.write(
                        "No matching skills found."
                    )

                if missing_skills:

                    st.write(
                        "### ⚠️ Skills You Should Learn"
                    )

                    for skill in missing_skills:

                        st.write(
                            f"• {skill}"
                        )

                else:

                    st.success(
                        "🎉 You already have the important "
                        "skills for this career!"
                    )

            # -------------------------------
            # Education
            # -------------------------------

            st.header("🎓 Education")

            st.write(
                analysis["education"]
            )

            # -------------------------------
            # Experience
            # -------------------------------

            st.header(
                "💼 Training / Internship Experience"
            )

            st.write(
                analysis["experience"]
            )

            # -------------------------------
            # Extracted Text
            # -------------------------------

            with st.expander(
                "📄 View Extracted Resume Text"
            ):

                st.text_area(
                    "Resume Content",
                    resume_text,
                    height=400
                )

        else:

            st.error(
                "Sorry, text could not be extracted from this file."
            )