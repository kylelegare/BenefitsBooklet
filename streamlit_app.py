from gpt_index import GPTSimpleVectorIndex
from langchain import OpenAI
import os
import streamlit as st

# Set the OpenAI API key
openai.api_key = st.secrets['openai']['api_key']

#Page Config For Streamlit
st.set_page_config(page_title='Benefits Booklet Q&A')

# Load the CSS styles from file
with open("style.css") as f:
    styles = f.read()

# Display the CSS styles
st.markdown(f"<style>{styles}</style>", unsafe_allow_html=True)

# Set the page title and headline

st.markdown('<h1 class="headline">Canadian Glianeers Benefits Booklet Q&A</h1>', unsafe_allow_html=True)

def ask_benefits():
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    query = st.text_input("The RBC Benefits Booklet has been converted into a document that can be read by OpenAI allowing you to ask any questions about the information inside ", value='')
    if st.button("Ask The Booklet"):
        response = index.query(query)
        response_lines = response.response.splitlines()
        st.write("\n\nThe Benefit Booklet Says:\n")
        for line in response_lines:
            st.write("\n" + line)
        st.write("\n\n")
        

# Call the function
ask_benefits()

