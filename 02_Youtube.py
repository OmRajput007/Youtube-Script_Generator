import openai
import streamlit as st
import os
from dotenv import load_dotenv

# Load your API keys from .env file
load_dotenv()

openai_api_key = os.getenv("api_key")
organization_id = os.getenv("organization")
project_id = os.getenv("project")

# Create the OpenAI client securely
client = openai.OpenAI(
    api_key=openai_api_key,
    organization=organization_id,
    project=project_id
)

st.title("Youtube Script Generator")

topic = st.text_input("Enter your video input here")

tone = st.selectbox("Choose the tone", ["Informative", "Dramatic", "Funny", "Poetic"])

if st.button("Generate Script"):
    messages = [
        {"role": "system", "content" : f"You are a {tone.lower()} YouTube scriptwriter."},
        {"role": "user", "content" : f"Write a detailed 700-word YouTube script on the topic: {topic}"}
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    st.write(response.choices[0].message.content)


