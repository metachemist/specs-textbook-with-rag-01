from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Physical AI Textbook API", version="1.0.0")

# Add CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # Docusaurus default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
from .api import chat, auth  # Import the API routers
app.include_router(chat.router, prefix="/api", tags=["chat"])
app.include_router(auth.router, prefix="/api", tags=["auth"])

@app.get("/")
def read_root():
    return {"message": "Physical AI Textbook API is running!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}