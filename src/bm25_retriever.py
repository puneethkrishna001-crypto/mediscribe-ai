from rank_bm25 import BM25Okapi


class BM25Retriever:

    def __init__(
        self,
        chunks
    ):
        self.chunks = chunks

        self.corpus = [
            chunk.page_content.lower().split()
            for chunk in chunks
        ]

        self.bm25 = BM25Okapi(
            self.corpus
        )

    def search(
        self,
        query,
        top_k=8
    ):
        query_tokens = (
            query.lower().split()
        )

        scores = self.bm25.get_scores(
            query_tokens
        )

        ranked = sorted(
            zip(
                self.chunks,
                scores
            ),
            key=lambda x: x[1],
            reverse=True
        )

        return ranked[:top_k]