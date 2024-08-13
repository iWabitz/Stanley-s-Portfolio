import streamlit as st
def quiz():

    st.header(":skull:. Simple Quiz")
    if ('current_question' not in st.session_state):
        st.session_state.current_question = 0
        
    if ('score' not in st.session_state):
        st.session_state.score = 0
        
    if ('quiz_complete' not in st.session_state):
        st.session_state.quiz_complete = False


    quiz_data = [
        {
            'question': "How do you create a button?", 
            'options': ['st.button', 'st.slider', 'st.createbutton', 'st.makebutton'],
            'correct_answer': 0
        },
        
        {
            'question': "How do you get input that is not a number", 
            'options': ['st.slider', 'st.text_input', 'st.button', 'st.Strinput'],
            'correct_answer': 1
        },
        
        {
            'question': "How do you get input that is a number", 
            'options': ['st.number', 'st.text_input', 'st.number_input', 'st.Intinput'],
            'correct_answer': 2
        },
        
        {
            'question': "How do you show your code?", 
            'options': ['st.code', 'st.show_code', 'st.codeshower', 'st.codeshow'],
            'correct_answer': 0
        }
        
        ]
    
    #Quiz Logic
    if not st.session_state.quiz_complete:
        question = quiz_data[st.session_state.current_question]
        st.write(f"Question {st.session_state.current_question+1} of {len(quiz_data)}")
        st.write(question['question'])

        answer = st.radio("Choose your answer", question['options'], key = (f"q{st.session_state.current_question}"))

        if st.button("Submit Answer"):
            if question['options'].index(answer) == question['correct_answer']:
                if st.button("Next"):
                    st.rerun()
                st.success("Correct!")
                st.session_state.score += 1
                
            else:
                st.error(f"Wrong. The correct answer was {question['options'][question['correct_answer']]}")

            if st.session_state.current_question < len(quiz_data) - 1:
                st.session_state.current_question += 1
                
            else:
                st.session_state.quiz_complete = True
            
    else:
        st.write(f"The quiz is complete")
        st.write(f"Your final score is {st.session_state.score} / {len(quiz_data)}")
        if st.session_state.score == len(quiz_data):
            st.balloons()
            st.write("CONGRATULATIONS, You got 100%")
        if st.button("Restart Quiz"):
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.quiz_complete = False
            st.rerun()
    st.sidebar.write('''
---------------------------------------
''')
    st.sidebar.write(f"Current Score: {st.session_state.score} / {len(quiz_data)}")
    st.sidebar.write('''
---------------------------------------
''')
    st.sidebar.write('''
This quiz app demonstrates the use of session_state in several ways:

1. Tracking the current question (st.session_state.current_question)
2. Keeping score (st.session_state.score)
3. Maintaining quiz state (st.session_state.quiz_complete)

These variables persist across reruns, allowing the quiz to maintain its state even when the user interacts with it.
''')
            
