import os
import time
import streamlit as st
import streamlit.components.v1 as components
from streamlit_chat import message
from functions.on_click import *
from locals.content import *
from streamlit_quill import st_quill

lc = Content()
def us_quill():
    content = st_quill(
        placeholder="Write your text here",
        value=st.session_state['content_us'],
        # html= st.checkbox("Return HTML", False),
        # readonly=checkbox("Read only", False),
        key="quill12",
    )

