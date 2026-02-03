from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
Ты персональный тренер.
Ты НЕ меняешь рекомендации.
Ты только объясняешь их простым языком.
"""

def explain(state: dict, recommendation: dict) -> str:
    prompt = f"""
Состояние спортсмена:
{state}

Рекомендация:
{recommendation}

Кратко объясни решение (3–5 строк).
"""

    resp = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        temperature=0.4,
    )
    return resp.choices[0].message.content
