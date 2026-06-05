# 🏥 MediScribe AI

<div align="center">

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://github.com/puneethkrishna001-crypto/mediscribe-ai)
[![Open Source](https://img.shields.io/badge/open%20source-❤️-red.svg)](https://github.com/puneethkrishna001-crypto/mediscribe-ai)

**Retrieval-Augmented Medical Knowledge Assistant powered by Hybrid Search and Gemini 2.5 Flash**

A cutting-edge medical document intelligence platform that leverages advanced retrieval-augmented generation (RAG), hybrid search capabilities, and state-of-the-art language models to provide accurate, context-aware medical information extraction and Q&A.

[Features](#-features) • [Quick Start](#-quick-start) • [Architecture](#-architecture) • [Configuration](#-configuration) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [✨ Features](#-features)
- [🚀 Quick Start](#-quick-start)
- [📁 Project Structure](#-project-structure)
- [🏗️ Architecture](#-architecture)
- [⚙️ Configuration](#-configuration)
- [🖼️ Screenshots](#-screenshots)
- [📊 Performance](#-performance)
- [🔧 API Reference](#-api-reference)
- [📚 Technologies](#-technologies)
- [🤝 Contributing](#-contributing)
- [📝 License](#-license)

---

## 🎯 Overview

**MediScribe AI** is an intelligent medical document processing platform designed to revolutionize how healthcare professionals and researchers interact with medical documentation. By combining advanced information retrieval techniques with state-of-the-art language models, it enables:

- **Semantic Understanding**: Extract meaningful information from complex medical documents
- **Context-Aware Responses**: Leverage conversation history for coherent Q&A interactions
- **Source Attribution**: Track and display which documents contributed to each response
- **Confidence Scoring**: Understand the reliability of retrieved information
- **Real-time Analytics**: Monitor system performance and knowledge base utilization

### Use Cases

✅ **Clinical Research** - Quickly find relevant studies and medical references  
✅ **Patient Education** - Generate accurate medical explanations from authoritative sources  
✅ **Literature Review** - Efficiently search through extensive medical documents  
✅ **Decision Support** - Get evidence-based recommendations from medical literature  
✅ **Regulatory Compliance** - Maintain audit trails with source documentation  

---

## ✨ Features

### 🔍 Hybrid Retrieval System
- **FAISS Vector Search**: Fast similarity-based document retrieval using embeddings
- **BM25 Lexical Search**: Traditional keyword-based retrieval for exact matches
- **Intelligent Fusion**: Combines both methods for optimal recall and precision

### 🤖 Advanced LLM Integration
- **Gemini 2.5 Flash**: Latest Google's multimodal language model
- **Temperature Control**: Adjustable response creativity (0.3 for medical accuracy)
- **Token Optimization**: Configurable output length for different use cases

### 💾 Knowledge Management
- **PDF Processing**: Automatically extract and index PDF medical documents
- **Dynamic Knowledge Base**: Upload and rebuild knowledge base on-the-fly
- **Document Tracking**: Monitor indexed documents and chunk coverage
- **Metadata Preservation**: Maintain document source and page information

### 🧠 Conversation Intelligence
- **Multi-turn Memory**: Maintain conversation context across multiple interactions
- **Smart Context Window**: Efficiently manage conversation history
- **Response Attribution**: Show sources for every answer with page references

### 📊 Monitoring & Analytics
- **Real-time Metrics**: Track questions asked, response times, and confidence scores
- **Performance Dashboard**: Monitor system health and knowledge base statistics
- **Retrieval Debugging**: Inspect which documents contributed to answers
- **Coverage Analysis**: Understand knowledge base utilization by document

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+**
- **Gemini API Key** ([Get one here](https://ai.google.dev/))
- **pip** or **conda** for package management
- **4GB+ RAM** (8GB recommended for optimal performance)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/puneethkrishna001-crypto/mediscribe-ai.git
   cd mediscribe-ai
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your GEMINI_API_KEY
   ```

5. **Prepare your medical documents**
   ```bash
   mkdir -p data/medical_docs
   # Place your PDF files in data/medical_docs/
   ```

6. **Launch the application**
   ```bash
   streamlit run app.py
   ```

   The app will be available at `http://localhost:8501`

### Your First Query

1. Open the application in your browser
2. Upload medical PDF documents using the sidebar
3. Click "Rebuild Knowledge Base" to index your documents
4. Ask your first question: *"What are the symptoms of hypertension?"*
5. View the response along with source attribution and confidence scores

---

## 📁 Project Structure

```
mediscribe-ai/
├── app.py                          # Main Streamlit application
├── config.py                       # Configuration parameters
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variables template
│
├── src/
│   ├── __init__.py
│   ├── utils.py                   # Retrieval pipeline builder
│   ├── llm.py                     # Medical LLM wrapper
│   ├── memory.py                  # Conversation memory manager
│   └── confidence.py              # Confidence estimation
│
├── data/
│   ├── medical_docs/              # Default medical documents
│   └── uploaded_docs/             # User-uploaded documents
│
├── vectorstore/                   # FAISS vector store
├── notebook/                      # Jupyter notebooks for exploration
├── evaluation/                    # Evaluation scripts and metrics
├── assets/
│   └── screenshots/               # Application screenshots
│
└── test_*.py                      # Testing utilities
```

---

## 🏗️ Architecture

### System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    Streamlit UI Layer                        │
│  (Chat Interface, Analytics Dashboard, Document Upload)    │
└────────────────┬────────────────────────────────────────────┘
                 │
    ┌────────────┴───────────────┐
    │                            │
┌───▼──────────────────┐   ┌────▼──────────────────────┐
│  Query Processing    │   │  Knowledge Base Manager   │
│  - Input validation  │   │  - PDF ingestion         │
│  - Query expansion   │   │  - Document chunking     │
└───┬──────────────────┘   │  - Metadata tracking     │
    │                      └────┬──────────────────────┘
    │                           │
    │        ┌──────────────────┴──────────────┐
    │        │                                 │
┌───▼────────▼──────────────────┐    ┌────────▼─────────────┐
│  Hybrid Retrieval System       │    │  Embedding Engine    │
│                                │    │                      │
│  ├─ FAISS Vector Store         │    │  Model:              │
│  │  (Dense Retrieval)          │    │  all-MiniLM-L6-v2   │
│  │                             │    │                      │
│  └─ BM25 Index                 │    │  Dimension: 384      │
│     (Sparse Retrieval)         │    │                      │
└───────────┬────────────────────┘    └────────────────────┘
            │
            │ Retrieved Context
            │
┌───────────▼──────────────────────────────────────┐
│          LLM Processing Chain                    │
│                                                   │
│  ├─ Context Builder                             │
│  │  (Merge retrieval + conversation history)    │
│  │                                               │
│  └─ Gemini 2.5 Flash                            │
│     (Generate medically accurate responses)     │
└───────────┬──────────────────────────────────────┘
            │
            ├─ Answer Generation
            ├─ Confidence Estimation
            ├─ Source Attribution
            └─ Performance Metrics
            │
            ▼
┌─────────────────────────────────────┐
│    Response + Metadata              │
│  - Answer text                      │
│  - Source documents                 │
│  - Confidence score                 │
│  - Response time                    │
│  - Retrieved chunks info            │
└─────────────────────────────────────┘
```

### Data Flow

```
User Query
    ↓
[Query Embedding] (all-MiniLM-L6-v2)
    ↓
    ├─→ [FAISS Dense Search] → Top-K similar vectors
    │                             ↓
    └─→ [BM25 Sparse Search] → Top-K keyword matches
                                  ↓
                        [Hybrid Fusion/Ranking]
                                  ↓
                        [Retrieve Documents]
                                  ↓
                    [Context + Conversation History]
                                  ↓
                         [Gemini 2.5 Flash LLM]
                                  ↓
                    [Generate Answer + Attribution]
                                  ↓
                    [Calculate Confidence Score]
                                  ↓
                        [Return to User]
```

---

## 🖼️ Screenshots

### Chat Interface - Interactive Q&A
![Chat Interface](assets/screenshots/Screenshot%202026-06-05%20111048.png)
*Real-time medical Q&A with streaming responses, confidence badges, and source attribution. The chat interface displays user queries and AI responses with detailed metrics.*

### Analytics Dashboard - Performance Metrics
![Analytics Dashboard](assets/screenshots/Screenshot%202026-06-05%20111102.png)
*Comprehensive analytics showing knowledge base statistics, document coverage, system performance metrics, and real-time usage analytics. Monitor your medical knowledge base health at a glance.*

### Document Management - Upload & Index
![Document Upload](assets/screenshots/Screenshot%202026-06-05%20111121.png)
*Sidebar interface for uploading PDF documents, viewing indexed documents, and rebuilding the knowledge base. Supports batch uploads and dynamic knowledge base expansion.*

### Response Details - Sources & Confidence
![Response Details](assets/screenshots/Screenshot%202026-06-05%20111132.png)
*Detailed response breakdown showing retrieved document sources, page references, confidence scores, retrieval metadata, and performance metrics. Full transparency into how answers are generated.*

---

## ⚙️ Configuration

All configuration is managed through `config.py`:

```python
# Document Processing
DOCS_PATH = "data/medical_docs"           # Path to medical documents
UPLOAD_PATH = "data/uploaded_docs"        # Path for user uploads
CHUNK_SIZE = 500                          # Characters per chunk
CHUNK_OVERLAP = 50                        # Overlap between chunks (context preservation)

# Vector Store
VECTORSTORE_PATH = "vectorstore"          # FAISS vector store location
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"  # Embedding model
TOP_K = 8                                 # Number of documents to retrieve

# LLM Settings
GEMINI_MODEL = "gemini-2.5-flash"         # Google's latest model
TEMPERATURE = 0.3                        # Lower = more deterministic (medical accuracy)
MAX_TOKENS = 1024                         # Maximum response length

# Evaluation
EVAL_TOP_K = 3                            # Top-K for evaluation metrics
```

### Environment Variables

Create a `.env` file in the root directory:

```env
# Google Gemini API
GOOGLE_API_KEY=your_gemini_api_key_here

# Optional: Custom paths
DATA_PATH=data
VECTORSTORE_PATH=vectorstore

# Optional: Model settings
CHUNK_SIZE=500
TOP_K=8
TEMPERATURE=0.3
```

### Advanced Configuration

**For production deployments:**

1. **Increase CHUNK_SIZE** for longer documents (e.g., 1000)
2. **Increase TOP_K** for more comprehensive retrieval (e.g., 16)
3. **Decrease TEMPERATURE** for more consistent outputs (e.g., 0.1)
4. **Enable caching** in `app.py` for faster reloads

---

## 📊 Performance

### Metrics Tracking

The application tracks:

| Metric | Description |
|--------|-------------|
| **Avg Response Time** | Time to retrieve and generate answer |
| **Questions Asked** | Total number of queries processed |
| **Documents Indexed** | Number of medical documents in knowledge base |
| **Chunks Created** | Total text segments for retrieval |
| **Retrieval Success** | Proportion of queries with relevant results |

### Optimization Tips

1. **Vector Store Indexing**: FAISS indexes are cached for fast retrieval (~50ms per query)
2. **Batch Processing**: Upload multiple documents at once for efficiency
3. **Query Optimization**: Be specific in medical queries for better results
4. **Conversation Memory**: System maintains 10-turn conversation history by default

---

## 🔧 API Reference

### Core Modules

#### `src.utils.build_retrieval_pipeline()`
Builds the hybrid retrieval system combining FAISS and BM25.

```python
retriever, chunks = build_retrieval_pipeline()
docs = retriever.retrieve("query text")
```

#### `src.llm.MedicalLLM.generate_answer()`
Generates medical answers using context and conversation history.

```python
llm = MedicalLLM()
answer = llm.generate_answer(question, context, history)
```

#### `src.memory.ConversationMemory`
Manages conversation history across turns.

```python
memory = ConversationMemory()
memory.add("user", "What is hypertension?")
memory.add("assistant", "Hypertension is...")
history = memory.get_context()
```

#### `src.confidence.ConfidenceEstimator.calculate()`
Estimates confidence in retrieved results.

```python
confidence = ConfidenceEstimator.calculate(retrieved_docs)
# Returns: "High", "Medium", or "Low"
```

---

## 📚 Technologies

### Core Technologies

| Component | Technology | Version |
|-----------|-----------|---------|
| **LLM** | Google Gemini 2.5 Flash | Latest |
| **Embeddings** | Sentence Transformers | 3.0.1 |
| **Vector Store** | FAISS (CPU) | 1.8.0 |
| **Sparse Retrieval** | BM25 | 0.2.2 |
| **Framework** | LangChain | 0.2.16 |
| **UI** | Streamlit | 1.38.0 |
| **NLP** | spaCy | 3.7.5 |

### Key Dependencies

```
langchain==0.2.16                      # RAG orchestration
langchain-community==0.2.16            # Extended integrations
langchain-google-genai==1.0.10         # Gemini integration
sentence-transformers==3.0.1           # Embeddings
faiss-cpu==1.8.0                       # Vector search
pypdf==4.3.1                          # PDF processing
streamlit==1.38.0                     # Web UI
rank-bm25==0.2.2                      # Keyword search
spacy==3.7.5                          # NLP processing
numpy==1.26.4                         # Numerical computing
pandas==2.2.2                         # Data manipulation
```

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/mediscribe-ai.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow PEP 8 style guide
   - Add docstrings to functions
   - Update relevant documentation

4. **Test your changes**
   ```bash
   python test_env.py
   python test_gemini.py
   ```

5. **Commit and push**
   ```bash
   git commit -m "Add: Your feature description"
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**
   - Describe your changes
   - Reference related issues
   - Add test cases if applicable

### Areas for Contribution

- 🐛 **Bug Fixes**: Report and fix issues
- ✨ **Features**: Add new retrieval methods or LLM integrations
- 📚 **Documentation**: Improve guides and examples
- 🧪 **Tests**: Expand test coverage
- 🎨 **UI/UX**: Enhance Streamlit interface
- 📊 **Evaluation**: Improve metrics and benchmarking

### Development Setup

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/

# Format code
black .

# Lint
flake8 .
```

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙋 Support & Contact

- **Issues**: [GitHub Issues](https://github.com/puneethkrishna001-crypto/mediscribe-ai/issues)
- **Discussions**: [GitHub Discussions](https://github.com/puneethkrishna001-crypto/mediscribe-ai/discussions)
- **Author**: [@puneethkrishna001-crypto](https://github.com/puneethkrishna001-crypto)

---

## 📖 Citation

If you use MediScribe AI in your research, please cite:

```bibtex
@software{mediscribe_ai_2024,
  title={MediScribe AI: Medical Document Intelligence Platform},
  author={Krishna, Puneeth},
  year={2024},
  url={https://github.com/puneethkrishna001-crypto/mediscribe-ai}
}
```

---

## 🌟 Acknowledgments

- Google for Gemini 2.5 Flash API
- HuggingFace for Sentence Transformers
- Facebook Research for FAISS
- Streamlit team for the amazing web framework
- LangChain community for RAG orchestration tools

---

<div align="center">

**Made with ❤️ for the medical AI community**

[⬆ Back to Top](#-mediscribe-ai)

</div>
