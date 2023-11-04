from fastapi import FastAPI, HTTPException, APIRouter
from routers.operations import router

app = FastAPI()
app.include_router(router)
