from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import router as api_router

app = FastAPI(title="Vino Bingo Backend")

# Allow React frontend & bots to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, change this to your frontend domain!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
