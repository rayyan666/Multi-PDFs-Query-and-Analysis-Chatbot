import streamlit as st
from dotenv import load_dotenv

def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDF files", page_icon=":books:")

    st.header("Chat with multiple PDF files :books:")
    st.text_input("Ask a question baout the relevant document:")

    with st.sidebar:
        st.subheader("Your Documents")
        st.file_uploader("Upload you PDF files here and click the submit button")
        st.button("Submit")


if __name__=='__main__':
    main()