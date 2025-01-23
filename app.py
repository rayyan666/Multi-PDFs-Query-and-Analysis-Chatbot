import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(separator="\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
    )

    chunks = text_splitter.split_text(text)
    return chunks





def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDF files", page_icon=":books:")

    st.header("Chat with multiple PDF files :books:")
    st.text_input("Ask a question baout the relevant document:")

    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader(
            "Upload you PDF files here and click the submit button",accept_multiple_files=True)
        if st.button("Submit"):
            with st.spinner("Processing"):
                #get the pdf text 
                raw_text = get_pdf_text(pdf_docs)

                #get the text chunks
                text_chunks = get_text_chunks(raw_text)
                #create vector store

if __name__=='__main__':
    main()