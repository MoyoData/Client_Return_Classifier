import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# --- Google Sheets Connection ---
@st.cache_resource
def connect_to_gsheet():
    # Authenticate with Google Sheets
    scope = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
    return gspread.authorize(creds)

def get_sheet_data(sheet_id, sheet_name):
    gc = connect_to_gsheet()
    worksheet = gc.open_by_key(sheet_id).worksheet(sheet_name)
    return worksheet.get_all_records()

# --- Streamlit App ---
st.title("Google Sheets Data Viewer")

# Load data
SHEET_ID = "1sBwwxi_LRKmzdJxz68W3fSClJVdwmTJ2UUJXylIgTbo"  # From URL: docs.google.com/spreadsheets/d/[THIS_IS_YOUR_SHEET_ID]/edit
SHEET_NAME = "Streamlit_Goolesheet"

df = pd.DataFrame(get_sheet_data(SHEET_ID, SHEET_NAME))
st.dataframe(df)

# Add new data example
with st.form("Add row"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    if st.form_submit_button("Submit"):
        gc = connect_to_gsheet()
        worksheet = gc.open_by_key(SHEET_ID).worksheet(SHEET_NAME)
        worksheet.append_row([name, email])
        st.success("Data added!")
