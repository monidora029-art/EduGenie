from gemini_client import gemini_generate


def get_learning_recommendations(goal: str) -> str:
    prompt = f"""
Create a personalized learning path for this student goal:

{goal}

Include:
1. Goal
2. Beginner stage
3. Intermediate stage
4. Advanced stage
5. Suggested timeline
6. Practice activities
7. Types of resources to use (do not invent URLs)
8. A final project idea

Keep the plan practical, clear, and beginner-friendly.
"""
    return gemini_generate(prompt)
