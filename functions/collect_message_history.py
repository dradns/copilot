import os
import streamlit as st
import langchain
import transformers
import huggingface_hub
from huggingface_hub import InferenceClient

def map_session_state(page_name):
    if page_name == 'user-story':
        return st.session_state.messages_us
    elif page_name == 'use-case':
        return st.session_state.messages_uc
    elif page_name == 'acceptance-criteria':
        return st.session_state.messages_ac
    elif page_name == 'chat':
        return st.session_state.chat_history

#collecting context
def collect_message_history(user_prompt, page_name):
    string_dialogue_before = ""
    for dict_message in map_session_state(page_name):
        if dict_message["role"] == "user":
            string_dialogue_before += "User: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue_before += "Assistant: " + dict_message["content"] + "\n\n"
    # string_dialogue_after = f"{string_dialogue_before} {user_prompt} Assistant: "
    string_dialogue_after = f"{string_dialogue_before}"
    print(string_dialogue_after)
    return string_dialogue_after
