from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="EduGenie - AI Learning Assistant", version="1.0.0")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


class TextRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=20000)


class QuizRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=20000)
    count: int = Field(default=3, ge=1, le=10)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.get("/health")
def health():
    return {"status": "ok", "application": "EduGenie"}


@app.post("/qa")
def qa(payload: TextRequest):
    return {"result": answer_question(payload.text)}


@app.post("/explain")
def explain(payload: TextRequest):
    return {"result": explain_topic(payload.text)}


@app.post("/quiz")
def quiz(payload: QuizRequest):
    return {"result": generate_quiz(payload.text, payload.count)}


@app.post("/summarize")
def summarize(payload: TextRequest):
    return {"result": summarize_text(payload.text)}


@app.post("/learn/recommendations")
def learning_recommendations(payload: TextRequest):
    return {"result": get_learning_recommendations(payload.text)}
