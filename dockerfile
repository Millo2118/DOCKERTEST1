#Usa python 3.9 slim como imagen base
FROM python:3.9-slim 

#Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

#Copia los archivos de dependencias al contenedor
COPY requirements.txt .

#Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

#Copia el archivo Python al contenedor
COPY app.py .

#Expone el puerto 5000 
EXPOSE 5000

#Comando para ejecutar la aplicacion flask
CMD ["python", "app.py"]
