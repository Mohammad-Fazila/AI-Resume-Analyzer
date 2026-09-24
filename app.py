import streamlit as st
from pypdf import PdfReader

# Page title
st.title("🤖 AI Resume Analyzer")

st.write("Upload your resume and analyze your skills.")

# Resume upload
uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

# Skills we want to check
skills = [
    "Python",
    "Java",
    "C++",
    "SQL",
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "Data Analysis",
    "Excel",
    "Power BI",
    "Tableau",
    "HTML",
    "CSS",
    "JavaScript"
]

if uploaded_file is not None:

    st.success("Resume uploaded successfully! ✅")

    # Read PDF
    reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text

    # Display extracted text
    st.subheader("📄 Resume Text")

    st.write(resume_text)

    # Find skills
    st.subheader("🔍 Skills Found")

    found_skills = []

    for skill in skills:
        if skill.lower() in resume_text.lower():
            found_skills.append(skill)

    if found_skills:
        for skill in found_skills:
            st.success("✅ " + skill)
    else:
        st.warning("No matching skills found.")

    # Suggestions
    if len(found_skills) < 5:
        st.info("Try adding more relevant technical skills to your resume.")

    if "Python" not in found_skills:
        st.info("Consider mentioning Python if you have learned it.")

    if "SQL" not in found_skills:
        st.info("Consider mentioning SQL if you have learned it.")

    if len(found_skills) >= 5:
        st.success("Your resume contains several technical skills! 🎉")