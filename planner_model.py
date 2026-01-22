import os
import requests

API_URL = "https://router.huggingface.co/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {os.environ['HF_TOKEN']}",
    "Content-Type": "application/json"
}

def run_planner(user_prompt: str) -> str:
    payload = {
        "model": "MiniMaxAI/MiniMax-M2.1",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a planning assistant. "
                    "Break the user request into clear, structured steps."
                )
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        "temperature": 0.3
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
