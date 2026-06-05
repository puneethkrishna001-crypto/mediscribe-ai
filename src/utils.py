from src.pdf_loader import PDFLoader
from src.chunker import Chunker
from src.vector_store import VectorStore
from src.bm25_retriever import BM25Retriever
from src.hybrid_retriever import HybridRetriever


def build_retrieval_pipeline():

    loader = PDFLoader()

    documents = loader.load_documents()

    chunker = Chunker()

    chunks = chunker.recursive_chunking(
        documents
    )

    vector_store = VectorStore()

    vector_db = vector_store.create(
        chunks
    )

    bm25 = BM25Retriever(
        chunks
    )

    retriever = HybridRetriever(
        vector_db,
        bm25
    )

    return retriever, chunks