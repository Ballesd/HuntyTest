# Utiliza una imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia todo el contenido de tu proyecto al contenedor en /app
COPY app/ .

# Copia el archivo requirements.txt al contenedor en /app
COPY requirements.txt .

# Instala las dependencias de tu proyecto (si tienes un archivo requirements.txt)
RUN pip install -r requirements.txt

# Expon el puerto en el que se ejecutará FastAPI
EXPOSE 8080

# Inicia la aplicación FastAPI usando uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
