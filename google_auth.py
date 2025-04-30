import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import streamlit as st

def get_gsheet(sheet_name):
    """
    Helper function to access specified Google Sheet
    """
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    #creds_dict = st.secrets["GOOGLE_CREDENTIALS"]
    creds_dict = json.loads(st.secrets["google_credentials"]["GOOGLE_CREDENTIALS"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
    return client.open(sheet_name).sheet1