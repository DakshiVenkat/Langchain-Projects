import requests
import streamlit as st

def get_ollama_response(input_text):
    url = "http://localhost:8000/essay/invoke"
    st.write(f"Making request to {url}")
    response = requests.post(url, json={'input': {'topic': input_text}})
    return response.json()['output']

# Streamlit framework
st.title('LangChain demo with QWEN2 LLM API')
input_text = st.text_input("Write an essay on")

if input_text:
    st.write(get_ollama_response(input_text))
