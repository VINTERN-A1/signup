
import streamlit as st
from github import Github
import uuid


#import streamlit as st
# GitHub credentials
ACCESS_TOKEN = "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"
REPO_NAME = "repo"

# Initialize the GitHub object with access token
g = Github(ACCESS_TOKEN)
repo = g.get_user().get_repo(REPO_NAME)

placeholder = st.empty()
email = st.text_input("Email",autocomplete = None)
st.markdown(" ")
name=st.text_input("User name",autocomplete = None) 
st.markdown(" ")
password = st.text_input("Password",autocomplete = None)  
if st.button("Sign Up",key="option_tab2"): 
    # Generate a random file name
    file_name = str("signup")+str(uuid.uuid4())+ ".txt"
    # Create the text to be written to the file
    file_contents = f"email: {email}\n"
    file_contents1= f"name: {name}\n"
    file_contents2= f"password:{password}\n"
            
    # Write the file to disk
    with open(file_name, "w") as f:
        f.write(file_contents)
        f.write(file_contents1)
        f.write(file_contents2)
            
    # Upload the file to GitHub
    with open(file_name, "r") as f:
        contents = f.read()
    repo.create_file(file_name, "Committing form data", contents)
            
    # Display a success message
    st.success("Succesfully Registered")
    placeholder = st.empty()
