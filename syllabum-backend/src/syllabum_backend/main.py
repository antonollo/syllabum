from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db.connect_db import engine
from sqlmodel import SQLModel
from dotenv import load_dotenv
from os import getenv

load_dotenv()

CORS_ORIGIN = getenv("CORS_ORIGIN")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=([CORS_ORIGIN] if CORS_ORIGIN else []),
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


@app.get("/")
def main():
    return {"Hello": "World"}
