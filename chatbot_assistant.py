import streamlit as st
import openai
import time


ASSISTANT_MODES = {
    'Beginner': '''You are a patient tutor explaining streamlit basics to beginnners and also, make sure to follow these exact rules
                    1. Do not give me the entire code all at once, but instead please provid in instructional bullet points
                    2. Assume the personality of Luffy from One Piece.
                ''',
    'Advanced': '''You are an expert streamlit developer giving feedback on Streamlit code snippet''',


    'Code Review': '''You are a code reviewer working at Google and have the most award given by this tech giant for best code review.
                    1. You are patient and knowledgable
                    2. You only give information that will help me become a better programmer.
                    3. Assume the personality of Mark Zuckerberg and please provide responses exactly the way he would say it.
                   '''
    
    
}

# Replace these with your own Assistant ID and Thread ID
ASSISTANT_ID = 'asst_hTTJeHzpw4fUzn6jM71RFaKd'
THREAD_ID = 'thread_nTltQvucdOmsK3A9sPGPP8MN'

def streamlit_assistant():
    st.title('Streamlit Multi-Mode Assistant')
    mode = st.selectbox('Please select a character', list(ASSISTANT_MODES.keys()))
    st.write(f"Your current mode is {mode}")
    
    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = {mode: [] for mode in ASSISTANT_MODES}
    
    #Display chat messages from history on app rerun
    for message in st.session_state.messages[mode]:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

    if prompt := st.chat_input(f"Ask the {mode} Assistant abbout Streamlit."):
        st.session_state.messages[mode].append({'role': 'user', 'content': prompt})
        with st.chat_message('user'):
            st.markdown(prompt)
        if 'openai_api_key' in st.session_state and st.session_state.openai_api_key:
            client = openai.OpenAI(api_key=st.session_state.openai_api_key)
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = get_assistant_response(client, prompt, mode)
                message_placeholder.markdown(full_response)
                st.session_state.messages[mode].append({"role": "assistant", "content": full_response})
def wait_for_run_complete(client, thread_id, run_id):
    while True:
        run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
        if run.completed_at:
            return run.status
        time.sleep(1)

def get_assistant_response(client, user_input, mode):
    # Add the user's message to the thread
    client.beta.threads.messages.create(
        thread_id=THREAD_ID,
        role='user',
        content=user_input
    )
    # Create a run
    run = client.beta.threads.runs.create(
        thread_id=THREAD_ID,
        assistant_id=ASSISTANT_ID
    )
    # Wait for the run to complete
    wait_for_run_complete(client, THREAD_ID, run.id)
    # Retrieve the assistant's messages
    messages = client.beta.threads.messages.list(thread_id=THREAD_ID)

    # Return the latest assistant message
    return messages.data[0].content[0].text.value



def main():
    
    # Streamlit page config
    st.set_page_config(page_title="My AI Chatbot", page_icon="🤖", layout="wide")

    # Sidebar for API key input
    st.sidebar.title("Setup")
    api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

    if api_key:
        st.session_state.openai_api_key=api_key

    streamlit_assistant()
if __name__=='__main__':
    main()

