from gemini_client import gemini_generate


def summarize_text(text: str) -> str:
    prompt = f"""
Summarize the following educational text for quick revision.

Requirements:
- Keep the important facts and ideas.
- Remove repetition and unnecessary wording.
- Use simple English.
- Use short headings and bullet points where helpful.
- Do not add information that is not present in the text.

Text:
{text}
"""
    return gemini_generate(prompt)
