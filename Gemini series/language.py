import streamlit as st
import os
import google.generativeai as genai
import dotenv
dotenv.load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up the model
generation_config = {
    "temperature": 0.2,
    "top_p": 0.8,
    "top_k": 64,
    "max_output_tokens": 8192,
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Function to translate text
def translate_text(text, source_language, target_language):
    prompt = f"Translate the following text from {source_language} to {target_language}: \"{text}\""
    response = model.generate_content(prompt)
    try:
        return response.text
    except Exception as e:
        print("Exception:\n", e, "\n")
        print("Response:\n", response.candidates)

# Streamlit app
def main():
    st.title("✍️🌐 Language Translator using Gemini 1.5 Flash 🌟✨")
    source_text = st.text_input("Enter the text to translate:")
    source_lang = st.selectbox("Source Language", ["English", "French", "Spanish", "German"])
    target_lang = st.selectbox("Target Language", ["English", "French", "Spanish", "German",'Telugu','Hindi'])

    if st.button("Translate"):
        translated_text = translate_text(source_text, source_lang.lower(), target_lang.lower())
        st.text_area("Translated Text:", translated_text)

if __name__ == "__main__":
    main()