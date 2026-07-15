from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine

from auth import router as auth_router
from routers.user import router as user_router
from routers.inventory import router as inventory_router

app = FastAPI(title="Textile Waste Intelligence Platform")
app.add_middleware(
    CORSMiddleware,
    allow_origins= ["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(inventory_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to Textile Waste Intelligence Platform"
    }