import os
import time

import streamlit as st

from src.utils import build_retrieval_pipeline
from src.llm import MedicalLLM
from src.memory import ConversationMemory
from src.confidence import ConfidenceEstimator


st.set_page_config(
    page_title="MediScribe AI",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 MediScribe AI")

st.caption(
    "Retrieval-Augmented Medical Knowledge Assistant powered by Hybrid Search and Gemini 2.5 Flash"
)

if "memory" not in st.session_state:
    st.session_state.memory = ConversationMemory()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "question_count" not in st.session_state:
    st.session_state.question_count = 0

if "avg_response_time" not in st.session_state:
    st.session_state.avg_response_time = []

if "retriever" not in st.session_state:

    with st.spinner(
        "Loading medical knowledge base..."
    ):

        retriever, chunks = (
            build_retrieval_pipeline()
        )

        st.session_state.retriever = retriever
        st.session_state.chunks = chunks

if "llm" not in st.session_state:
    st.session_state.llm = MedicalLLM()

with st.sidebar:

    st.header("📤 Upload PDFs")

    uploaded_files = st.file_uploader(
        "Upload new documents",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        os.makedirs(
            "data/uploaded_docs",
            exist_ok=True
        )

        for file in uploaded_files:

            with open(
                f"data/uploaded_docs/{file.name}",
                "wb"
            ) as f:

                f.write(
                    file.getbuffer()
                )

        st.success(
            "Files uploaded successfully."
        )

        if st.button(
            "Rebuild Knowledge Base"
        ):

            st.session_state.clear()

            st.rerun()

    st.divider()

    st.header("📄 Documents")

    document_names = sorted(
        {
            chunk.metadata.get(
                "document_name",
                "Unknown"
            )
            for chunk in st.session_state.chunks
        }
    )

    for doc in document_names:
        st.write(f"• {doc}")

    st.divider()

    st.header("🤖 Models")

    st.write(
        "LLM: Gemini 2.5 Flash"
    )

    st.write(
        "Embeddings: all-MiniLM-L6-v2"
    )

    st.write(
        "Retriever: FAISS + BM25"
    )

tab1, tab2 = st.tabs(
    [
        "Chat",
        "Analytics"
    ]
)

with tab1:

    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):

            st.markdown(
                message["content"]
            )

    question = st.chat_input(
        "Ask a medical question..."
    )

    if question:

        start_time = time.time()

        st.session_state.question_count += 1

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message(
            "user"
        ):
            st.markdown(
                question
            )

        docs = (
            st.session_state.retriever
            .retrieve(question)
        )

        context = "\n\n".join(
            [
                doc.page_content
                for doc in docs
            ]
        )

        history = (
            st.session_state.memory
            .get_context()
        )

        answer = (
            st.session_state.llm
            .generate_answer(
                question,
                context,
                history
            )
        )

        confidence = (
            ConfidenceEstimator
            .calculate(docs)
        )

        end_time = time.time()

        response_time = round(
            end_time - start_time,
            2
        )

        st.session_state.avg_response_time.append(
            response_time
        )

        st.session_state.memory.add(
            "user",
            question
        )

        st.session_state.memory.add(
            "assistant",
            answer
        )

        sources = []

        seen = set()

        for doc in docs:

            document_name = doc.metadata.get(
                "document_name",
                "Unknown"
            )

            page_number = doc.metadata.get(
                "page",
                0
            )

            source = (
                f"{document_name} "
                f"(Page {page_number + 1})"
            )

            if source not in seen:

                seen.add(
                    source
                )

                sources.append(
                    source
                )

        with st.chat_message(
            "assistant"
        ):

            st.markdown(
                answer
            )

            if confidence == "High":

                st.success(
                    f"Confidence: {confidence}"
                )

            elif confidence == "Medium":

                st.warning(
                    f"Confidence: {confidence}"
                )

            else:

                st.error(
                    f"Confidence: {confidence}"
                )

            st.info(
                f"Response Time: {response_time} sec"
            )

            with st.expander(
                "Sources"
            ):

                for source in sources:

                    st.markdown(
                        f"- {source}"
                    )

            with st.expander(
                "Retrieval Details"
            ):

                st.write(
                    f"Retrieved Chunks: {len(docs)}"
                )

                st.write(
                    "Retrieval Method: Hybrid Search"
                )

                unique_docs = sorted(
                    {
                        doc.metadata.get(
                            "document_name",
                            "Unknown"
                        )
                        for doc in docs
                    }
                )

                for doc_name in unique_docs:

                    st.write(
                        f"• {doc_name}"
                    )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

with tab2:

    st.subheader(
        "Knowledge Base Analytics"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Documents Indexed",
            len(document_names)
        )

        st.metric(
            "Chunks Created",
            len(
                st.session_state.chunks
            )
        )

        st.metric(
            "Questions Asked",
            st.session_state.question_count
        )

    with col2:

        st.metric(
            "Embedding Dimension",
            384
        )

        st.metric(
            "Retriever",
            "Hybrid"
        )

        st.metric(
            "LLM",
            "Gemini 2.5"
        )

    st.divider()

    st.subheader(
        "Performance"
    )

    if st.session_state.avg_response_time:

        avg_time = round(
            sum(
                st.session_state.avg_response_time
            )
            /
            len(
                st.session_state.avg_response_time
            ),
            2
        )

        st.metric(
            "Average Response Time",
            f"{avg_time} sec"
        )

    st.divider()

    st.subheader(
        "Document Coverage"
    )

    document_stats = {}

    for chunk in st.session_state.chunks:

        name = chunk.metadata.get(
            "document_name",
            "Unknown"
        )

        document_stats[name] = (
            document_stats.get(
                name,
                0
            )
            + 1
        )

    for doc, count in sorted(
        document_stats.items()
    ):

        st.write(
            f"{doc}: {count} chunks"
        )

    st.divider()

    st.subheader(
        "System Information"
    )

    st.write(
        "Embedding Model: all-MiniLM-L6-v2"
    )

    st.write(
        "Vector Store: FAISS"
    )

    st.write(
        "Retriever: Hybrid Retrieval (FAISS + BM25)"
    )

    st.write(
        "LLM: Gemini 2.5 Flash"
    )