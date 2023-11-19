import os
import time
import streamlit as st
import streamlit.components.v1 as components
from streamlit_chat import message
from components.sidebar import *
from functions.LLM_model import *

from locals.prompt import *
from locals.content import *

lc = Content()
pt = Prompt()
def clear_chat_history():
    del st.session_state["messages_us"]
    if 'messages_us' not in st.session_state:
        st.session_state['messages_us'] = [{"role": "assistant", "content": lc.gt("user-story-ass-first-reply")}]

def append_and_clear():
    st.session_state.chat_history.append({"role": "user", "content": st.session_state["user_input"]})
    with st.sidebar:
        with st.spinner(lc.gt("thinking")):
            response = modell_call(st.session_state["user_input"])
            print(response)
            st.session_state.chat_history.append({"role": "assistant", "content": response})
            st.session_state.user_input = ""


def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.responses.append(user_input)
def on_btn_click():
    del st.session_state['questions']
    del st.session_state['responses']


