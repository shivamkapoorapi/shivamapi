import streamlit as st
from transformers import pipeline

# Set up the summarization pipeline
summarizer = pipeline("summarization")

# Streamlit app title and description
st.title("Text Summarization")
st.markdown("This app uses the Hugging Face Transformers library to summarize text.")

# Text input box
text = st.text_area("Enter text to be summarized", height=200)

# Summarization button
if st.button("Summarize"):
    if text:
        # Generate the summary
        summary = summarizer(text, max_length=150, min_length=30, do_sample=False)[0]["summary_text"]
        
        # Display the summary
        st.markdown("### Summary")
        st.write(summary)
    else:
        st.warning("Please enter some text to be summarized.")
