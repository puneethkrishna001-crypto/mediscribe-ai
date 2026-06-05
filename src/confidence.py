class ConfidenceEstimator:

    @staticmethod
    def calculate(retrieved_docs):

        count = len(
            retrieved_docs
        )

        unique_docs = len(
            {
                doc.metadata.get(
                    "document_name",
                    ""
                )
                for doc in retrieved_docs
            }
        )

        score = (
            count * 5
            +
            unique_docs * 10
        )

        if score >= 70:
            return "High"

        if score >= 40:
            return "Medium"

        return "Low"