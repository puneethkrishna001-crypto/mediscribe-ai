from langchain_community.embeddings import HuggingFaceEmbeddings

from config import EMBEDDING_MODEL


class EmbeddingModel:
    def __init__(self):
        self.model = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL,
            model_kwargs={"device": "cpu"}
        )

    def get_model(self):
        return self.model