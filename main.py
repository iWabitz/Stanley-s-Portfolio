#Intro to streamlit day 1
from src.landing_1 import introduction
from src.setup_2 import setup
from src.basic_streamlit_elements_3 import basic_elements
from src.interactive_app_4 import interactive_app
from src.run_app_5 import run_app
from src.hold_num_6 import hold_num
from src.hands_on_7 import hands_on
from src.wrap_up_8 import wrap_up
from src.to_do_9 import to_do
from src.quiz_10 import quiz
import streamlit as st

def main():
    st.title("Intro to streamlit lesson 1")
    st.subheader("Lesson plan for beginner python coders")

    #add a sidebar
    st.sidebar.title("Streamlit Masterclass")
    with st.sidebar.expander("Lesson Plans", expanded = False):
        streamlit_sections = [
        ":one:. Introduction",
        ":two:. Setup",
        ":atom_symbol:. Basic Streamlit Elements",
        ":four:. Simple Interactive App",
        ":running:. Running the App",
        ":five:. Capturing Variables",
        ":raised_hands:. Hands on activity",
        ":package:. Wrap up",
        ":nine:. To-Do List",
        ":skull:. Simple Quiz",
        
        ]

        selected_streamlit = st.radio("Go To", streamlit_sections)
    # main content
    if selected_streamlit:
        
        if selected_streamlit == ':one:. Introduction':
            introduction()
        elif selected_streamlit == ':two:. Setup':
            setup()
        elif selected_streamlit == ':atom_symbol:. Basic Streamlit Elements':
            basic_elements()
        elif selected_streamlit == ':four:. Simple Interactive App':
            interactive_app()
        elif selected_streamlit == ':running:. Running the App':
            run_app()
        elif selected_streamlit == ':five:. Capturing Variables':
            hold_num()
        elif selected_streamlit == ':raised_hands:. Hands on activity':
            hands_on()
        elif selected_streamlit == ':package:. Wrap up':
            wrap_up()
        elif selected_streamlit == ':nine:. To-Do List':
            to_do()
        elif selected_streamlit == ':skull:. Simple Quiz':
            quiz()
        
if __name__ == "__main__":
    main()
