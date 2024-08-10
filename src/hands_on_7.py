import streamlit as st
def hands_on():
    st.header(":raised_hands:. Hands on activity")
    st.write("Now it's your turn to create something awesome!")
    st.code('''
import streamlit as st
import random

st.title("Guess the Number Game")

#Generate a random number between 1 and 100

if 'secret_number' not in st.session_state:
    st.session_state['secret_number'] = random.randint(1, 100)

secret_number = st.session_state['secret_number']

#Get the player's guess

guess = st.number_input("Choose a number between 1 and 100", min_value=1, max_value=100)

if st.button("Check my guess"):
    if secret_number == guess:
        st.balloons()
        result = "You guessed the correct number! GREAT JOB!"
    else:
        hint1 = max(secret_number - 20, 1)
        hint2 = min(secret_number + 20, 100)
        result = f"You are close, here's a hint: The number is between {hint1} and {hint2}."

    st.write(result)
   ''') 
