import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

try:
    OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]
except:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)

st.set_page_config(page_title="Business Report Analyzer", page_icon="📊", layout="wide")
st.title("📊 AI-Powered Business Report Analyzer")
st.markdown("Upload any business report or annual report PDF and extract instant insights.")

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def split_text_into_chunks(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=500)
    return splitter.split_text(text)

def get_answer(context, question):
    prompt = f"""You are a senior business analyst at McKinsey & Company.
Answer the question using the context provided from the business report.
Be specific, structured, and use bullet points where appropriate.
If the answer is not in the context, say "This information is not available in the report."

Context:
{context}

Question:
{question}

Answer:"""
    response = client.chat.completions.create(
        model="openrouter/auto",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

with st.sidebar:
    st.header("📁 Upload Report")
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    if uploaded_file:
        if st.button("🔍 Process Report", use_container_width=True):
            with st.spinner("Reading report..."):
                raw_text = extract_text_from_pdf(uploaded_file)
                if not raw_text.strip():
                    st.error("Could not extract text from this PDF.")
                else:
                    chunks = split_text_into_chunks(raw_text)
                    st.session_state["chunks"] = chunks
                    st.session_state["report_processed"] = True
                    st.session_state["report_name"] = uploaded_file.name
                    st.success("Report processed successfully!")

if st.session_state.get("report_processed"):
    st.markdown(f"**Analyzing:** `{st.session_state['report_name']}`")
    st.divider()
    context = " ".join(st.session_state["chunks"][:3])
    st.subheader("⚡ Auto-Generated Insights")
    if st.button("Generate Key Insights", use_container_width=True):
        questions = [
            "What are the key financial highlights and metrics in this report?",
            "What are the major business risks mentioned in this report?",
            "What are the company's strategic priorities and future plans?",
            "What are the key operational performance metrics?"
        ]
        labels = [
            "💰 Financial Highlights",
            "⚠️ Key Risks",
            "🎯 Strategic Priorities",
            "📈 Operational Metrics"
        ]
        cols = st.columns(2)
        for i, (q, label) in enumerate(zip(questions, labels)):
            with cols[i % 2]:
                with st.spinner(f"Analyzing {label}..."):
                    answer = get_answer(context, q)
                st.markdown(f"### {label}")
                st.markdown(answer)
                st.divider()
    st.subheader("💬 Ask Your Own Question")
    user_question = st.text_input("Type your question about the report")
    if user_question:
        with st.spinner("Thinking..."):
            answer = get_answer(context, user_question)
        st.markdown("### Answer")
        st.markdown(answer)
else:
    st.info("👈 Upload a PDF report from the sidebar and click 'Process Report' to get started.")
    st.markdown("""
    ### What this tool does:
    - 📄 **Extracts** text from any business or annual report PDF
    - 🤖 **Analyzes** it using AI
    - 💡 **Generates** instant insights on financials, risks, strategy
    - 💬 **Answers** any custom question you ask about the report
    """)