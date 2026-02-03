# app/agent/explainer.py
import os
from typing import Optional

from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
client: Optional[OpenAI] = OpenAI(api_key=api_key) if api_key else None

SYSTEM_PROMPT = """
Ты персональный тренер.
Ты НЕ меняешь рекомендации.
Ты только объясняешь их простым языком.
"""

def explain(state: dict, recommendation: dict) -> str:
    if not client:
        return "LLM отключён: отсутствует API key"

    try:
        resp = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"{state}\n{recommendation}"},
            ],
            temperature=0.4,
        )
        return resp.choices[0].message.content or "Пояснение недоступно"
    except Exception:
        return "Пояснение недоступно из-за ошибки LLM"
