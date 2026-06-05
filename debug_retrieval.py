from src.utils import build_retrieval_pipeline

retriever, chunks = build_retrieval_pipeline()

query = "Compare dengue and malaria"

docs = retriever.retrieve(query)

for i, doc in enumerate(docs, start=1):
    print("\n" + "=" * 50)
    print(f"RESULT {i}")
    print("=" * 50)

    print("Document:",
          doc.metadata.get(
              "document_name",
              "Unknown"
          ))

    print("\nContent Preview:")
    print(doc.page_content[:500])