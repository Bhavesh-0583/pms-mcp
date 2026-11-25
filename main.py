from fastapi import FastAPI
from pms import get_tasks, get_projects, get_project_tasks
from mcp_server import mcp

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

# Create MCP app
mcp_app = mcp.streamable_http_app()

print("MCP APP =", mcp_app)

# Mount MCP
app.mount("/mcp", mcp_app)

# Print all routes
print("==== ROUTES ====")

for route in app.routes:
    try:
        print(route.path)
    except Exception as e:
        print(e)
