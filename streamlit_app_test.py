import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Authenticate
@st.cache_resource
def connect_to_gsheet():
    scope = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
    return gspread.authorize(creds)

# Usage
gc = connect_to_gsheet()
sheet = gc.open_by_key("1sBwwxi_LRKmzdJxz68W3fSClJVdwmTJ2UUJXylIgTbo")  # From sheet URL
worksheet = sheet.sheet1
data = worksheet.get_all_records()
st.dataframe(data)
