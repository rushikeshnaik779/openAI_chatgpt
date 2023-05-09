import streamlit as st
from connection import get_response

import openai 
import streamlit as st

# pip install streamlit-chat  
from streamlit_chat import message


def home():
    prompt_input = st.text_input('Give the Input for app to write code')
    return prompt_input





if __name__ == "__main__":
    prompt_input = home()
    if st.button("click me to get the results"): 
        response = get_response(prompt_input=prompt_input)
        st.write(response)
        print(response)
    

    