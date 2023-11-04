from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")

async def index():
    return {"title": "Hola, ruta de inicio de la prueba de Hunty:)"}

#Función que valida que los parámetros sean números o no sean valores nulos
async def typeValidation(a, b):
    if a is None or b is None:
        return False
    else:
        try:
            float(a)
            float(b)
        except ValueError:
            return False
        else:
            return True

# ----------------------------Funciones de operaciones matemáticas---------------------------   
# suma
@app.get("/add")
async def add(a, b):
    if typeValidation(a, b):
        return {"resultado": float(a) + float(b)}
    else:
        raise HTTPException(status_code=400, detail="Ingresar valores numéricos para la suma y no pueden ser nulos")
    
# resta
@app.get("/substract")
async def substract(a, b):
    if typeValidation(a, b):
        return {"resultado": float(a) - float(b)}
    else:
        raise HTTPException(status_code=400, detail="Ingresar valores numéricos para la resta y no pueden ser nulos")

# multiplicación
@app.get("/multiply")
async def multiply(a, b):
    if typeValidation(a, b):
        return {"resultado": float(a) * float(b)}
    else:
        raise HTTPException(status_code=400, detail="Ingresar valores numéricos para la multiplicación y no pueden ser nulos")

# división
@app.get("/divide")
async def divide(a, b):
    if typeValidation(a, b):
        if float(b) == 0:
            raise HTTPException(status_code=400, detail="No se puede dividir entre 0")
        else:
            return {"resultado": float(a) / float(b)}
    else:
        raise HTTPException(status_code=400, detail="Ingresar valores numéricos para la división y no pueden ser nulos")