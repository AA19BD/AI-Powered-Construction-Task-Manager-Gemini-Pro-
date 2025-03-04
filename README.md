# Construction AI API

## Overview
This is a FastAPI-based application for managing construction projects and their tasks. It integrates with Gemini Pro API to generate project tasks and updates task statuses in the background.

## Setup Instructions

### Prerequisites
- Python 3.11+
- `venv` (Virtual Environment)
- SQLite (or any other database supported by SQLAlchemy)


### 1️⃣ Clone the Repository
```sh
git clone https://github.com/AA19BD/AI-Powered-Construction-Task-Manager-Gemini-Pro-.git
cd construction_ai
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file in the root directory and add the following:
```env
DATABASE_URL=sqlite:///./construction.db
API_KEY=your_api_key_here
```
Gemini Pro API Integration
Use the Gemini Pro Free Tier API to generate construction project tasks dynamically. -

https://ai.google.dev/gemini-api/docs


### 5️⃣ Start the API
```sh
uvicorn app.main:app --reload
```

The API will be available at: **`http://127.0.0.1:8000`**

### **Access API Documentation**
   - Open your browser and go to:
     - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
     - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 📌 API Usage Examples


### 🔹 Get All Projects
```sh
curl -X GET "http://127.0.0.1:8000/projects" -H "accept: application/json"
```

### 🔹 Create a New Project
```sh
curl -X POST "http://127.0.0.1:8000/projects" \
     -H "Content-Type: application/json" \
     -d '{"name": "New Construction Project", "budget": 100000}'
```

### 🔹 Fetch a Specific Project
```sh
curl -X GET "http://127.0.0.1:8000/projects/1" -H "accept: application/json"
```

### 🔹 Run Tests
```sh
python -m pytest app/tests/test_main.py
```

## ✅ License
This project is licensed under the MIT License.

## 📧 Contact
For any questions, feel free to reach out:
- **Email:** aitbanov640@gmail.com
- **GitHub:** [AA19BD](https://github.com/AA19BD)
- **LinkedIn:** [Aitbanov Abylay](https://www.linkedin.com/in/aitbanov-abylay/)


