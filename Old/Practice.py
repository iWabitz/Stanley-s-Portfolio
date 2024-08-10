import streamlit as st

st.markdown('''
<style>
.red-text {
    color: red;
    font-size: 24px;
}
.stButton> button {
    height: 50px;
    padding: 50px;
    color: red;
}
.stApp{
    background-color: blue;
}
</style>
''', unsafe_allow_html=True)

st.markdown('<p class="red-text">It is very sunny!</p>', unsafe_allow_html=True)

st.button("Click me!")
