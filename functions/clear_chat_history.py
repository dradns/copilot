import streamlit as st
from locals.prompt import *
from locals.content import *

lc = Content()
pt = Prompt()

def clear_chat_history():
    del st.session_state["chat_history"]
    if 'chat_history' not in st.session_state:
        st.session_state['messages_us'] = [{"role": "assistant", "content": lc.gt("user-story-ass-first-reply")}]
