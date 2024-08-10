import streamlit as st

st.title("My Streamlit")

st.title("_Streamlit_ is :blue[cool] :sunglasses:")

st.subheader('Subscribe')

st.caption("People who never listen, Always a person")

st.code('x = 15 + y')

st.latex(r''' e^{i\pi} + 1 = 0 ''')

st.subheader(":girl: :coffee:")

st.subheader(":ramen: :drooling_face:")

st.subheader(":soccer: :goal_net:")

st.subheader(":yawning_face: :bed:")

name = st.text_input('Enter your name')
st.write('Hello, ', name)

number = st.number_input('Insert a number')
st.write('The number is ', number)

st.title("The Wonders of the Ocean")

st.write("The ocean is a vast and mysterious place that covers about 71% of the Earth's surface. It's home to a wide variety of life forms, from the tiniest plankton to the largest whale. The ocean's depths are still largely unexplored, and scientists believe there are many species yet to be discovered. The sheer size and complexity of the ocean make it one of the most fascinating parts of our planet.")
         
