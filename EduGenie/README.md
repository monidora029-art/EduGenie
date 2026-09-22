# EduGenie: Google Gemini Powered Learning Assistant

EduGenie is an AI-powered educational assistant built with FastAPI, HTML/CSS/JavaScript, and Google Gemini. It supports question answering, simple concept explanations, quiz generation, summarization, and personalized learning paths.

## Features

- Ask academic questions
- Explain difficult topics in simple English
- Generate multiple-choice quizzes
- Summarize study material
- Create beginner-to-advanced learning paths
- Responsive web interface
- Health-check API
- Optional local LaMini-Flan-T5 explainer

## Project Structure

```text
EduGenie/
├── main.py
├── gemini_client.py
├── qna.py
├── explanation_module.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── requirements-local.txt
├── .env.example
├── .env
├── .gitignore
├── README.md
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── tests/
    ├── __init__.py
    └── test_api.py
```

## 1. Open the project

Open the `EduGenie` folder in VS Code.

## 2. Create a virtual environment

### PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### Command Prompt

```cmd
python -m venv .venv
.venv\Scripts\activate
```

## 3. Install packages

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 4. Configure Gemini

Open `.env` and replace the placeholder with your Google AI Studio API key:

```env
GEMINI_API_KEY=YOUR_REAL_API_KEY
GEMINI_MODEL=gemini-2.5-flash
USE_LOCAL_EXPLAINER=false
LOCAL_EXPLAINER_MODEL=MBZUAI/LaMini-Flan-T5-783M
```

Do not upload `.env` to GitHub.

## 5. Start the server

```powershell
uvicorn main:app --reload
```

Open:

- Website: http://127.0.0.1:8000
- API documentation: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Web interface |
| GET | `/health` | Health check |
| POST | `/qa` | Answer a question |
| POST | `/explain` | Explain a topic |
| POST | `/quiz` | Generate MCQs |
| POST | `/summarize` | Summarize text |
| POST | `/learn/recommendations` | Create a learning path |

## Optional local explanation model

The project can use LaMini-Flan-T5 for the explanation module. This is optional and may require significant disk space and memory.

```powershell
pip install -r requirements-local.txt
```

Then set:

```env
USE_LOCAL_EXPLAINER=true
```

Restart the server after changing `.env`.

## Troubleshooting

### `ModuleNotFoundError`

Make sure the virtual environment is active and run:

```powershell
pip install -r requirements.txt
```

### PowerShell blocks activation

Use Command Prompt and run:

```cmd
.venv\Scripts\activate
```

### Gemini API error

Check that `GEMINI_API_KEY` is valid, the API is enabled for the key, and `GEMINI_MODEL` is an available model for your API account.

### Port already in use

Run another port:

```powershell
uvicorn main:app --reload --port 8001
```

Then open `http://127.0.0.1:8001`.

## Testing

Install pytest if needed:

```powershell
pip install pytest
```

Run:

```powershell
pytest
```

## Important

The API key belongs in `.env` only. The included `.gitignore` prevents `.env` from being committed to Git.
