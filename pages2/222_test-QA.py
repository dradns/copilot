import os
import streamlit as st
from components.sidebar import sidebar
from functions.LLM_model import *
from huggingface_hub import InferenceClient
from locals.prompt import *
from locals.content import *
from locals.survey import *

lc = Content()
pt = Prompt()
sr = Survey()

#set survey counter
survey_name = "first_survey"
if 'page_survey_counter' not in st.session_state:
    st.session_state['page_survey_counter'] = len(sr.gs(survey_name))

#TITLES
st.set_page_config(page_title="Analyst copilot", page_icon="📖", layout="wide")
st.title("📖"+ lc.gt("user-story-title"))
st.write("")
#st.header('Test 1')
#st.subheader('Test 1')

st.write('session_state.keys')
st.write(st.session_state)

st.write('survey')
st.write(sr.gs('first_survey'))

#st.video("https://www.youtube.com/watch?v=ovtxI75g34g")

with st.expander(lc.gt("user-story-goal-page")):
    st.write("Привет")
    st.image("https://static.streamlit.io/examples/dice.jpg")

st.write("")

with st.expander(lc.gt("user-story-steps")):
    st.video("https://www.youtube.com/watch?v=ovtxI75g34g")

st.write("")

with st.expander(lc.gt("user-story-typical-mistakes")):
    st.image("static/2023-10-30_16-10-05.png")

st.divider()

st.warning(lc.gt("user-story-lets-write"))

def get_assistant_reply():
    if st.session_state.page_survey_counter > 0:
        with st.chat_message("assistant"):
            full_response2 = sr.gs(survey_name)[len(sr.gs(survey_name)) - st.session_state.page_survey_counter]
            placeholder = st.empty()
            placeholder.markdown(full_response2)
            st.session_state.page_survey_counter -= 1
            st.write(st.session_state.page_survey_counter)
        message = {"role": "assistant", "content": full_response2}

    else:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = model_response(prompt)
                placeholder = st.empty()
                full_response = ''
                for item in response:
                    full_response += item
                    placeholder.markdown(full_response)
                placeholder.markdown(full_response)
        message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)

#DECLARE BUTTON RESET HISTORY
def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "I'm best business analyst ever! Wanna help?"}]
#USAGE BUTTON RESET HISTORY
st.button(lc.gt("user-story-button-forget"), on_click=clear_chat_history)

# Enable caching for expensive functions
#bootstrap_caching()
# Render sidebar
sidebar()

#st.session_state["API_KEY"] = 'r8_5dXks0XSi27sUU4zxiCeKiYOB1wvfil3UZOxV'
#replicate_api = st.session_state.get("API_KEY")
#os.environ['REPLICATE_API_TOKEN'] = replicate_api
# print('API KEY')
# print(st.session_state.get("API_KEY"))

# Set first message to history
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "I'm best business analyst ever! Wanna help?"}]

# Render chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Render current user input
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)


# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    get_assistant_reply()


# def is_surv_ques(survey_name):
#     if st.session_state.page_survey_counter > 0:
#         return True
#     else:
#         return False



