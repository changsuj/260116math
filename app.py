import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import tempfile
import os

# ===== 페이지 설정 =====
st.set_page_config(
    page_title="PDF 챗봇",
    page_icon="📚",
    layout="centered"
)

# ===== 커스텀 CSS =====
st.markdown("""
<style>
    .stChat {
        border-radius: 10px;
    }
    .main-header {
        text-align: center;
        padding: 1rem 0;
        border-bottom: 2px solid #f0f2f6;
        margin-bottom: 2rem;
    }
    .chat-container {
        max-width: 800px;
        margin: 0 auto;
    }
    [data-testid="stChatMessage"] {
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# ===== 헤더 =====
st.markdown('<div class="main-header">', unsafe_allow_html=True)
st.title("📚 PDF 문서 기반 AI 챗봇")
st.caption("test.pdf 문서의 내용을 기반으로 질문에 답변합니다.")
st.markdown('</div>', unsafe_allow_html=True)

# ===== API Key 설정 =====
try:
    GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]
except KeyError:
    st.error("⚠️ API Key가 설정되지 않았습니다. `.streamlit/secrets.toml` 파일을 확인하세요.")
    st.stop()

# ===== 세션 상태 초기화 =====
if "messages" not in st.session_state:
    st.session_state.messages = []

if
