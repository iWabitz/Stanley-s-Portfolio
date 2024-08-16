import streamlit as st
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
