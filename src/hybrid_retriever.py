from collections import defaultdict

from config import TOP_K


class HybridRetriever:

    def __init__(
        self,
        vectorstore,
        bm25_retriever
    ):
        self.vectorstore = vectorstore
        self.bm25_retriever = bm25_retriever

    def reciprocal_rank_fusion(
        self,
        vector_results,
        bm25_results,
        k=60
    ):
        scores = defaultdict(float)

        document_map = {}

        for rank, doc in enumerate(vector_results):

            content = doc.page_content

            scores[content] += (
                1 / (k + rank + 1)
            )

            document_map[content] = doc

        for rank, (doc, _) in enumerate(bm25_results):

            content = doc.page_content

            scores[content] += (
                1 / (k + rank + 1)
            )

            document_map[content] = doc

        ranked_docs = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        final_docs = []

        seen_content = set()

        document_counter = defaultdict(int)

        max_chunks_per_document = 2

        for content, _ in ranked_docs:

            if content in seen_content:
                continue

            doc = document_map[content]

            document_name = doc.metadata.get(
                "document_name",
                "unknown"
            )

            if (
                document_counter[document_name]
                >= max_chunks_per_document
            ):
                continue

            document_counter[
                document_name
            ] += 1

            final_docs.append(doc)

            seen_content.add(content)

            if len(final_docs) >= TOP_K:
                break

        return final_docs

    def retrieve(
        self,
        query
    ):
        vector_results = (
            self.vectorstore
            .similarity_search(
                query,
                k=TOP_K * 3
            )
        )

        bm25_results = (
            self.bm25_retriever
            .search(
                query,
                top_k=TOP_K * 3
            )
        )

        return self.reciprocal_rank_fusion(
            vector_results,
            bm25_results
        )