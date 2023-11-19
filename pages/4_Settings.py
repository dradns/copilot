import os
import streamlit as st
from components.sidebar import st_sidebar
from locals.prompt import *
from locals.content import *
from streamlit_quill import st_quill

lc = Content()
pt = Prompt()

def default_language():
    if st.session_state["LANGUAGE"] == 'RUS':
        return ['Русский', 'English']
    else:
        return ['English', 'Русский']

st.subheader('Language')

if "LANGUAGE" not in st.session_state.keys():
    st.session_state["LANGUAGE"] = 'RUS'

selected_language = st.selectbox('Choose a language', default_language())

if selected_language == 'Русский':
    st.session_state["LANGUAGE"] = 'RUS'
elif selected_language == 'English':
    st.session_state["LANGUAGE"] = 'ENG'

st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")

st.write('session_state.keys')
st.write(st.session_state)

if "selected_model" not in st.session_state.keys():
    st.session_state["selected_model"] = 'Llama2-13B'

st.subheader('Models and parameters')
selected_model = st.selectbox('Choose a Llama2 model', ['Llama2-7B', 'Llama2-13B'])

if selected_model == 'Llama2-7B':
    llm = 'a16z-infra/llama7b-v2-chat:4f0a4744c7295c024a1de15e1a63c880d3da035fa1f49bfd344fe076074c8eea'
    st.session_state["selected_model"] = 'Llama2-7B'
elif selected_model == 'Llama2-13B':
    llm = 'a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5'
    st.session_state["selected_model"] = 'Llama2-13B'


temperature = st.slider('temperature', min_value=0.01, max_value=5.0, value=0.1, step=0.01)
top_p = st.slider('top_p', min_value=0.01, max_value=1.0, value=0.9, step=0.01)
max_length = st.slider('max_length', min_value=32, max_value=128, value=120, step=8)

content = st_quill(
    placeholder="Write your text here",
    # html=checkbox("Return HTML", False),
    # readonly=checkbox("Read only", False),
    key="quill",
)

if content:
    st.subheader("Content")
    st.text(content)

#EXAMPE QUILL
#https://okld-gallery.streamlit.app/?p=quill-editor



# st.write('selected_language var')
# st.write(selected_language)
# st.write()
#
# st.write('selected_language ENV')
# st.write(st.session_state.get("LANGUAGE"))
# st.write()
#
# st.write('selected content CONTENT CLASS')
# st.write(lc.gt('test'))
# st.write()
#
# st.write('selected content PROMPT CLASS')
# st.write(pt.gp('test'))
# st.write()

# if not api_key:
#     st.warning(
#         "Enter your API key in the sidebar. You can get a key at")
#
# api_key_input = st.text_input(
#             "API Key",
#             type="password",
#             placeholder="Paste your API key here ",  # noqa: E501
#             value=os.environ.get("API_KEY", None)
#             or st.session_state.get("API_KEY", ""),
#         )