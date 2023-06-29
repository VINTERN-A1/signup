import streamlit as st
from github import Github
import uuid

# GitHub credentials
ACCESS_TOKEN = "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"
REPO_NAME = "dat"

# Initialize the GitHub object with the access token
g = Github(ACCESS_TOKEN)
repo = g.get_user().get_repo(REPO_NAME)

placeholder = st.empty()
email = st.text_input("Email", autocomplete=None)
st.markdown(" ")
name = st.text_input("User name", autocomplete=None)
st.markdown(" ")
password = st.text_input("Password", autocomplete=None)
if st.button("Sign Up", key="option_tab2"):
    # Generate a random file name
    file_name = str(uuid.uuid4()) + ".txt"

    # Create the text to be written to the file
    file_contents = f"email: {email}\n"
    file_contents += f"name: {name}\n"
    file_contents += f"password: {password}\n"

    # Upload the file to GitHub
    repo.create_file(file_name, "Committing form data", file_contents)

    # Display a success message
    st.success("Successfully Registered")
    placeholder = st.empty()
