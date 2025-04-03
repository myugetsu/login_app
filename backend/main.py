# apps/backend/src/main.py
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
from app.models.user import Base
from app.routes import auth

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI application
app = FastAPI(
    title="Ventry Authentication Service",
    description="Authentication microservice for Ventry platform",
    version="0.1.0"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include authentication routes
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

# Optional: Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Run the application (for development)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
