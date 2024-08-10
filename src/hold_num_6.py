import streamlit as st
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
    
