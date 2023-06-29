import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets credentials
SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
CREDS_FILE = 'credentials.json'
SPREADSHEET_ID = '1R9-wMUkE0H8jOy9nO4fjGdeDDez9Vrv2TNrHuVVLe7A'

# Authenticate with Google Sheets API
creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_FILE, SCOPE)
client = gspread.authorize(creds)
sheet = client.open_by_key(SPREADSHEET_ID).sheet1

def registration_form():
    st.header('Registration Form')

    # Input fields
    placeholder = st.empty()
    email = st.text_input('Email',autocomplete = None)
    name = st.text_input('Username',autocomplete = None)
    password = st.text_input('Password', type='password')

    # Submit button
    if st.button('Register'):
        # Write the form data to the Google Sheets spreadsheet
        sheet.append_row([email, name, password])
        st.success('Registration successful!')

# Run the Streamlit app
if __name__ == '__main__':
    registration_form()
