from mcp.server.fastmcp import FastMCP

from pms import (
    get_tasks,
    get_projects,
    get_project_tasks,
    get_work_packages,
    get_milestones,
    get_users,
    get_projects_count,
    get_work_packages_count,
    get_users_count
)

mcp = FastMCP(
    "PMS",
    host="0.0.0.0"
)

@mcp.tool()
def get_time_entries():
    """
    Get time entries from PMS
    """
    return get_tasks()

@mcp.tool()
def get_projects_list():
    """
    Get projects from PMS
    """
    return get_projects()

@mcp.tool()
def get_project_tasks_list(project_id: int):
    """
    Get tasks/work packages for a project
    """
    return get_project_tasks(project_id)

@mcp.tool()
def get_all_work_packages():
    """
    Get all work packages
    """
    return get_work_packages()

@mcp.tool()
def get_milestones_list():
    """
    Get milestones
    """
    return get_milestones()

@mcp.tool()
def get_users_list():
    """
    Get PMS users
    """
    return get_users()

@mcp.tool()
def project_count():
    projects = get_projects()
    return {
        "total_projects": len(projects)
    }

@mcp.tool()
def projects_count():
    return {
        "total_projects": get_projects_count()
    }

@mcp.tool()
def work_packages_count():
    return {
        "total_work_packages": get_work_packages_count()
    }

@mcp.tool()
def users_count():
    return {
        "total_users": get_users_count()
    }
