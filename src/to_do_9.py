import streamlit as st
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
        
