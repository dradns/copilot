
from functions.on_click import *
from functions.clear_chat_history import *
from functions.render_chat import *
from functions.LLM_model import *
from functions.on_click import *

lc = Content()
pt = Prompt()

page_name = "chat"

def st_sidebar():
    if "chat_history" not in st.session_state.keys():
        st.session_state.chat_history = [{"role": "assistant", "content": lc.gt("user-story-ass-first-reply")}]

    with st.sidebar:
        render_chat()

        if st.text_input('', key='user_input', on_change=rerender_and_call(page_name)) != "":
            st_sidebar()


        st.button(lc.gt("user-story-button-forget"), on_click=clear_chat_history, type="primary", key=1010)

