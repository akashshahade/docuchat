import ollama
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain_community.embeddings import OllamaEmbeddings
from langchain.vectorstores import FAISS
from PyPDF2 import PdfReader

# Directory for storing FAISS index
DB_FAISS_PATH = "vector_db/faiss_index"

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = "".join([page.extract_text() or "" for page in reader.pages])
    
    # Debugging: Check extracted text
    print("Extracted PDF Text:", text[:1000])  # Print first 1000 characters
    
    if len(text.strip()) == 0:
        raise ValueError("No text extracted from PDF. The file might be an image-based PDF.")

    return text

# Function to create or load a fresh vector database
def create_or_load_vector_db(pdf_text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = [Document(page_content=chunk) for chunk in text_splitter.split_text(pdf_text)]

    embedding_function = OllamaEmbeddings(model="llama3.2:1b")

    # 🔥 Delete FAISS database before creating a new one
    if os.path.exists(DB_FAISS_PATH):
        os.system(f"rm -rf {DB_FAISS_PATH}")  # Linux/Mac
        os.system(f"rmdir /s /q {DB_FAISS_PATH}")  # Windows

    # ✅ Correct FAISS Initialization (Without index_factory)
    vector_db = FAISS.from_documents(docs, embedding_function)
    vector_db.save_local(DB_FAISS_PATH)

    return vector_db

# Function to query Ollama with relevant PDF context
def query_ollama(pdf_text, user_question):
    vector_db = create_or_load_vector_db(pdf_text)

    docs = vector_db.similarity_search(user_question, k=5)  # Retrieve more relevant chunks
    context = "\n\n".join([doc.page_content[:500] for doc in docs])  # Limit chunk size

    prompt = f"""You are an AI assistant that answers questions based on a given PDF. 
    Here is the extracted text from the document:

    {context}

    Now, answer the user's question:

    {user_question}
    """

    response = ollama.chat(
        model="llama3.2:1b", 
        messages=[{"role": "user", "content": prompt}], 
        options={"num_threads": 2}  # Optimize CPU usage
    )

    return response['message']['content']
