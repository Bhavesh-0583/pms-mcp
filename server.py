from mcp.server.fastmcp import FastMCP
from pms import get_tasks

mcp = FastMCP("PMS")

@mcp.tool()
def get_time_entries():
    """Get time entries from PMS"""
    return get_tasks()

print("Tool registered: get_time_entries")

if __name__ == "__main__":
    print("Starting PMS MCP Server...")
    mcp.run()
