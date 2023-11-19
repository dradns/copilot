import os
import streamlit as st
from functions.LLM_model import *
from locals.prompt import *
from locals.content import *
from functions.collect_instructions import *
from functions.collect_message_history import *
from functions.set_session_variables import *

lc = Content()
pt = Prompt()

#SET SESSION VARIABLES
set_session_variables()

#TITLES
page_name = "use-case"
st.set_page_config(page_title="Analyst copilot", page_icon="📖", layout="wide")
st.title("📖"+ " " + lc.gt("use-case-title"))

#st.write('session_state.keys')
#st.write(st.session_state)

#st.info(lc.gt("use-case-description"))
#st.write("")

#Page goals, Page steps, Typical mistakes
col1, col2, col3 = st.columns(3)
with col1:
   with st.expander(lc.gt("use-case-goal-page")):
       st.write("Привет")
       st.image("https://static.streamlit.io/examples/dice.jpg")

with col2:
    with st.expander(lc.gt("use-case-steps")):
        st.video("https://www.youtube.com/watch?v=ovtxI75g34g")

with col3:
    with st.expander(lc.gt("use-case-typical-mistakes")):
        st.image("static/2023-10-30_16-10-05.png")

#st.warning(lc.gt("use-case-lets-write"))

#DECLARE BUTTON RESET HISTORY
def clear_chat_history():
    del st.session_state["messages_uc"]
    if 'messages_uc' not in st.session_state:
        st.session_state['messages_uc'] = [{"role": "assistant", "content": lc.gt("use-case-ass-first-reply")}]

#USAGE BUTTON RESET HISTORY
st.button(lc.gt("use-case-button-forget"), on_click=clear_chat_history, type="primary", key=2020)

# Store LLM generated responses
if "messages_uc" not in st.session_state.keys():
    st.session_state.messages_uc = [{"role": "assistant", "content": lc.gt("use-case-ass-first-reply")}]

# Display or clear chat history
for message in st.session_state.messages_uc:
    with st.chat_message(message["role"]):
        st.write(message["content"])

#append user message to global
if user_prompt := st.chat_input():
    st.session_state.messages_uc.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.write(user_prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages_uc[-1]["role"] != "assistant":
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
    st.session_state.messages_uc.append(message)