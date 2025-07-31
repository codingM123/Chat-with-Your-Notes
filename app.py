import os
import streamlit as st
from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from transformers import pipeline
from utils.pdf_loader import load_pdf_and_split
import tempfile

st.set_page_config(page_title="Chat with Your Notes 📄", layout="centered")
st.title("📄 Chat with your Notes (🤖)")

if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None

uploaded_file = st.file_uploader("📎 Upload your PDF", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    with st.spinner("🔍 Processing your PDF..."):
        # Step 1: Load and split PDF
        documents = load_pdf_and_split(tmp_path)

        # Step 2: SentenceTransformer embeddings
        embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

        # Step 3: Vector DB
        vectorstore = Chroma.from_documents(documents, embedding=embeddings, persist_directory="db")

        # Step 4: HuggingFace QA Pipeline
        hf_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")
        llm = HuggingFacePipeline(pipeline=hf_pipeline)

        # Step 5: RetrievalQA Chain
        retriever = vectorstore.as_retriever()
        qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

        st.session_state.qa_chain = qa_chain
        st.success("✅ PDF processed successfully!")

# Ask question
if st.session_state.qa_chain:
    query = st.text_input("💬 Ask a question from the PDF")
    if query:
        with st.spinner("🤔 Generating answer..."):
            answer = st.session_state.qa_chain.run(query)
            st.write("### 🤖 Answer:")
            st.write(answer)
