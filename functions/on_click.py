import os
import time
import streamlit as st
import streamlit.components.v1 as components
from streamlit_chat import message

def clear_chat_history():
    del st.session_state["messages_us"]
    if 'messages_us' not in st.session_state:
        st.session_state['messages_us'] = [{"role": "assistant", "content": lc.gt("user-story-ass-first-reply")}]

def clear_text():
    st.session_state.my_text = st.session_state.widget
    st.session_state.widget = ""
def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.responses.append(user_input)
def on_btn_click():
    del st.session_state['questions']
    del st.session_state['responses']


