import streamlit as st
from llama_index.llms.ollama import Ollama
import time
# Initialize the Ollama model
model = Ollama(model="llama3.1")
# Function to get the model response
def get_model_response(question):
    attempts = 3  # Number of retry attempts
    for attempt in range(attempts):
        try:
            result = model.complete(question)
            return result
        except Exception as e:
            if attempt < attempts - 1:
                time.sleep(2)  # Wait for 2 seconds before retrying
            else:
                return f"Error: {str(e)}"

# Streamlit UI
st.title("Build your own LLM model with llama3.1")

# Input for the question
question = st.text_input("Enter your question:")

# When the button is pressed, run the model and display the result
if st.button("Get Answer"):
    if question:
        result = get_model_response(question)
        st.write("Answer:", result)
    else:
        st.write("Please enter a question.")
