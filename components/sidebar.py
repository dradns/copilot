import os
import time
import streamlit as st
import streamlit.components.v1 as components
from streamlit_chat import message
from functions.on_click import *
from functions.clear_chat_history import *
from functions.render_chat import *
from locals.prompt import *
from locals.content import *
from functions.LLM_model import *

lc = Content()
pt = Prompt()

page_name = "chat-history"

def st_sidebar():
    if "chat_history" not in st.session_state.keys():
        st.session_state.chat_history = [{"role": "assistant", "content": lc.gt("user-story-ass-first-reply")}]

    with st.sidebar:
        render_chat()

        if st.text_input('', key='user_input', on_change=append_and_clear) != "":
            st_sidebar()

        st.button(lc.gt("user-story-button-forget"), on_click=clear_chat_history, type="primary", key=1010)

