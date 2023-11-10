from fastapi import FastAPI, HTTPException, APIRouter
from routers.operations import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Hola prueba de Hunty"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)