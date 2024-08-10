import streamlit as st
def run_app():
    st.header(":running:. Running the App")
    st.write("Run your streamlit app: ")
    st.write("- Make sure you are in the right directory using `cd`")
    st.code("streamlit run your_app_name.py")
    st.write("Make sure you are in the correct directory in your terminal or command prompt.")
