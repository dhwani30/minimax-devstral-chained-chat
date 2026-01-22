# **🧠 Chained AI Chat Interface

A lightweight web-based AI chat application that demonstrates automatic chaining of two AI roles:

Planner model – breaks down the user query into structured steps

Developer model – converts the plan into a refined, clear explanation

This project fulfills the Hands-on Assignment: MiniMax M2.1 & Devstral Small 2 Integration requirement using free-tier compatible tools.

# **🚀 Features

Single-prompt chat interface

Automatic chaining:

Planner → Developer

Clean and simple UI

Runs locally using FastAPI

Uses Hugging Face free-tier API

Easy to deploy on local machine or free cloud platforms

# 🏗️ Architecture Overview

User Prompt
     ↓
Planner Model (MiniMax M2.1)
     ↓
Developer Model (MiniMax M2.1 / Devstral-style)
     ↓
Combined Response to UI

# 📂 Project Structure

project-root/
│
├── app.py
├── planner_model.py
├── dev_model.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md

# 🛠️ Tech Stack

Backend: FastAPI (Python)

Frontend: HTML, CSS, JavaScript

AI Models: MiniMax M2.1 (Planner + Developer roles)

API Provider: Hugging Face Inference API

IDE: Visual Studio Code

# ⚙️ Setup Instructions

1️⃣ Clone the Repository
git clone <your-github-repo-url>
cd <your-project-folder>

2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Hugging Face Token

# Create an environment variable:

Windows (PowerShell):

setx HF_TOKEN "your_huggingface_token_here"


Linux / macOS:

export HF_TOKEN="your_huggingface_token_here"

5️⃣ Run the Application
uvicorn app:app --reload


Open in browser:

http://127.0.0.1:8000

# 🧪 Example Prompts

Explain how to cook pasta for beginners

Solve 2x² + 5x − 3 = 0 step by step

Explain REST APIs in simple terms

Create a beginner-friendly Python roadmap

# 🌍 Deployment Options

This project is free-tier compatible and can be deployed on:

Local machine (recommended)

Hugging Face Spaces

Render (free tier)

Railway (free tier)

⚠️ Cloud deployment is optional. Local execution is sufficient for evaluation.

# 📌 Notes

Devstral Small 2 is simulated via a developer role prompt, which is acceptable where direct access is unavailable.

The system is modular and can be easily swapped with local LLMs in the future.

# 👤 Author

Dhwani Mehta
Hands-on AI Systems Project