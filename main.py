import streamlit as st
import pandas as pd
from fpdf import FPDF
from io import BytesIO
from datetime import datetime, timedelta

st.set_page_config(page_title="Ramadan 2025 Calendar", layout="centered")

page = st.sidebar.radio("Navigate", ["Home", "Input Timings", "Show Calendar"])

if "start_date" not in st.session_state:
    st.session_state.start_date = datetime(2025, 3, 10)
if "suhoor_times" not in st.session_state:
    st.session_state.suhoor_times = ["05:00"] * 30
if "iftar_times" not in st.session_state:
    st.session_state.iftar_times = ["18:00"] * 30

if page == "Home":
    st.title("Welcome to Ramadan 2025 Timing Calendar Collector")
    st.write("A Ramadan calendar is a schedule that provides daily timings for Suhoor (pre-dawn meal) and Iftar (breaking fast at sunset) throughout the month of Ramadan. It typically covers 30 days, as the Islamic month follows the lunar calendar, which lasts 29 or 30 days depending on the moon sighting.")
    


elif page == "Input Timings":
    st.title("Input Ramadan 2025 Suhoor & Iftar Timings")

    st.session_state.start_date = st.date_input(
        "Enter the starting date of Ramadan 2025",
        st.session_state.start_date
    )

    st.write("### Enter Suhoor and Iftar Timings for 30 Days")
    for day in range(30):
        col1, col2 = st.columns(2)
        with col1:
            st.session_state.suhoor_times[day] = st.text_input(
                f"Suhoor Time (Day {day + 1})", value=st.session_state.suhoor_times[day], key=f"suhoor_{day}"
            )
        with col2:
            st.session_state.iftar_times[day] = st.text_input(
                f"Iftar Time (Day {day + 1})", value=st.session_state.iftar_times[day], key=f"iftar_{day}"
            )

elif page == "Show Calendar":
    st.title("Ramadan 2025 Calendar")

    dates = [(st.session_state.start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(30)]

    data = pd.DataFrame({
        'Day': [f"Day {i + 1}" for i in range(30)],
        'Date': dates,
        'Suhoor Time': st.session_state.suhoor_times,
        'Iftar Time': st.session_state.iftar_times
    })

    st.write("### Suhoor & Iftar Timings")
    st.dataframe(data)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Ramadan 2025 Suhoor & Iftar Timings", ln=True, align='C')
    pdf.ln(5)

    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(20, 10, txt="Day", border=1)
    pdf.cell(40, 10, txt="Date", border=1)
    pdf.cell(50, 10, txt="Suhoor Time", border=1)
    pdf.cell(50, 10, txt="Iftar Time", border=1)
    pdf.ln()

    pdf.set_font("Arial", size=12)
    for index, row in data.iterrows():
        pdf.cell(20, 10, txt=row['Day'], border=1)
        pdf.cell(40, 10, txt=row['Date'], border=1)
        pdf.cell(50, 10, txt=row['Suhoor Time'], border=1)
        pdf.cell(50, 10, txt=row['Iftar Time'], border=1)
        pdf.ln()

    
