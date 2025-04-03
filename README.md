# Ventry Authentication Service

Ventry Authentication Service is a microservice-based authentication system built with **FastAPI** for the backend and **React** with **TypeScript** for the frontend. It provides secure authentication and user management for the Ventry platform.

---

## Features

### Backend
- Built with **FastAPI**.
- Database integration using SQLAlchemy.
- Token-based authentication with support for access and refresh tokens.
- CORS middleware for cross-origin requests.
- Auto-generated API documentation with Swagger and ReDoc.

### Frontend
- Built with **React** and **TypeScript**.
- **React Router** for client-side routing.
- **Axios** for API communication with token management.
- Tailwind CSS for responsive and modern UI design.
- Authentication pages (Login, Signup) with form validation.

---

## Project Structure

### Backend
/backend ├── app │ ├── database.py # Database connection and setup │ ├── models # SQLAlchemy models │ ├── routes # API route definitions │ └── main.py # FastAPI application entry point

### Frontend

---

## Getting Started

### Prerequisites
- **Python 3.9+** for the backend.
- **Node.js 16+** and **npm** or **yarn** for the frontend.
- **PostgreSQL** or any SQL database supported by SQLAlchemy.

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend

   python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows

uvicorn app.main:app --reload
```
cd frontend

npm install
```

VITE_API_BASE_URL=http://127.0.0.1:8000

Scripts
Backend
Run Development Server: uvicorn app.main:app --reload
Run Tests: pytest
Frontend
Start Development Server: npm run dev
Build for Production: npm run build
Run Tests: npm run test
