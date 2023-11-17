from functions.set_session_variables import *
from components.sidebar import *
from components.us.us_buttons import *
from components.us.us_header import *
from components.us.us_quill import *

#DECLARE SESSION VARIABLES
set_session_variables()

#RENDER SIDEBAR
st_sidebar()

#DECLARE CONFIG
page_name = "user-story"

#RENDER US HEADER
us_header()

#RENDER US QUILL
us_quill()

#RENDER US BUTTONS
us_buttons()

#DEBUG
st.write('session_state.keys')
st.write(st.session_state)





