from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from app.users.users import users_router
from app.db.core import init_db


app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router, prefix="/users")

app.mount("/static", StaticFiles(directory="app/src/static"), name="static")
templates = Jinja2Templates(directory="app/src/templates")

@app.get("/")
async def main_page(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})

@app.post("/init_db")
async def create_or_reset_db(request: Request):
    await init_db()
    return JSONResponse({"Status": "Database init succesful"}, status_code=201)