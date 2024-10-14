# login.py
import streamlit as st

st.title("Login Page")

with st.form(key='login_form'):
    Email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    col1, col2 = st.columns([3, 1])
    with col1:
            login_button = st.form_submit_button("Login")
    with col2:
            st.write("Don't have an account? [Register](/https://github.com/Johnsonndungu/Registration-loginpage/blob/main/Main.py)") 

# Add your login logic here, e.g., check credentials against a database
