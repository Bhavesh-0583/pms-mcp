import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("PMS_URL")
API_KEY = os.getenv("PMS_API_KEY")

AUTH = ("apikey", API_KEY)


def get_all_pages(endpoint):
    all_items = []
    offset = 1

    while True:
        url = f"{BASE_URL}{endpoint}?pageSize=100&offset={offset}"

        response = requests.get(
            url,
            auth=AUTH
        )

        data = response.json()

        items = data.get("_embedded", {}).get("elements", [])

        if not items:
            break

        all_items.extend(items)

        if len(items) < 100:
            break

        offset += 100

    return all_items


def get_tasks():
    return get_all_pages("/api/v3/time_entries")


def get_projects():
    return get_all_pages("/api/v3/projects")

def get_project_tasks(project_id):
    url = f"{BASE_URL}/api/v3/projects/{project_id}/work_packages?pageSize=100"

    response = requests.get(
        url,
        auth=AUTH
    )

    return response.json()


def get_work_packages():
    return get_all_pages("/api/v3/work_packages")


def get_milestones():
    return get_all_pages("/api/v3/work_packages")


def get_projects_count():
    projects = get_all_pages("/api/v3/projects")
    return len(projects)

def get_work_packages_count():
    work_packages = get_all_pages("/api/v3/work_packages")
    return len(work_packages)

def get_users_count():
    users = get_all_pages("/api/v3/users")
    return len(users)

def get_users():
    url = f"{BASE_URL}/api/v3/users?pageSize=100"

    response = requests.get(
        url,
        auth=AUTH
    )

    return response.json()

import json


def get_active_projects_count():
    filters = json.dumps([
        {
            "active": {
                "operator": "=",
                "values": ["t"]
            }
        }
    ])

    url = f"{BASE_URL}/api/v3/projects?pageSize=1&filters={filters}"

    response = requests.get(
        url,
        auth=AUTH
    )

    data = response.json()

    return {
        "active_projects": data.get("total", 0)
    }
