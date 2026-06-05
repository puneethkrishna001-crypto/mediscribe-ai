from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

from config import DOCS_PATH
from config import UPLOAD_PATH


class PDFLoader:

    def __init__(self):

        self.default_path = Path(
            DOCS_PATH
        )

        self.upload_path = Path(
            UPLOAD_PATH
        )

    def load_documents(self):

        documents = []

        pdf_files = []

        pdf_files.extend(
            list(
                self.default_path.glob("*.pdf")
            )
        )

        pdf_files.extend(
            list(
                self.upload_path.glob("*.pdf")
            )
        )

        if not pdf_files:

            raise FileNotFoundError(
                "No PDFs found."
            )

        for pdf_file in pdf_files:

            loader = PyPDFLoader(
                str(pdf_file)
            )

            pages = loader.load()

            for page in pages:

                page.metadata[
                    "document_name"
                ] = pdf_file.name

            documents.extend(
                pages
            )

        return documents