import os
import openai
import gradio as gr

# Set OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Conversation prompt and sequences
start_sequence = "\nAI:"
restart_sequence = "\nHuman: "
prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "

# Function to interact with OpenAI model
def openai_create(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    return response.choices[0].text

# Function to handle chat interactions and history
def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history

# Set up Gradio interface
block = gr.Interface(
    fn=chatgpt_clone,
    inputs=gr.Textbox(placeholder=prompt, label="User Input"),
    outputs=[gr.Textbox(label="Chatbot Response", readonly=True), gr.Textbox(label="History", readonly=True)],
    title="WhizChat",
    description="Chat with an AI assistant."
)

block.launch(debug=True)
