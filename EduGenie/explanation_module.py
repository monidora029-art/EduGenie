import os
from functools import lru_cache

from gemini_client import gemini_generate


@lru_cache(maxsize=1)
def get_local_explainer():
    if os.getenv("USE_LOCAL_EXPLAINER", "false").lower() != "true":
        return None

    try:
        from transformers import pipeline
        model_name = os.getenv(
            "LOCAL_EXPLAINER_MODEL", "MBZUAI/LaMini-Flan-T5-783M"
        )
        return pipeline("text2text-generation", model=model_name)
    except Exception:
        return None


def explain_topic(topic: str) -> str:
    local_model = get_local_explainer()

    if local_model is not None:
        prompt = (
            "Explain the following educational topic in very simple English. "
            "Include a definition, how it works, and one example:\n\n"
            f"{topic}"
        )
        try:
            result = local_model(prompt, max_new_tokens=300, do_sample=False)
            if result and "generated_text" in result[0]:
                return result[0]["generated_text"].strip()
        except Exception:
            pass

    prompt = f"""
You are EduGenie, a patient teacher.
Explain this topic for a beginner:

{topic}

Use this structure:
1. Simple definition
2. How it works
3. Easy real-world example
4. Key points to remember

Use simple English and avoid unnecessary jargon.
"""
    return gemini_generate(prompt)
