from mcp.server.fastmcp import FastMCP
from pms import get_tasks, get_projects

mcp = FastMCP("PMS")

@mcp.tool()
def get_time_entries():
    return get_tasks()

@mcp.tool()
def get_projects_list():
    return get_projects()