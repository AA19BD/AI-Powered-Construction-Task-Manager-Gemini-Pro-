import os
import httpx

from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get('API_KEY')


async def generate_tasks(project_name: str, location: str) -> List[Dict[str, str]]:
    api_url = (f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent?"
               f"key={API_KEY}")

    request_body = {
        "contents": [
            {"parts": [{"text": f"List key construction tasks for a {project_name} in {location}."}]}
        ]
    }

    try:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(api_url, json=request_body)
            response.raise_for_status()

        response_data = response.json()
        candidates = response_data.get("candidates", [])

        if not candidates:
            print("No tasks found in API response.")
            return []

        task_text = candidates[0].get("content", {}).get("parts", [{}])[0].get("text", "")
        task_list = [task.strip() for task in task_text.split("\n") if task.strip()]

        return [{"name": task, "status": "pending"} for task in task_list]

    except httpx.TimeoutException:
        print("Request timed out. The API took too long to respond.")
    except httpx.HTTPStatusError as e:
        print(f"HTTP Error {e.response.status_code}: {e.response.text}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return []
