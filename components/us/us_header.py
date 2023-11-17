import os
import time
import streamlit as st
import streamlit.components.v1 as components
from streamlit_chat import message
from functions.on_click import *
from locals.content import *

lc = Content()
def us_header():
    col101, col102 = st.columns([6, 4])
    with col101:
        st.subheader("📖" + " " + lc.gt("user-story-title"))
    with col102:
        with st.expander(lc.gt("user-story-goal-page")):
            tab1, tab2, tab3 = st.tabs(["Цели страницы ---", "Этапы выполнения---", "Типичные ошибки---"])
            tab1.write("this is tab 1")
            tab1.image("https://static.streamlit.io/examples/dice.jpg")
            tab2.write("this is tab 2")
            tab2.video("https://www.youtube.com/watch?v=ovtxI75g34g")
            tab3.write("this is tab 2")
            tab3.video("https://www.youtube.com/watch?v=ovtxI75g34g")

