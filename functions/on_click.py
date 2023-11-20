import os
import time
import streamlit as st
import streamlit.components.v1 as components
from streamlit_chat import message
from components.sidebar import *
from locals.prompt import *
from locals.content import *
from functions.LLM_model import *

lc = Content()
pt = Prompt()
def clear_chat_history():
    del st.session_state["chat_history"]
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = [{"role": "assistant", "content": lc.gt("user-story-ass-first-reply")}]

def rerender_and_call(page_name):
    st.session_state.chat_history.append({"role": "user", "content": st.session_state["user_input"]})
    with st.sidebar:
        with st.spinner(lc.gt("thinking")):
            #print(response)
            response = model_chat_response(st.session_state["user_input"], page_name)
            st.session_state.chat_history.append({"role": "assistant", "content": response})
            st.session_state.user_input = ""

def on_btn_click():
    del st.session_state['questions']
    del st.session_state['responses']


