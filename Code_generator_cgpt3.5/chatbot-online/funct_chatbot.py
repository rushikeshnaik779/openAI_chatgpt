import streamlit as st
from streamlit_chat import message
from utils import get_initial_message, get_chatgpt_response, update_chat
import os
from dotenv import load_dotenv
load_dotenv()
import openai
import tempfile
import os
import traceback


openai.api_key = "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"


def get_response_from_chatgpt(user_input):
    with st.spinner("generating..."):
        messages = st.session_state['messages']
        messages = update_chat(messages, "user", user_input)
        response = get_chatgpt_response(messages, model)
        messages = update_chat(messages, "assistant", response)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
    
    
        


def run_code(code): 
    
    temp_file = tempfile.NamedTemporaryFile(suffix='.py', delete=False)
    temp_file.write(code.encode())
    temp_file.close()
    temp_file_path = temp_file.name
    os.system(f"streamlit run {temp_file_path}") 




if "__main__" == __name__ :
        
    st.title("Chatbot : ChatGPT and Streamlit Chat")
    st.subheader("Find code") 

    model = st.selectbox(
    "Select a model",
    ("gpt-3.5-turbo", "gpt-4")
    )

    if 'generated' not in st.session_state:
        st.session_state['generated'] = []
    if 'past' not in st.session_state:
        st.session_state['past'] = []

    if 'messages' not in st.session_state:
        st.session_state['messages'] = get_initial_message()


    # Text input box
    user_input = st.text_input("Enter text:")
    
    # Button to trigger processing
    if st.button("Get response from chatgpt"):
        get_response_from_chatgpt(user_input)



    if st.session_state['generated']:

        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            #st.code(st.session_state["generated"][i])
            if "```" in st.session_state["generated"][i] :
                try:  
                    splitted_list = st.session_state["generated"][i].split("```")
                    for c in splitted_list: 
                        if "python" in c: 
                            code = c.replace("python", "")
                    if st.button('run the code', key=i): 
                        run_code(code)
                    message(st.code(code, language="python"))                    
                except Exception:
                    traceback.print_exc() 
                       
            elif "```python" not in st.session_state["generated"][i] : 
                message(st.session_state["generated"][i], key=str(i))


    st.write(st.session_state["generated"])