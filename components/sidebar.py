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

        if st.session_state.chat_history[-1]["role"] != "assistant":
            with st.spinner(lc.gt("thinking")):
                response = modell_call("who ou")
                print(response)
                st.session_state.chat_history.append({"role": "assistant", "content": response})
                message(st.session_state.chat_history[-1]["content"], is_user=False, logo=logo_robot, key=st.session_state.get("global_key_counter")+500000)

        if user_prompt := st.text_input('', key='user_input', on_change=append_and_clear):
            pass

        st.button(lc.gt("user-story-button-forget"), on_click=clear_chat_history, type="primary", key=1010)