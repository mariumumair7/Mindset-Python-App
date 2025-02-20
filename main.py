import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title="PIAIC", layout="wide")

st.title("PIAIC - Presidential Initiative for Artificial Intelligence and Computing")

st.write("Welcome to the PIAIC Information Hub. This is a simple app built with Streamlit to provide details about PIAIC and its programs.")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Programs", "Admissions", "Contact"])

if page == "Home":
    st.header("Home Page")
    st.write("Welcome to the Home Page of PIAIC. The Presidential Initiative for Artificial Intelligence and Computing is an educational program aiming to develop a skilled workforce in emerging technologies like Artificial Intelligence, Cloud Computing, Blockchain, and the Internet of Things (IoT).")

elif page == "Programs":
    st.header("Our Programs")
    st.write("PIAIC offers the following specialized programs:")
    st.markdown("- Artificial Intelligence (AI)")
    st.markdown("- Cloud Native Computing")
    st.markdown("- Blockchain")
    st.markdown("- Internet of Things (IoT)")

elif page == "Admissions":
    st.header("Admissions")
    st.write("Admissions are open throughout the year. You can apply online through the official PIAIC website.")
    st.write("Visit [PIAIC Admissions](https://www.piaic.org/) for more details.")
    uploaded_files = st.file_uploader("Upload your form in PDF:", type=("pdf",), accept_multiple_files=True)
    if uploaded_files:
        for uploaded_file in uploaded_files:
            st.write(f"Uploaded file: {uploaded_file.name}")

elif page == "Contact":
    st.header("Contact Us")
    st.write("For more information, reach out to us at: info@piaic.org")
    st.write("Follow us on social media:")
    st.write("- Twitter: @piaicofficial")
    st.write("- Facebook: PIAIC")
    st.write("- LinkedIn: PIAIC")
