from fastapi import FastAPI
from pms import get_tasks

app = FastAPI()

@app.get("/")
def home():
    return {"message": "PMS MCP Server Running"}

@app.get("/time_entries")
def time_entries():
    return get_tasks()
