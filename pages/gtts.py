from functions.LLM_model import *
from gtts import gTTS
from io import BytesIO

def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.responses.append(user_input)

def on_btn_click():
    del st.session_state['questions']
    del st.session_state['responses']

st.session_state.setdefault('questions', [])

st.title("Survey QA Bot")
questions_list = ['question 1', 'question 2', 'question 3']
#response_list = ['res 1']
st.warning(lc.gt("user-story-lets-write"))
st.error('Error message')
st.warning('Warning message')
st.divider()
st.info('Info message')
st.success('Success message')

if 'responses' not in st.session_state.keys():
    st.session_state.questions.extend(questions_list)
    st.session_state.responses = ['res 1']

chat_placeholder = st.empty()
st.button("Clear message", on_click=on_btn_click)


# for question in st.session_state.questions:
#     message(st.session_state['questions'][0], is_user=False)
#     message(st.session_state['responses'][0], is_user = True)
#     #message(question)


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

text = st.text_input("Enter text")

sound_file = BytesIO()
if text:
    tts = gTTS(text, lang='ru')
    tts.write_to_fp(sound_file)
    st.audio(sound_file)