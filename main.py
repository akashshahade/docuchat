import streamlit as st
import os
from ollama_rag import query_ollama, extract_text_from_pdf

# Set page config
st.set_page_config(page_title="DocuChat - Talk to PDFs", layout="wide")

# Title
st.title("📄 DocuChat - Talk to PDFs")

# ✅ Ensure session state variables are initialized
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # Initialize chat history

if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""  # Initialize PDF text storage

# 🔄 Button to Reset System (Clears Old Data)
if st.button("🔄 Reset System (Clear Old Data)"):
    st.session_state.chat_history = []
    st.session_state.pdf_text = ""

    # Fully delete old FAISS vector database
    vector_db_path = "vector_db/faiss_index"
    if os.path.exists(vector_db_path):
        os.system(f"rm -rf {vector_db_path}")  # Linux/Mac
        os.system(f"rmdir /s /q {vector_db_path}")  # Windows

    st.success("✅ System Reset! Upload a new document now.")
    st.experimental_rerun()  # Force refresh

# Upload multiple PDFs
uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    st.success(f"✅ {len(uploaded_files)} PDF(s) Uploaded Successfully!")

    # Combine text from all uploaded PDFs
    combined_text = ""
    for uploaded_file in uploaded_files:
        combined_text += extract_text_from_pdf(uploaded_file) + "\n\n"
    
    st.session_state.pdf_text = combined_text  # Store combined text

    user_question = st.text_input("Ask a question across all PDFs:")

    if st.button("Get Answer"):
        if user_question:
            with st.spinner("Thinking..."):
                response = query_ollama(st.session_state.pdf_text, user_question)  # Pass combined text
            st.session_state.chat_history.insert(0, (user_question, response))  # Insert latest at top

# ✅ Display chat history safely (after ensuring it's initialized)
for question, answer in st.session_state.chat_history:
    st.markdown(f"**Q:** {question}")
    st.success(f"**A:** {answer}")

# Footer - centered at the bottom
st.markdown(
    """
    <div style='position: fixed; bottom: 10px; width: 100%; text-align: center; font-size: 14px; color: grey;'>
        Developed by <b>Akash Shahade</b>
    </div>
    """,
    unsafe_allow_html=True
)
