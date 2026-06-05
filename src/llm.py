import os

import google.generativeai as genai

from dotenv import load_dotenv

from config import (
    GEMINI_MODEL,
    TEMPERATURE,
    MAX_TOKENS
)

load_dotenv()


class MedicalLLM:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found in .env"
            )

        genai.configure(
            api_key=api_key
        )

        self.model = genai.GenerativeModel(
            model_name=GEMINI_MODEL,
            generation_config={
                "temperature": TEMPERATURE,
                "max_output_tokens": MAX_TOKENS
            }
        )

    def build_prompt(
        self,
        question,
        context,
        chat_history=""
    ):
        return f"""
You are MediScribe AI.

Answer ONLY using the provided medical context.

If the answer cannot be found in the context, say:

'I could not find sufficient information in the uploaded medical documents.'

Conversation History:
{chat_history}

Medical Context:
{context}

Question:
{question}
"""

    def generate_answer(
        self,
        question,
        context,
        chat_history=""
    ):
        prompt = self.build_prompt(
            question,
            context,
            chat_history
        )

        response = self.model.generate_content(
            prompt
        )

        return response.text