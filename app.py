import streamlit as st
import requests
import json
from streamlit_ace import st_ace

st.set_page_config(page_title="Code75",page_icon='',layout='wide')

st.markdown("<h1 style='text-align: center;'>Code75</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: right;'>❤ Made by Vishnu</h6>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    h1 {
        background-color:red;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# create dropdown menu to select language
language_options = ['c', 'cpp', 'python', 'java']
language = st.selectbox('Select a language', language_options)

# divide the screen into two columns
col1, col2 = st.columns([3, 1])

# create code editor in the first column
with col1:
    code = st_ace(
        placeholder="Enter your code here",
        language=language,
        theme="github"
    )

# create section for taking input in the first column
with col2:
    st.write('Input:')
    input_data = st.text_area('Enter input data here')

# create a button to run the code in the second column
with col2:
    st.write('')
    st.write('')
    if st.button('Run'):
        if language!="python":
            payload = {
            'clientId': st.secrets["clientId"],
            'clientSecret':st.secrets["clientSecret"],
            'script': code,
            'language': language,
            'versionIndex': '0',
            'stdin': input_data
            }
        else:
            payload = {
            'clientId': st.secrets["clientId"],
            'clientSecret':st.secrets["clientSecret"],
            'script': code,
            'language': 'python3',
            'versionIndex': '0',
            'stdin': input_data
            }
            
        response = requests.post('https://api.jdoodle.com/v1/execute', json=payload)
        result = json.loads(response.text)
        st.write('Output:')
        st.write(result['output'])
