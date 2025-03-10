# ai_chat_system
REST API'S
# AI Chat System

This project is a Django-based AI chat system that provides user authentication, chat interactions, and token-based messaging with an AI chatbot.

## Features
- User Registration & Login (JWT Authentication)
- AI Chatbot Interaction
- Token Deduction for Chat Usage
- REST API with Django Rest Framework (DRF)
-

## Installation

### Prerequisites
- Python 3.10+
- Django 5+
- Virtual Environment (venv)
- PostgreSQL (or SQLite for development)

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/ai-chat-system.git
   cd ai-chat-system
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```sh
   python manage.py migrate
   ```
5. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
6. Run the server:
   ```sh
   python manage.py runserver
   ```

## API Endpoints

### User Registration
**Endpoint:** `/register/`
- **Method:** `POST`
- **Request Body:**
  ```json
  { "username": "testuser", "password": "securepassword" }
  ```
- **Response:**
  ```json
  { "message": "Registration successful!", "access": "JWT_ACCESS_TOKEN", "refresh": "JWT_REFRESH_TOKEN" }
  ```

### User Login
**Endpoint:** `/login/`
- **Method:** `POST`
- **Request Body:**
  ```json
  { "username": "testuser", "password": "securepassword" }
  ```
- **Response:**
  ```json
  { "message": "Login successful!", "access": "JWT_ACCESS_TOKEN", "refresh": "JWT_REFRESH_TOKEN" }
  ```

### Chat with AI
**Endpoint:** `/chat/`
- **Method:** `POST`
- **Headers:** `{ "Authorization": "Bearer JWT_ACCESS_TOKEN" }`
- **Request Body:**
  ```json
  { "message": "Hello AI" }
  ```
- **Response:**
  ```json
  { "message": "Hello AI", "response": "AI Response to 'Hello AI'", "remaining_tokens": 900 }
  ```

### Check Token Balance
**Endpoint:** `/token-balance/`
- **Method:** `GET`
- **Headers:** `{ "Authorization": "Bearer JWT_ACCESS_TOKEN" }`
- **Response:**
  ```json
  { "user_id": 1, "username": "testuser", "tokens": 900 }
  ```

## Testing Commands

### Using cURL
- **Register a user:**
  ```sh
  curl -X POST http://127.0.0.1:8000/register/ -H "Content-Type: application/json" -d '{"username": "testuser", "password": "securepassword"}'
  ```
- **Login user:**
  ```sh
  curl -X POST http://127.0.0.1:8000/login/ -H "Content-Type: application/json" -d '{"username": "testuser", "password": "securepassword"}'
  ```
- **Chat with AI:**
  ```sh
  curl -X POST http://127.0.0.1:8000/chat/ -H "Content-Type: application/json" -H "Authorization: Bearer JWT_ACCESS_TOKEN" -d '{"message": "Hello AI"}'
  ```
- **Check Token Balance:**
  ```sh
  curl -X GET http://127.0.0.1:8000/token-balance/ -H "Authorization: Bearer JWT_ACCESS_TOKEN"
  ```

### Using Django Test Framework
Run the tests using:
```sh
python manage.py test
```

## Challenges Faced
- Handling JWT Authentication and Token Expiry.
- Ensuring proper token deduction on chat requests.
- Frontend and backend integration issues.

## Future Improvements
- Connect to OpenAI API for real AI-generated responses.
- Implement real-time chat with WebSockets.
- Improve UI/UX for a better user experience.

## Submission Instructions
1. Push your code to GitHub.
2. Include a detailed `README.md` with setup, usage, and testing details.
3. Provide input/output samples.
4. Submit the repository link or a ZIP file of the project.

---
🚀 **Happy Coding!**


