#Intro to streamlit day 1
from src.landing_1 import introduction
from src.setup_2 import setup
import streamlit as st
def main():
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
    ":five:. Capturing Variables",
    ":raised_hands:. Hands on activity",
    ":package:. Wrap up",
    ":nine:. To-Do List",
    ":skull:. Simple Quiz",
    
    ]


    selected_section = st.sidebar.radio("Go To", sections)
    # main content
    if selected_section == ':one:. Introduction':
        introduction()
    elif selected_section == ':two:. Setup':
        setup()
    elif selected_section == ':atom_symbol:. Basic Streamlit Elements':
        basic_elements()
    elif selected_section == ':four:. Simple Interactive App':
        interactive_app()
    elif selected_section == ':running:. Running the App':
        run_app()
    elif selected_section == ':five:. Capturing Variables':
        hold_num()
    elif selected_section == ':raised_hands:. Hands on activity':
        hands_on()
    elif selected_section == ':package:. Wrap up':
        wrap_up()
    elif selected_section == ':nine:. To-Do List':
        to_do()
    elif selected_section == ':skull:. Simple Quiz':
        quiz()
    

def basic_elements():
    st.header(":atom_symbol:. Basic Streamlit Elements")
    st.write("Let's explore some basic streamlit elements:")
    st.subheader("3.1 Text Elements")
    st.write("Here are some examples of text elements:")
    st.code('''
st.title("Example 1")
st.write("Example 2")
st.subheader("Example 3")
st.markdown("Example 4")
st.caption("Example 5")

''')
    st.subheader("3.2 Input Elements")
    st.write("Streamlit provides various input elements:")
    username = st.text_input("Enter your username ")
    age = st.slider("Select your age ", 1, 100)
    st.write(f"Hello {username}, you are {age} years old.")
    st.subheader("3.3 Display Image")
    st.write("You can display images like this:")
    st.image("https://media.discordapp.net/attachments/1238937989200089169/1258999930165526528/image.png?ex=66969cce&is=66954b4e&hm=0b8de778a231a19b0b24a188ae3cbb201f41028dfbcfd37482af0f68f27a5a86&=&format=webp&quality=lossless&width=396&height=622")

def interactive_app():
    st.header(":four:. Simple Interactive App")
    st.write("Let's create a basic calculator: ")
    num1 = st.number_input("Please enter your first number ", value = 0)
    num2 = st.number_input("Please enter your second number ", value = 0)
    operation = st.selectbox("Choose your operation ", ['*', '/', '+', '-'])
    if st.button("FIND YOUR ANSWER"):
        
        if operation == '*':
            result = num1*num2
            
        elif operation == '/':
            if num2 == 0:
                result = "You can't divide a number by 0!"
            else:
                result = num1/num2
                
            
        elif operation == '+':
            result = num1+num2
            
        else:
            result = num1-num2 
        st.write(result)

def run_app():
    st.header(":running:. Running the App")
    st.write("Run your streamlit app: ")
    st.write("- Make sure you are in the right directory using `cd`")
    st.code("streamlit run your_app_name.py")
    st.write("Make sure you are in the correct directory in your terminal or command prompt.")
def hold_num():
    st.header(":five:. Capturing Variables")
    st.write("Session State is a way to share variables between reruns, for each user session. For example, when you are creating a mini-game it prevents the number from changing every time you click the button")

    st.subheader("Initialize values in Session State")
    st.write("The Session State API is very similar to Python dictionaries:")
    st.code('''
#Initialization
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Session State also supports attribute based syntax
if 'key' not in st.session_state:
    st.session_state.key = 'value'
    ''')

    st.subheader("Delete items")
    st.write("Delete items in Session State:")
    st.code('''
# Delete a single key-value pair
del st.session_state[key]

# Delete all the items in Session state
for key in st.session_state.keys():
    del st.session_state[key]
    
''')
    st.subheader("Session State and Widget State association")
    st.write("When there is a widget there will also be a session state")
    st.code('''
st.text_input("Your name", key="name")
''')
    
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
def to_do():
    st.header(":nine:. To-Do List")
    st.write("Let's make a To-Do list!")
    todo = st.text_input("Please enter a todo item ")
    if 'todos' not in st.session_state:
        st.session_state.todos = []
        #Create a text input
        
    if st.button("Add"):
        st.session_state.todos.append(todo)
    st.title("To-do List")
    for i, todo in enumerate(st.session_state.todos):
        st.write(f" {i+1}. {todo}")
        
def wrap_up():
    st.header(":package:. Wrap up")
    st.write("Great job! You've learned the basics of streamlit.")
    st.write("Remember you can make amazing web apps with just a few lines of Python code.")
    st.write("Keep Exploring and have fun coding!")


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
            
if __name__ == "__main__":
    main()
