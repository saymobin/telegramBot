from pathlib import Path
from dotenv import set_key

from fastapi import FastAPI,Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

ENV_PATH = Path(__file__).parent.parent / ".env"

@app.get("/", response_class=HTMLResponse)
async def render_dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="panel.html",
    )
    
@app.post("/api/token")
async def save_token(token: str = Form(default="")):
    set_key(ENV_PATH, "BOT_TOKEN1", token)
    return HTMLResponse(status_code=200)