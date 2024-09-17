import streamlit as st
from PIL import Image


if 'state_1' not in st.session_state: 
    st.write("State")
    print("state")
    st.session_state['state_1'] = True
    st.session_state['state_2'] = False




# Checkbox States
state_1 = st.sidebar.checkbox("NER Name", value=st.session_state['state_1'])
state_2 = st.sidebar.checkbox("NER Date", value=st.session_state['state_2'])

# Handle Logic - Only one can be chosen
if state_1:
    st.session_state['state_1']  = True
    st.session_state['state_2']  = False
    state_1 = st.session_state['state_1']
    state_2 = st.session_state['state_2']
    image = Image.open('data/name.png')
    st.image(image, caption='Image 1', use_column_width=True)
    
if state_2:
    st.session_state['state_1']  = False
    st.session_state['state_2']  = True
    state_1 = st.session_state['state_1']
    state_2 = st.session_state['state_2']
    image = Image.open('data/date.png')
    st.image(image, caption='Image 2', use_column_width=True)
