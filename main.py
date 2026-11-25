from fastapi import FastAPI
from pms import get_tasks, get_projects, get_project_tasks

app = FastAPI()

@app.get("/")
def home():
    return {"message": "PMS MCP Server Running"}

@app.get("/time_entries")
def time_entries():
    return get_tasks()

@app.get("/projects")
def projects():
    return get_projects()

@app.get("/project_tasks/{project_id}")
def project_tasks(project_id: int):
    return get_project_tasks(project_id)

@app.get("/mcp")
def mcp_check():
    return {
        "name": "PMS MCP",
        "status": "running"
    }
