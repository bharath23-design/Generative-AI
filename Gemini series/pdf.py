import streamlit as st
import os
import google.generativeai as genai
import dotenv

dotenv.load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up the model
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# Streamlit app
def main():
    st.title(" 📚 PDF Chatbot 🤖 ")

    # Upload PDF
    uploaded_file = st.file_uploader("Upload a PDF")

    if uploaded_file is not None:
        # Get the temporary file path from the uploaded file
        tmp_filepath = uploaded_file.name

        # Save the uploaded file to the temporary location
        with open(tmp_filepath, "wb") as f:
            f.write(uploaded_file.getvalue())

        # Use the temporary file path for upload
        file_id = genai.upload_file(path=tmp_filepath)

        # Text input for asking multiple questions
        user_input = st.text_input("Ask a question about the document:")

        if user_input:
            # Prompt the model with the file ID and the user's question
            response = model.generate_content([file_id, user_input])

            # Display the answer
            st.text_area("Response:", response.text)

if __name__ == "__main__":
    main()
