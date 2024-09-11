import openai
import streamlit as st

# OpenAI API key ko set karein
openai.api_key = 'sk-5AF0armObv3N6VvreKReGSzeenA7y_39d0lCF0QcrjT3BlbkFJl-CTfDyW2aIRLw0vstlkf5_zckEL6yBU0SZelkubIA'

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Latest model use karna
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

# Streamlit app ka front-end
st.title("AI Chatbot using OpenAI")

# User input ke liye text box
user_input = st.text_input("You: ", "Hello, how are you?")

# Jab user input kare aur 'Send' button dabaye to AI response generate karega
if st.button('Send'):
    response = generate_response(user_input)
    st.write(f"AI: {response}")
