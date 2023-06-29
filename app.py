
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


import streamlit as st
from github import Github

# GitHub credentials
github_username = 'vintern-a1'
github_token = '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'

# GitHub repository info
repo_owner = 'vintern-a1'
repo_name = 'repo'

# Create a new issue in the GitHub repository
def create_github_issue(text):
    try:
        g = Github(github_token)
        repo = g.get_repo(f'{repo_owner}/{repo_name}')
        issue = repo.create_issue(title='Streamlit Form Submission', body=text)
        return issue
    except Exception as e:
        st.error(f'Error creating GitHub issue: {e}')

# Streamlit form
def streamlit_form():
    st.header('GitHub Repository Text Dump')
    text = st.text_area('Enter the text you want to dump to GitHub')

    if st.button('Submit'):
        issue = create_github_issue(text)
        if issue:
            st.success('Text dumped to GitHub successfully!')
        else:
            st.error('Failed to dump text to GitHub.')

# Run the Streamlit app
if __name__ == '__main__':
    streamlit_form()
