from fastapi import FastAPI
from pms import get_tasks, get_projects, get_project_tasks
from mcp_server import mcp

app = FastAPI()

# Existing APIs
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

# MCP Mount
app.mount("/mcp", mcp.streamable_http_app())
