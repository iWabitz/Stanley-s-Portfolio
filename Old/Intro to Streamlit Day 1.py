#Intro to streamlit day 1
import streamlit as st
st.title("Intro to streamlit lesson 1")
st.subheader("Lesson plan for beginner python coders")

#add a sidebar
st.sidebar.title("lesson section")

sections = [
":one:. Introduction",
":two:. Setup",
":atom_symbol:. Basic Streamlit Elements",
":four:. Simple Interactive App",
":running:. Running the App",
":raised_hands:. Hands on activity",
":package:. Wrap up",
]


selected_section = st.sidebar.radio("Go To", sections)
