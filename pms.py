import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("PMS_URL")
API_KEY = os.getenv("PMS_API_KEY")

AUTH = ("apikey", API_KEY)


def get_tasks():
    """
    Get latest time entries
    """
    url = f"{BASE_URL}/api/v3/time_entries?pageSize=100"

    response = requests.get(
        url,
        auth=AUTH
    )

    return response.json()


def get_projects():
    """
    Get projects
    """
    url = f"{BASE_URL}/api/v3/projects?pageSize=100"

    response = requests.get(
        url,
        auth=AUTH
    )

    return response.json()


def get_project_tasks(project_id):
    """
    Get work packages/tasks for a project
    """
    url = f"{BASE_URL}/api/v3/projects/{project_id}/work_packages?pageSize=100"

    response = requests.get(
        url,
        auth=AUTH
    )

    return response.json()


def get_work_packages():
    """
    Get all work packages
    """
    url = f"{BASE_URL}/api/v3/work_packages?pageSize=100"

    response = requests.get(
        url,
        auth=AUTH
    )

    return response.json()


def get_milestones():
    """
    Get milestone work packages
    """
    url = f"{BASE_URL}/api/v3/work_packages?pageSize=100"

    response = requests.get(
        url,
        auth=AUTH
    )

    return response.json()


def get_users():
    """
    Get users
    """
    url = f"{BASE_URL}/api/v3/users?pageSize=100"

    response = requests.get(
        url,
        auth=AUTH
    )

    return response.json()
