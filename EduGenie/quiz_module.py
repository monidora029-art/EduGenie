import json
import re

from gemini_client import gemini_generate


def _clean_json_block(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```$", "", text)
    start = text.find("[")
    end = text.rfind("]")
    if start != -1 and end != -1 and end > start:
        return text[start : end + 1]
    return text


def generate_quiz(passage: str, count: int = 3):
    prompt = f"""
Create exactly {count} multiple-choice questions from the educational content below.
Return ONLY valid JSON as an array. Do not add markdown or extra text.
Each item must contain:
- question: string
- options: exactly 4 strings
- answer: exactly one option string from options
- explanation: short explanation

Content:
{passage}
"""

    raw = gemini_generate(prompt)

    try:
        data = json.loads(_clean_json_block(raw))
        if not isinstance(data, list):
            raise ValueError("Quiz response is not a JSON array.")

        normalized = []
        for item in data[:count]:
            if not isinstance(item, dict):
                continue
            question = str(item.get("question", "")).strip()
            options = item.get("options", [])
            answer = str(item.get("answer", "")).strip()
            explanation = str(item.get("explanation", "")).strip()

            if not question or not isinstance(options, list) or len(options) != 4:
                continue
            options = [str(option).strip() for option in options]
            if answer not in options:
                continue

            normalized.append(
                {
                    "question": question,
                    "options": options,
                    "answer": answer,
                    "explanation": explanation,
                }
            )

        if not normalized:
            raise ValueError("No valid quiz questions were returned.")
        return normalized

    except Exception as exc:
        return {
            "error": "Could not create the quiz in the expected format.",
            "details": str(exc),
            "raw": raw,
        }
