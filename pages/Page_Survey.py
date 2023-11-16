import streamlit as st
from streamlit_chat import message
from functions.LLM_model import *
from streamlit_quill import st_quill

def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.responses.append(user_input)

def on_btn_click():
    del st.session_state['questions']
    del st.session_state['responses']

st.session_state.setdefault('questions', [])

st.title("Survey QA Bot")
questions_list = ["DuplicateWidgetID: There are multiple identical widgets with the erawdsfasdfs erawdsfasdfs erawdsfasdfs erawdsfasdfs same generated key", 'question 2', 'question 3']
#response_list = ['res 1']
st.warning(lc.gt("user-story-lets-write"))
st.error('Error message')
st.warning('Warning message')
st.divider()
st.info('Info message')
st.success('Success message')

col1, col2 = st.columns([2,1])
with col1:
    if 'responses' not in st.session_state.keys():
        st.session_state.questions.extend(questions_list)
        st.session_state.responses = ["DuplicateWidgetID: There are multiple identical widgets with the erawdsfasdfs erawdsfasdfs erawdsfasdfs DuplicateWidgetID: There are multiple identical widgets with the erawdsfasdfs erawdsfasdfs erawdsfasdfs"]

chat_placeholder = st.empty()
st.button("Clear message", on_click=on_btn_click)


# for question in st.session_state.questions:
#     message(st.session_state['questions'][0], is_user=False)
#     message(st.session_state['responses'][0], is_user = True)
    #message(question)


# with st.container():
#     st.text_input("User Response:", on_change=on_input_change, key="user_input")
#
#
# st.write('sess questions')
# st.write(len(st.session_state['questions']))
# st.write(st.session_state['questions'])
# st.write('sess responses')
# st.write(len(st.session_state['responses']))
# st.write(st.session_state['responses'])
# st.write('session_state.keys')
# st.write(st.session_state)

col33, col34 = st.columns([6,4])
with col33:
    content = st_quill(
        placeholder="Write your text here",
        value=st.session_state['content_us'],
        # html= st.checkbox("Return HTML", False),
        # readonly=checkbox("Read only", False),
        key="quill12",
    )

i = 2000

with col34:
    for question in st.session_state.questions:
        message(st.session_state['questions'][0], is_user=False, key = i)
        message(st.session_state['responses'][0], is_user=True, key = i+1)
        i += 7

    #st.text_input('', key=7777)
    st.text_area('', key=7778)
