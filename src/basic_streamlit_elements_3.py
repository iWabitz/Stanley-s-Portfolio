import streamlit as st
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
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/3/33/Patrick_Star.svg/220px-Patrick_Star.svg.png")
