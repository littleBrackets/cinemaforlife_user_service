from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import users
from app.db.models import user 
from app.db.session import engine, Base

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Management Service")

origins = [
    "http://localhost:5011",  # React dev server default
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Include user routes
app.include_router(users.router, prefix="/api")
