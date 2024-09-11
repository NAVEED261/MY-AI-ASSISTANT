import openai
import streamlit as st

# OpenAI API key ko set karein (yahaan apni API key daalein)
openai.api_key = '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'

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Latest GPT-4 model use karein
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

# Streamlit app ka front-end
st.title("AI Chatbot using GPT-4")

# User input ke liye text box
user_input = st.text_input("You: ", "Hello, how are you?")

# Jab user input kare aur 'Send' button dabaye to AI response generate karega
if st.button('Send'):
    response = generate_response(user_input)
    st.write(f"AI: {response}")
