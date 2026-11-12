RAG PDF Chatbot

Project Overview

RAG PDF Chatbot is a Python-based project that aims to build an AI-powered chatbot capable of answering questions based on the content of uploaded PDF documents.

The project uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from documents and provide context-based answers.

This is my first AI Engineering project. Coming from a Back-End development background with PHP and Laravel, I am exploring AI concepts through practical implementation and step-by-step development.

Project Status

Work in Progress

The project is currently in its initial document-loading stage. Development will continue by implementing document splitting, embeddings, vector storage, and retrieval.

Technology Stack

- Python – Main programming language.
- LangChain – Document processing and RAG workflow.
- PyPDFLoader – Loading and extracting PDF content.
- ChromaDB – Vector database (planned).
- Streamlit – Web interface (planned).

How It Works

The planned RAG pipeline consists of the following steps:

1. Document Loading: Load PDF files and extract their text and metadata.
2. Text Splitting: Divide documents into smaller chunks.
3. Embeddings: Convert text chunks into numerical vector representations.
4. Vector Storage: Store embeddings in ChromaDB.
5. Retrieval: Find the most relevant chunks based on the user's question.
6. Generation: Send the retrieved context and question to an LLM to generate an answer.

Development Roadmap

- [x] Load PDF documents using PyPDFLoader.
- [x] Split documents into smaller chunks.
- [x] Generate embeddings.
- [x] Store embeddings in ChromaDB.
- [ ] Retrieve relevant document chunks.
- [ ] Generate answers using an LLM.
- [ ] Build a Streamlit interface.
- [ ] Add installation instructions and project screenshots.

Learning Goals

Through this project, I aim to understand:

- Retrieval-Augmented Generation (RAG).
- Document loading and processing.
- Text embeddings and semantic search.
- Vector databases.
- LLM integration and context-based generation.

Author

Nourhan Habib