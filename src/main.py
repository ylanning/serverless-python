from fastapi import FastAPIfrom src.env import configMODE= config("MODE", cast=str, default="Testing")app = FastAPI()@app.get("/")def home_page():    return {                "message": "Welcome to the home page",                "mode": MODE            }  # JSON-ready dictionary