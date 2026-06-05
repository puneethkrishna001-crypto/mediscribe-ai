from src.utils import build_retrieval_pipeline

retriever, chunks = build_retrieval_pipeline()

for i in range(5):
    print(chunks[i].metadata)