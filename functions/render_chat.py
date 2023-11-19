import os
import time
import streamlit as st
import streamlit.components.v1 as components
from streamlit_chat import message

logo_human = "https://i.postimg.cc/QdbnMMkd/analyst-ava.png"
logo_robot = "https://i.postimg.cc/L8sGLRb6/logo2.png"

st.session_state.get("global_key_counter")
def render_chat():
    j = st.session_state.get("global_key_counter")
    for item in st.session_state.chat_history:
        if item["role"] == "assistant":
            message(item["content"], is_user=False, logo=logo_robot, key=j)
        else:
            message(item["content"], is_user=True, logo=logo_human, key=j + 1)
        st.session_state["global_key_counter"] += 7
        j = st.session_state.get("global_key_counter")
