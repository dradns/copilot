import os
import streamlit as st
import langchain
import transformers
import huggingface_hub
from huggingface_hub import InferenceClient
from locals.prompt import *
from locals.content import *

lc = Content()
pt = Prompt()

#collecting context

def collect_instructions(page_name):
    if page_name == "user-story":
        return collect_instructions_us()
    elif page_name == "use-case":
        return collect_instructions_uc()
    elif page_name == "acceptance-criteria":
        return collect_instructions_ac()
    elif page_name == "chat":
        return collect_instructions_ch()

def collect_instructions_ch():
    chat_role = pt.gp("chat-role")
    do_not_pretend = pt.gp("do-not-pretend")
    length_instruction = pt.gp("chat-length-instructions")
    string_instructions = chat_role + do_not_pretend+ length_instruction

    return string_instructions
def collect_instructions_us():
    user_story_role = pt.gp("user-story-role")
    do_not_pretend = pt.gp("do-not-pretend")
    user_story_description = pt.gp("user-story-description")
    user_story_example = pt.gp("user-story-example")
    language_instruction = pt.gp("language-instruction")
    length_instruction = pt.gp("user-story-length-instruction")
    string_instructions = user_story_role + do_not_pretend + user_story_description + user_story_example + language_instruction + length_instruction

    return string_instructions

def collect_instructions_uc():
    use_case_role = pt.gp("use-case-role")
    do_not_pretend = pt.gp("do-not-pretend")
    use_case_description = pt.gp("use-case-description")
    use_case_example = pt.gp("use-case-example")
    language_instruction = pt.gp("language-instruction")
    length_instruction = pt.gp("use-case-length-instruction")
    string_instructions = use_case_role + do_not_pretend + use_case_description + use_case_example + language_instruction + length_instruction

    return string_instructions

def collect_instructions_ac():
    use_case_role = pt.gp("acceptance-criteria-role")
    do_not_pretend = pt.gp("do-not-pretend")
    use_case_description = pt.gp("acceptance-criteria-description")
    use_case_example = pt.gp("acceptance-criteria-example")
    language_instruction = pt.gp("language-instruction")
    length_instruction = pt.gp("acceptance-criteria-length-instruction")
    string_instructions = use_case_role + do_not_pretend + use_case_description + use_case_example + language_instruction + length_instruction

    return string_instructions