import streamlit as st

if 'todos' not in st.session_state:
    st.session_state.todos = []

#Create a text input
todo = st.text_input("Please enter a todo item ")
if st.button("Add"):
    st.session_state.todos.append(todo)
st.title("To-do List")
for i, todo in enumerate(st.session_state.todos):
    st.write(f" {i+1}. {todo}")
    st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")


        
