import streamlit as st
from github import Github
import uuid

# GitHub credentials
ACCESS_TOKEN = "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"
REPO_OWNER = "VINTERN-A1"
REPO_NAME = "repo"

# Initialize the GitHub object with the access token
g = Github(ACCESS_TOKEN)
repo = g.get_repo(f"{REPO_OWNER}/{REPO_NAME}")

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
