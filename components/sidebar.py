import os
import time
import streamlit as st
import streamlit.components.v1 as components
from streamlit_chat import message
from functions.on_click import *

logo_human = "https://i.postimg.cc/QdbnMMkd/analyst-ava.png"
logo_robot = "https://i.postimg.cc/L8sGLRb6/logo2.png"
def st_sidebar():
    # j = 20000
    st.set_page_config(page_title="Analyst copilot", page_icon="📖", layout="wide", initial_sidebar_state="expanded")

    with st.sidebar:
        for item in st.session_state.chat_history:
            # message(st.session_state['questions'][0], is_user=False, key=j)
            # message(st.session_state['responses'][0], is_user=True, key=j + 1)
            message("check", is_user=True, logo=logo_human)
            message("pong", is_user=False, logo=logo_robot)
            #j += 7

        with st.spinner("Loading..."):
            st.success("Done!")
            st.text_input('', key=776655567, on_change=clear_text)
            #st.text_area('', key='widget12', on_change=clear_text, label="1")
            st.button("Clear message", on_click=on_btn_click,key=58930)


# st.markdown("""
# <style>
#     [data-testid=stSidebar] {
#         background-color: #ff000050;
#     }
# </style>
# """, unsafe_allow_html=True)
#
# st.markdown("""
# <style>
#     [data-testid=stChatInput] {
#         background-color: #ff000050;
#     }
# </style>
# """, unsafe_allow_html=True)