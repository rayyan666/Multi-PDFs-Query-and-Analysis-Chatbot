## Multiple PDFs Doc Query and Exploration Chatbot Project

### Project Overview
#### This project enables users to upload multiple PDF files and engage in a conversational interface to ask questions about the content. It uses PyPDF2 for extracting text, LangChain for text chunking and retrieval, and FAISS for vector-based search. The app integrates Hugging Face models to provide contextually accurate responses. Built with Streamlit, it offers an intuitive interface for seamless document interaction. Perfect for exploring and querying PDF content efficiently.


## Key Features
- **Multi-PDF Support:** Users can upload and query multiple PDF files simultaneously.  
- **Conversational Interface:** Engage in a natural language conversation to ask questions about the document content.  
- **Advanced NLP Techniques:** Utilizes **Hugging Face embeddings** and **FAISS** for efficient text retrieval and similarity search.  
- **Memory Retention:** Implements **ConversationBufferMemory** to maintain chat history for coherent interactions.  
- **User-Friendly UI:** Built with **Streamlit**, offering an intuitive and interactive interface for seamless document exploration.  


## Tech Stack
- **Frameworks/Libraries:**  
  - **Streamlit** for the web interface.  
  - **LangChain** for text chunking, retrieval, and conversational chains.  
  - **FAISS** for vector-based similarity search.  
  - **Hugging Face Transformers** for embeddings and language models (e.g., `google/flan-t5-large`).  
  - **PyPDF2** for text extraction from PDFs.  
- **Other Tools:**  
  - **Python-dotenv** for environment variable management.  
  - **Logging** for tracking application events.  


## How It Works
1. **Text Extraction:**  
   - PDFs are processed using **PyPDF2** to extract raw text.  
2. **Text Chunking:**  
   - The extracted text is split into smaller chunks using **LangChain's CharacterTextSplitter**.  
3. **Vector Embeddings:**  
   - Text chunks are converted into embeddings using **Hugging Face's sentence-transformers/all-MiniLM-L6-v2** model.  
4. **Vector Storage:**  
   - Embeddings are stored in a **FAISS vector store** for efficient similarity search.  
5. **Conversational Chain:**  
   - A **ConversationalRetrievalChain** is created using **Hugging Face's google/flan-t5-large** model for generating context-aware responses.  
6. **User Interaction:**  
   - Users can ask questions, and the chatbot retrieves relevant information from the PDFs using the vector store and conversational chain.  

## Getting Started

To get this project up and running on your local machine, clone the repository and install the required dependencies and have an .env file with your api credentials:

```bash
git clone https://github.com/rayyan666/Multi-PDFs-Query-and-Analysis-Chatbot.git
cd Multi-PDFs-Query-and-Analysis-Chatbot
pip install -r requirements.txt
streamlit run app.py

## Future Enhancements
- **Support for additional file formats:**  
  Add compatibility for DOCX, TXT, and other document formats.  
- **Integration with OpenAI's GPT models:**  
  Enhance response quality by integrating GPT-3.5 or GPT-4.  
- **Deployment to a cloud platform:**  
  Deploy the app on platforms like Streamlit Cloud, AWS, or Heroku for wider accessibility.  
- **Improved UI/UX:**  
  Add more customization options, themes, and a better user interface.  