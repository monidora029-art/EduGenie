import os
from functools import lru_cache
from dotenv import load_dotenv

load_dotenv()

DEFAULT_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")


@lru_cache(maxsize=1)
def get_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "your_google_ai_studio_api_key_here":
        return None

    try:
        from google import genai
        return genai.Client(api_key=api_key)
    except Exception:
        return None


def gemini_generate(prompt: str) -> str:
    client = get_gemini_client()
    if client is None:
        return (
            "Gemini API is not configured. Add a valid GEMINI_API_KEY to your .env file "
            "and restart the server."
        )

    model = os.getenv("GEMINI_MODEL", DEFAULT_MODEL)
    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
        )
        text = getattr(response, "text", None)
        if text:
            return text.strip()
        return "Gemini returned an empty response."
    except Exception as exc:
        return f"Gemini API error: {exc}"
