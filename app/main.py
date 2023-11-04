from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def index():
    return {"title": "Hola, ruta de inicio de la prueba de Hunty:)"}

##Matematic operations with two numbers in parameters
@app.get("/add")
def add(a: float, b: float):
    return a + b

@app.get("/substract")
def substract(a: float, b: float):
    return a - b

@app.get("/multiply")
def multiply(a: float, b: float):
    return a * b

@app.get("/divide")
def divide(a: float, b: float):
    return a / b