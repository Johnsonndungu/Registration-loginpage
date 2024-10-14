import streamlit as st

st.title("Registration form")
with st.form(key='registration_form'):
        Firstname = st.text_input("Firstname")
        Lastname = st.text_input("Lastname")
        email = st.text_input("Email")
        phone_number = st.text_input("Phone number")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")  

        col1, col2 = st.columns([3, 1])
        with col1:
            submit_button = st.form_submit_button(label='Register')
        with col2:
            st.write("Have an account? [Login](/https://github.com/Johnsonndungu/Registration-loginpage/blob/main/Login.py") 

        if submit_button:
            if not Firstname or email or phone_number or password or confirm_password:
             st.error("Please fill in all fields")
            elif password != confirm_password:
                st.error("Passwords do not match!")
            else:
        # Here you would typically handle the registration logic, e.g.,
        #  - Store the user data in a database
        #  - Send a confirmation email
                st.success(f"Thank you for registering, {Firstname}!")
