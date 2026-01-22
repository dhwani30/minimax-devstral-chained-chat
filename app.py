from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from planner_model import run_planner
from dev_model import run_developer

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    prompt = body.get("prompt", "").strip()

    planner_output = run_planner(prompt)
    developer_output = run_developer(planner_output)

    return JSONResponse(
        content={
            "planner": planner_output,
            "developer": developer_output
        },
        headers={"Cache-Control": "no-store"}
    )
