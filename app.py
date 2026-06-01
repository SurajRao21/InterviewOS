import streamlit as st
from utils.parser import extract_text_from_pdf
from agents.candidate_agent import analyze_resume

st.set_page_config(
    page_title="InterviewOS",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 InterviewOS")

st.subheader(
    "AI-Powered Personalized Interview Preparation Operating System"
)

st.divider()

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

job_description = st.file_uploader(
    "Upload Job Description",
    type=["pdf", "txt"]
)

if resume:
    st.success(f"Resume Uploaded: {resume.name}")

    resume_text = extract_text_from_pdf(resume)

    st.subheader("Resume Text Preview")

    st.text_area(
        "Extracted Resume Text",
        resume_text[:5000],
        height=300
    )

    if st.button("Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            analysis = analyze_resume(
                resume_text
            )

            st.subheader(
                "Candidate Intelligence Report"
            )

            st.code(
                analysis,
                language="json"
            )

if job_description:
    st.success(
        f"Job Description Uploaded: {job_description.name}"
    )