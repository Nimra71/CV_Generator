# app.py
import streamlit as st
from utils import generate_cv_pdf

st.set_page_config(page_title="Professional CV Generator", layout="centered")

st.title("🖤 Minimal Black & White CV Generator")
st.write("Enter your details below and download a professional CV.")

# -------- USER INPUT --------
name = st.text_input("Full Name")
contact = st.text_input("Contact (Email | Phone | LinkedIn)")

education = st.text_area("Education (one per line)").split("\n")
experience = st.text_area("Experience (one per line)").split("\n")
projects = st.text_area("Projects (one per line)").split("\n")
skills = st.text_area("Skills (comma separated)").split(",")
certificates = st.text_area("Certificates (one per line)").split("\n")

# -------- GENERATE CV --------
if st.button("Generate CV"):
    if not name or not contact:
        st.error("Please fill in at least Name and Contact.")
    else:
        user_data = {
            "name": name,
            "contact": contact,
            "education": education,
            "experience": experience,
            "projects": projects,
            "skills": skills,
            "certificates": certificates
        }

        pdf_path = generate_cv_pdf(user_data)

        with open(pdf_path, "rb") as f:
            st.download_button(
                label="⬇️ Download Your CV (PDF)",
                data=f,
                file_name="Professional_CV.pdf",
                mime="application/pdf"
            )

        st.success("Your CV is ready!")
