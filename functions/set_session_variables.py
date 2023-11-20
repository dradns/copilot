import streamlit as st
from locals.prompt import *
from locals.content import *

lc = Content()
pt = Prompt()

def set_session_variables():
    st.session_state['content_us'] = "Can you tell me a little bit about the system you're looking to improve? What is the main goal you want to achieve with this system? And what kind of user are you? For example, are you an administrator, a manager, or an end-user?"
    #st.session_state.setdefault('questions', [])
    st.session_state['questions_list_1'] = [
        "DuplicateWidgetID: There are multiple identical widgets with the erawdsfasdfs erawdsfasdfs erawdsfasdfs erawdsfasdfs same generated key",
        'question 2', 'question 3']

    #SET LANGUAGE
    if "LANGUAGE" not in st.session_state.keys():
        st.session_state["LANGUAGE"] = 'RUS'
    #SET MODEL
    if "selected_model" not in st.session_state.keys():
        st.session_state["selected_model"] = 'Llama2-13B'

    #SET HISTORY
    if "chat_history" not in st.session_state.keys():
        st.session_state.chat_history = [{"role": "assistant", "content": lc.gt("user-story-ass-first-reply")}]

    if "user_input" not in st.session_state.keys():
        st.session_state["user_input"] = ""

    if "global_key_counter" not in st.session_state.keys():
        st.session_state["global_key_counter"] = 40000

    if "temp_input" not in st.session_state.keys():
        st.session_state["temp_input"] = ""