FROM python:3.10-slim

WORKDIR /app

# Copia requirements.txt dentro del contenedor
COPY requirements.txt /app/

RUN pip install -r requirements.txt

EXPOSE 80

# Copia el resto del código al contenedor
COPY . /app/

CMD ["python", "app.py"]
