import os

from langchain_community.vectorstores import FAISS

from config import VECTORSTORE_PATH
from src.embeddings import EmbeddingModel


class VectorStore:
    def __init__(self):
        self.embeddings = EmbeddingModel().get_model()

    def create(self, chunks):
        os.makedirs(
            VECTORSTORE_PATH,
            exist_ok=True
        )

        vectorstore = FAISS.from_documents(
            chunks,
            self.embeddings
        )

        vectorstore.save_local(
            VECTORSTORE_PATH
        )

        return vectorstore

    def load(self):
        index_file = os.path.join(
            VECTORSTORE_PATH,
            "index.faiss"
        )

        if not os.path.exists(index_file):
            return None

        return FAISS.load_local(
            VECTORSTORE_PATH,
            self.embeddings,
            allow_dangerous_deserialization=True
        )