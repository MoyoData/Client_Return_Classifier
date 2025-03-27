import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# For public sheet (no authentication needed)
def get_public_sheet_data(sheet_id, sheet_name):
    url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
    df = pd.read_csv(url)
    return df

# Your sheet details
SHEET_ID = '1sBwwxi_LRKmzdJxz68W3fSClJVdwmTJ2UUJXylIgTbo'  # Replace with your sheet ID
SHEET_NAME = 'Streamlit_Goolesheet'  # Replace with your sheet name

# Load data
df = get_public_sheet_data(SHEET_ID, SHEET_NAME)

# Display in Streamlit
st.title("Google Sheet Data in Streamlit")
st.write(df)
