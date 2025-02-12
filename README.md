# Chatbot_Deepseek_R1
Resume Q&A Chatbot using RAG (LangChain + Ollama + ChromaDB)

📌 Overview

This project implements a Retrieval-Augmented Generation (RAG) pipeline that allows users to ask questions about a resume document and receive intelligent responses based on the document's content. The system efficiently retrieves relevant text chunks from the resume and uses an LLM to generate accurate answers.

🚀 Tech Stack

LangChain (TextLoader, PyPDFLoader, Chroma, FAISS, Retrieval Chain)

Ollama LLM (DeepSeek-R1)

OpenAI/Ollama Embeddings

ChromaDB / FAISS for vector storage

RecursiveCharacterTextSplitter for document chunking

Python & PyPDFLoader for PDF processing

🔥 How It Works

Load and process a PDF resume.

Split the text into chunks for efficient retrieval.

Generate vector embeddings and store them in ChromaDB.

Retrieve the most relevant chunks based on user queries.

Use an LLM (DeepSeek-R1) to generate detailed answers.

🛠 Installation

Ensure you have Python installed, then install the required dependencies:

pip install langchain langchain_community langchain_ollama chromadb faiss-cpu pypdf python-dotenv

⚡ How to Run

Place the resume file (resume.pdf) in the project directory.

Update the script to point to the correct file path.

Run the script:

python main.py

