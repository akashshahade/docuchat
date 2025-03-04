✅ README.md for DocuChat
md
Copy
Edit
# 📄 DocuChat - Talk to PDFs

### **Chat with multiple PDFs using AI-powered Retrieval-Augmented Generation (RAG) and Ollama's local LLaMA model.**
---

## 🚀 **Overview**
DocuChat is a **Streamlit-based AI chatbot** that allows users to **upload multiple PDFs** and ask questions about their content. The system uses **LangChain**, **FAISS**, and **Ollama** to process the PDFs and generate responses based on the extracted data.

- ✅ **Supports multiple PDFs** – Upload and chat across multiple documents.
- ✅ **Works Offline** – Uses **Ollama** with a **local LLaMA model**, no API key required.
- ✅ **Fast and Efficient** – Uses **FAISS** for quick document search.
- ✅ **Easy to Use** – Simple **Streamlit UI** with a **one-click reset button**.
- ✅ **Secure** – No cloud processing, everything runs on your machine.

---

## 🛠️ **Tech Stack**
- **Frontend**: Streamlit  
- **Backend**: LangChain, FAISS, Ollama  
- **AI Model**: LLaMA 3.2 1B (runs locally via Ollama)  
- **PDF Processing**: PyPDF  

---

## 🔧 **Installation Guide**
### **1️⃣ Prerequisites**
Make sure you have the following installed:
- **Python 3.9+** – [Download here](https://www.python.org/downloads/)
- **Git** – [Download here](https://git-scm.com/downloads)
- **Ollama** – [Install from here](https://ollama.com/)

### **2️⃣ Clone the Repository**
Open **Terminal/Command Prompt** and run:
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/docuchat.git
cd docuchat
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Download the AI Model
Run this command to download the LLaMA 3.2 1B model:

bash
Copy
Edit
ollama pull llama3.2:1b
🚀 How to Run the App
Run the following command in your project directory:

bash
Copy
Edit
streamlit run main.py
This will open the DocuChat web app in your browser.

📂 Project Structure
bash
Copy
Edit
docuchat/
│── main.py         # Streamlit UI
│── ollama_rag.py   # RAG processing backend
│── requirements.txt # Required Python packages
│── README.md       # Project documentation
│── vector_db/      # FAISS index (auto-generated)
🖥️ Usage
1️⃣ Upload PDFs
Click on "Upload PDF files" and select multiple PDFs.
2️⃣ Ask Questions
Type your question in the chatbox and hit "Get Answer".
3️⃣ Reset for New Documents
Click "🔄 Reset System" before uploading new PDFs to clear old data.
🛠 Customization
Modify the AI Model
If you want to use a different LLaMA model, change this line in ollama_rag.py:

python
Copy
Edit
embedding_function = OllamaEmbeddings(model="llama3.2:1b")
You can replace "llama3.2:1b" with other models like "mistral".

Change FAISS Retrieval Depth
To increase/decrease the number of document chunks retrieved, update:

python
Copy
Edit
docs = vector_db.similarity_search(user_question, k=5)
Higher k means more context but slower responses.
Lower k means faster responses but less context.
🛠 Troubleshooting
1️⃣ Error: Model Not Found
If you see:

bash
Copy
Edit
{"error":"model \"llama3.2:1b\" not found, try pulling it first"}
Run:

bash
Copy
Edit
ollama pull llama3.2:1b
2️⃣ Error: FAISS Index Not Updating
If old answers appear even after new PDFs, reset the FAISS index:

bash
Copy
Edit
rm -rf vector_db/  # Mac/Linux
rmdir /s /q vector_db  # Windows
Then restart the app.

🤝 Contributing
If you'd like to improve DocuChat, follow these steps:

Fork the repository on GitHub.
Clone it to your local machine:
bash
Copy
Edit
git clone https://github.com/YOUR_GITHUB_USERNAME/docuchat.git
Create a new branch:
bash
Copy
Edit
git checkout -b feature-yourfeature
Commit and push your changes:
bash
Copy
Edit
git add .
git commit -m "Added new feature"
git push origin feature-yourfeature
Submit a Pull Request on GitHub.
🎯 Future Improvements
✅ Add support for Word and Excel files
✅ Integrate voice input for questions
✅ Enable document summarization feature

📜 License
This project is open-source and licensed under the MIT License.

📢 Support
For any issues, feel free to open an issue in the GitHub repository or contact me.

🎉 Enjoy DocuChat! 🚀
