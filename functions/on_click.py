import os
import time
import streamlit as st
import streamlit.components.v1 as components
from streamlit_chat import message

def clear_chat_history():
    del st.session_state["messages_us"]
    if 'messages_us' not in st.session_state:
        st.session_state['messages_us'] = [{"role": "assistant", "content": lc.gt("user-story-ass-first-reply")}]

def append_and_clear():
    st.session_state.my_text = st.session_state.user_input
    print(st.session_state.my_text + "\n st.session_state.my_text \n")
    print(st.session_state.user_input + "\n st.session_state.user_input \n")
    st.session_state.chat_history.append({"role": "user", "content": st.session_state["my_text"]})
    st.session_state.user_input = ""
    st.session_state.my_text = ""

def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.responses.append(user_input)
def on_btn_click():
    del st.session_state['questions']
    del st.session_state['responses']


