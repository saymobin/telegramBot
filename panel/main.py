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

@app.post("/api/proxy")
async def save_proxy(proxy: str = Form(default="")):
    set_key(ENV_PATH, "PROXY", proxy)
    return HTMLResponse(status_code=200)

@app.post("/api/date_toggle")
async def save_date_toggle(date_toggle: str = Form(default="off")):
    set_key(ENV_PATH, "DATE_STATUS", date_toggle)
    return HTMLResponse(status_code=200)

@app.post("/api/echo_toggle")
async def save_echo_toggle(echo_toggle: str = Form(default="off")):
    set_key(ENV_PATH, "ECHO_STATUS", echo_toggle)
    return HTMLResponse(status_code=200)