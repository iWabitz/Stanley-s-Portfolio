# chatbot_assistant.py
import streamlit as st
import openai
import time

st.set_page_config(page_title='My AI Chatbot', page_icon='', layout = 'wide')

st.sidebar.title('Setup')
api_key = st.sidebar.text_input('Enter your OpenAI API Key', type = 'password')

st.title('My AI Chatbot')

if 'messages' not in st.session_state:
    st.session_state.messages = []

ASSISTANT_ID = 'asst_Xa0BP7rwsCQUmWLvsezrArgp'
THREAD_ID = 'thread_xqGZd1gfF4vAityThrBXkhKC'

def wait_for_run_complete(client, thread_id, run_id):
    while True:
        run = client.beta.threads.run.retrieve(thread_id = thread_id, run_id = run_id)
        if run.completed_st:
            return run.status
        time.sleep(1)

def get_assistant_response(client, user_input):
    client.beta.threads.messages.create(
        thread_id=THREAD_ID,
        role ='user',
        content=user_input
    )


    run = client.beta.threads.runs.create(
        thread_id = THREAD_ID,
        assistant_id=ASSISTANT_ID
    )

    wait_for_run_complete(client, THREAD_ID, run.id)
    messages = client.beta.threads.messages.list(thread_id=THREAD_ID)

    return messages.data[0].content[0].text.value

for messages in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

#Chat Input
if api_key:
    client = openai.OpenAI(api_key=api_key)

    prompt = st.chat_input('Ask me anything!')

    if prompt:
        st.session_state.messages.append({'role': 'user', 'content': prompt})

        with st.chat_message('user'):
            st.markdown(prompt)

        with st.chat_message('assistant'):
            message_placeholder = st.empty()
            full_response = get_assistant_response(client, prompt)
            message_placeholder.markdown(full_response)

        st.session_state.messages.append({'role': 'assistant', 'content': full_response})

else:
    st.warning('Please enter your OpenAI API Key in the sidebar to start the chat!')
            
