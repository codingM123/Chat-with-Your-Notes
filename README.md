# 📄 Chat with Your Notes — AI PDF Chatbot (LangChain + ChromaDB + HuggingFace Transformers)

Empower your documents with conversational AI. Upload a PDF, ask questions, and get accurate, context-aware answers using cutting-edge AI models.

---

## 🚀 Tech Stack (FANG-level & Industry Ready)

| Layer             | Tech Used                              | Purpose                                      |
|------------------|----------------------------------------|----------------------------------------------|
| LLM Backend      | [HuggingFace Transformers](https://huggingface.co/) | Replace OpenAI with open-source/fine-tuned LLMs |
| Vector DB        | [ChromaDB](https://www.trychroma.com/) | Store and retrieve document embeddings       |
| Embeddings       | `sentence-transformers` (e.g., all-MiniLM) | Lightweight, fast embeddings (384-dim)      |
| App Framework    | [Streamlit](https://streamlit.io/)     | Interactive frontend                         |
| PDF Processing   | `PyPDF2`, `langchain.document_loaders` | Load and parse PDFs                          |
| Env Management   | `python-dotenv`                        | API keys & secrets handling                  |
| Memory Persist   | `ChromaDB persist_directory`           | Retain vectorstore across sessions           |

---

## 💡 Features

- 🧠 Chat with *any* uploaded PDF (notes, resumes, reports, research papers)
- 📎 PDF processed using smart chunking for better QA context
- 🔎 Semantic Search with ChromaDB (FAISS optional)
- ⚡ Uses HuggingFace LLMs for inference (Free tier ready)
- 🔐 Secure API token management with `.env`
- 🎯 Modular code (`utils/`, `helper.py`) for extensibility

---

## 📁 Project Structure

```
chat-with-your-notes/
├── app.py                  # Streamlit app logic
├── helper.py              # Any helper functions
├── utils/
│   └── pdf_loader.py      # Loads and splits PDFs
├── requirements.txt       # All dependencies
├── .env                   # Your HuggingFace token (DO NOT UPLOAD)
├── README.md
└── LICENSE
```

---

## ⚙️ Setup Instructions

```bash
1. Clone the repo
https://github.com/your-username/chat-with-your-notes.git
cd chat-with-your-notes

# 2. (Optional but Recommended) Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your HuggingFace token
echo "HUGGINGFACEHUB_API_TOKEN=your-token-here" > .env

# 5. Run the app
streamlit run app.py
```

---

## 🧪 Test It With:
Upload a PDF like:
- ✅ Academic notes
- ✅ Resumes
- ✅ Government reports
- ✅ Technical documentation

Ask questions like:
- "What is the eligibility criteria mentioned?"
- "Summarize key points from this resume."
- "What are the findings in section 3?"

---

## 🌍 Future Additions (Upcoming Tech Integration)
- 🔗 RAG (Retrieval Augmented Generation) with LlamaIndex
- 🤖 Self-hosted LLMs via Ollama / vLLM
- 🧠 Multi-PDF querying
- 🪢 API mode for chatbot integration with WhatsApp or Telegram
- 🛡️ Role-based access for multi-user environments

---

## 🙌 Credits
- [LangChain](https://github.com/hwchase17/langchain)
- [HuggingFace](https://huggingface.co/)
- [Streamlit](https://streamlit.io/)

---

## 🛑 Disclaimer
This tool is built for learning, experimentation, and personal document analysis. Do **not** use it for sensitive, legal, or confidential documents in production without adding proper authentication and data protection.

---

