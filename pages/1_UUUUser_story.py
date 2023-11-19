import os
import streamlit as st
from functions.LLM_model import *
from locals.prompt import *
from locals.content import *
from functions.collect_instructions import *
from functions.collect_message_history import *
from functions.set_session_variables import *
from streamlit_quill import st_quill

lc = Content()
pt = Prompt()

#SET SESSION VARIABLES
set_session_variables()

#TITLES
page_name = "user-story"
st.set_page_config(page_title="Analyst copilot", page_icon="📖", layout="wide")

#st.write('session_state.keys')
#st.write(st.session_state)

#st.info(lc.gt("user-story-description"))
#st.write("")

#Page goals, Page steps, Typical mistakes
# col1, col2, col3 = st.columns(3)
# with col1:
#    with st.expander(lc.gt("user-story-goal-page")):
#        st.write("Привет")
#        st.image("https://static.streamlit.io/examples/dice.jpg")
#
# with col2:
#     with st.expander(lc.gt("user-story-steps")):
#         st.video("https://www.youtube.com/watch?v=ovtxI75g34g")
#
# with col3:
#     with st.expander(lc.gt("user-story-typical-mistakes")):
#         st.image("static/2023-10-30_16-10-05.png")

#st.divider()

#DECLARE BUTTON RESET HISTORY
def clear_chat_history():
    del st.session_state["messages_us"]
    if 'messages_us' not in st.session_state:
        st.session_state['messages_us'] = [{"role": "assistant", "content": lc.gt("user-story-ass-first-reply")}]

col1, col2,col3 = st.columns([4,4,2])
with col1:
   st.subheader("📖"+ " " + lc.gt("user-story-title"))
with col2:
    with st.expander(lc.gt("user-story-goal-page")):
        tab1, tab2, tab3 = st.tabs(["Цели страницы ---", "Этапы выполнения---", "Типичные ошибки---"])
        tab1.write("this is tab 1")
        tab1.image("https://static.streamlit.io/examples/dice.jpg")
        tab2.write("this is tab 2")
        tab2.video("https://www.youtube.com/watch?v=ovtxI75g34g")
        tab3.write("this is tab 2")
        tab3.video("https://www.youtube.com/watch?v=ovtxI75g34g")

#st.divider()

if "content_us" not in st.session_state.keys():
    st.session_state.content_us = ""

st.session_state['content_us'] = "Can you tell me a little bit about the system you're looking to improve? What is the main goal you want to achieve with this system? And what kind of user are you? For example, are you an administrator, a manager, or an end-user?"

col13, col14 = st.columns([8,2])
with col13:
    content = st_quill(
        placeholder="Write your text here",
        value=st.session_state['content_us'],
        # html= st.checkbox("Return HTML", False),
        # readonly=checkbox("Read only", False),
        key="quill",
    )

with col14:
    st.button("Сохранить", on_click=clear_chat_history, type="primary", key=1011)
    st.button("Улучшить", on_click=clear_chat_history, type="primary", key=1012)
    st.button("Создать UC", on_click=clear_chat_history, type="primary", key=1013)








col23, col24 = st.columns([3,7])

def render_dialog():
    for message in st.session_state.messages_us:
        with st.chat_message(message["role"]):
            st.write(message["content"])

with col24:
    content = st_quill(
        placeholder="Write your text here",
        value=st.session_state['content_us'],
        # html= st.checkbox("Return HTML", False),
        # readonly=checkbox("Read only", False),
        key="quill234234",
    )
# Store LLM generated responses
with col23:
    if "messages_us" not in st.session_state.keys():
        st.session_state.messages_us = [{"role": "assistant", "content": lc.gt("user-story-ass-first-reply")}]



# USAGE BUTTON RESET HISTORY
    st.button(lc.gt("user-story-button-forget"), on_click=clear_chat_history, type="primary", key=1010)
    render_dialog()
    st.text_input('', key=776667)
    st.text_area('', key=777777)

#append user message to global
if user_prompt := st.chat_input():
    st.session_state.messages_us.append({"role": "user", "content": user_prompt})


# Generate a new response if last message is not from assistant
if st.session_state.messages_us[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner(lc.gt("thinking")):
            response = model_response(user_prompt, page_name)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages_us.append(message)
