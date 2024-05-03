import streamlit as st
import subprocess

def login():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "password":
            st.success("Logged in as {}".format(username))
            return True
        else:
            st.error("Invalid username or password")
            return False

def main():
    st.title("Real-time violence detection")

    # Check if user is logged in
    if 'is_logged_in' not in st.session_state:
        st.session_state.is_logged_in = False

    if not st.session_state.is_logged_in:
        if login():
            st.session_state.is_logged_in = True
            # Run app.py using subprocess and Streamlit's run command
            subprocess.Popen(["streamlit", "run", "app.py"])
            st.stop()  # Stop the current script execution after launching app.py

    else:
        st.write("You are logged in!")

if __name__ == "__main__":
    main()
