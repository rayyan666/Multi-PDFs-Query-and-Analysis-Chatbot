import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
# from langchain.chat_models import ChatOpenAI
from langchain.llms import HuggingFaceHub
from htmlpage import css,bot_template,user_template
import os
from logger import logging

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    logging.info(f"Extracted text from {len(pdf_docs)} PDF(s).")
    return text
    


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(separator="\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
    )

    chunks = text_splitter.split_text(text)
    logging.info(f"Text split into {len(chunks)} chunks.")
    return chunks


def get_vectorstore(text_chunks):
    embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    logging.info("Vectorstore created successfully.")
    return vectorstore


def get_conversation_chain(vectorstore):
    load_dotenv()
    hf_api = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    if hf_api is None:
       logging.error("API_KEY environment variable not set.")
       raise ValueError("API_KEY environment variable not set")
    
    #llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
    logging.info("Initializing HuggingFaceHub with model: google/flan-t5-large")
    llm = HuggingFaceHub(repo_id="google/flan-t5-lar    ge", model_kwargs={"temperature": 0.7, "max_length": 512}, huggingfacehub_api_token=hf_api)
    memory = ConversationBufferMemory(memory_key= 'chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory = memory

    )
    logging.info("Conversation chain created successfully.")
    return conversation_chain

def handle_user_input(user_question):
    logging.info(f"User asked: {user_question}")
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)

        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDF files", page_icon=":books:")

    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None


    st.header("Chat with multiple PDF files :books:")
    user_question = st.text_input("Ask a question about the relevant document:")
    if user_question:
            handle_user_input(user_question)

    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader(
            "Upload you PDF files here and click the submit button",accept_multiple_files=True)
        if st.button("Submit"):
            with st.spinner("Processing"):
                logging.info("Processing PDF files.")

                #get the pdf text 
                raw_text = get_pdf_text(pdf_docs)

                #get the text chunks
                text_chunks = get_text_chunks(raw_text)

                #create vector store
                vectorstore = get_vectorstore(text_chunks)

                st.session_state.conversation = get_conversation_chain(vectorstore)
                logging.info("Conversation chain is ready for interaction.")
 
if __name__=='__main__':
    main()