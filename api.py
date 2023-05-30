import streamlit as st
from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Define the Streamlit app
def main():
    st.title("Text Summarizer")
    article = st.text_area("Enter the article:", height=200)
    if st.button("Summarize"):
        if article:
            # Generate the summary
            summary = summarizer(article, max_length=130, min_length=30, do_sample=False)
            st.success(summary[0]['summary_text'])
        else:
            st.warning("Please enter some text.")

# Run the app
if __name__ == '__main__':
    main()
