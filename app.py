from flask import Flask
import os

# Creamos la aplicación Flask
app = Flask(__name__)

# Definimos la ruta principal
@app.route('/')
def hello_world():
    # Mensaje clave para verificar el despliegue
    return '<h1>¡Hola Mundo Flask, desplegado en Kubernetes!</h1>'

# Configuración para Docker
if __name__ == '__main__':
    # Usamos host='0.0.0.0' para que el servidor web sea accesible desde fuera del contenedor.
    # Usamos port=5000 (el puerto por defecto de Flask).
    app.run(debug=True, host='0.0.0.0', port=5000)