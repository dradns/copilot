import os
import streamlit as st
import langchain
import transformers
import huggingface_hub
from huggingface_hub import InferenceClient
from functions.collect_instructions import *
from functions.collect_message_history import *

#collecting context
def model_response(user_prompt, page_name):
    #1. собрать взять нужную инструкцию в зависимости от языка
    #2. собрать историю сообщений

    # Collect instructions for page_name
    string_instructions = collect_instructions(page_name)
    #Сollect whole message history
    string_dialogue = collect_message_history(user_prompt, page_name)
    total_string = string_instructions + string_dialogue
    print(total_string)
    print('--------------')
    return modell_call(total_string)

endpoint_url = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-7b-chat-hf"
hf_token = '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'

client = InferenceClient(endpoint_url, token=hf_token)

gen_kwargs = dict(
    max_new_tokens=1000,
    top_k=30,
    top_p=0.5,
    temperature=0.1,
    repetition_penalty=1.02,
    stream = False,
    details=False,
    #stop_sequences=["\nUser:", "<|endoftext|>", "</s>"],
)

#model call
def modell_call(total_string):
    return client.text_generation(total_string, **gen_kwargs)