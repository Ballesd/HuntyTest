from fastapi import FastAPI, HTTPException, APIRouter

router = APIRouter(
    prefix="/operations",
    tags=["operations"],
)

@router.get("/")
async def index():
    return {"title": "Hola, ruta de inicio de la prueba de Hunty:)"}

def validate_numbers(a, b):
    try:
        float(a)
        float(b)
    except ValueError:
        return False
    return True

@router.get("/add")
async def add(a, b):
    if not validate_numbers(a, b):
        raise HTTPException(status_code=400, detail="Ingresar valores numéricos para la suma y no pueden ser nulos")
    return {"resultado": float(a) + float(b)}

@router.get("/subtract")
async def subtract(a, b):
    if not validate_numbers(a, b):
        raise HTTPException(status_code=400, detail="Ingresar valores numéricos para la resta y no pueden ser nulos")
    return {"resultado": float(a) - float(b)}

@router.get("/multiply")
async def multiply(a, b):
    if not validate_numbers(a, b):
        raise HTTPException(status_code=400, detail="Ingresar valores numéricos para la multiplicación y no pueden ser nulos")
    return {"resultado": float(a) * float(b)}

@router.get("/divide")
async def divide(a, b):
    if not validate_numbers(a, b):
        raise HTTPException(status_code=400, detail="Ingresar valores numéricos para la división y no pueden ser nulos")
    if float(b) == 0:
        raise HTTPException(status_code=400, detail="No se puede dividir entre 0")
    return {"resultado": float(a) / float(b)}
