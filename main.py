from fpdf import FPDF
import streamlit as st
import pandas as pd
from io import BytesIO
import datetime

st.title("Ramadan 2025 Timing Calendar Collector")

# User inputs the starting date of Ramadan
start_date = st.date_input("Enter the starting date of Ramadan (e.g., 2025-03-10):", datetime.date(2025, 3, 10))

# Collect Suhoor and Iftar times for 30 days
timings = []
for i in range(1, 31):
    suhoor = st.time_input(f"Suhoor Time (Day {i})", value=datetime.time(5, 0))
    iftar = st.time_input(f"Iftar Time (Day {i})", value=datetime.time(18, 0))
    timings.append({
        "Day": i,
        "Date": (start_date + datetime.timedelta(days=i - 1)).strftime("%Y-%m-%d"),
        "Suhoor": suhoor.strftime("%H:%M"),
        "Iftar": iftar.strftime("%H:%M")
    })

# Display collected timings as a DataFrame
st.write("### Collected Ramadan 2025 Timings")
df = pd.DataFrame(timings)
st.dataframe(df)

# Generate PDF if the button is clicked
if st.button("Generate PDF"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Ramadan 2025 Timing Calendar", ln=True, align='C')
    pdf.ln(10)

    # Add table headers
    pdf.cell(20, 10, "Day", 1)
    pdf.cell(40, 10, "Date", 1)
    pdf.cell(40, 10, "Suhoor", 1)
    pdf.cell(40, 10, "Iftar", 1)
    pdf.ln()

    # Add table data
    for timing in timings:
        pdf.cell(20, 10, str(timing["Day"]), 1)
        pdf.cell(40, 10, timing["Date"], 1)
        pdf.cell(40, 10, timing["Suhoor"], 1)
        pdf.cell(40, 10, timing["Iftar"], 1)
        pdf.ln()

    # Save PDF to a BytesIO object
    pdf_buffer = BytesIO()
    pdf.output(pdf_buffer)
    pdf_buffer.seek(0)

    # Download button for the PDF
    st.download_button(
        label="Download Ramadan 2025 Calendar PDF",
        data=pdf_buffer,
        file_name="ramadan_2025_calendar.pdf",
        mime="application/pdf"
    )
