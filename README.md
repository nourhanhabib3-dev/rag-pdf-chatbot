# RAG PDF Chatbot

I'm building a chatbot that answers questions about a PDF you give it. You upload a document, ask something, and it replies using only what's inside that file instead of guessing.

This is my first AI project. I come from a back-end background (PHP and Laravel), and I'm using it to learn how RAG actually works by building it from scratch.

## Status

Work in progress. I'm adding to it step by step and will update this page as things get done.

## Planned stack

- Python
- LangChain
- Chroma (vector database)
- Streamlit (simple web interface)

## How it will work

1. Load the PDF and split it into small chunks
2. Turn each chunk into an embedding
3. Store the embeddings in Chroma
4. When a question comes in, find the most relevant chunks
5. Send those chunks and the question to the model to get the answer

## Roadmap

- [ ] Load and split a PDF
- [ ] Create embeddings and store them in Chroma
- [ ] Retrieve relevant chunks for a question
- [ ] Generate answers from the retrieved text
- [ ] Build the Streamlit interface
- [ ] Write setup instructions and add screenshots

## Author

Nourhan Habib
