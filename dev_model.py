import os
import requests

API_URL = "https://router.huggingface.co/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {os.environ['HF_TOKEN']}",
    "Content-Type": "application/json"
}

def run_developer(plan: str) -> str:
    payload = {
        "model": "MiniMaxAI/MiniMax-M2.1",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are an expert software developer. "
                    "Convert the plan into a clear, concise implementation explanation."
                )
            },
            {
                "role": "user",
                "content": plan
            }
        ],
        "temperature": 0.6
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
