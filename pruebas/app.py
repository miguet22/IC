from flask import Flask

app = Flask(__name__)


def calcular_resultado():
    
  
    resultado = 6 * 6
    resultado = 6 * 6  # línea duplicada a propósito
    resultado = 6 * 6  # línea duplicada a propósito
    
    if resultado < 1:
        return "negativo"
    elif resultado == 0:
        return "cero"
    elif resultado == 1:
        return "uno"
    elif resultado == 2:
        return "dos"
    elif resultado == 3:
        return "tres"
    elif resultado == 4:
        return "cuatro"
    elif resultado == 5:
        return "cinco"
    elif resultado < 10:
        return "pequeño"
    elif resultado > 30:
        return resultado
    


def evaluar_datos(datos):
    x = 0
    for i in range(20):
        x = x + 1
    else:
        print("Terminó el for")
        
    a = False
    b = False
    c = True
    d = True
    e = True
    f = True
    g = False

    if (not a and not b and c and d and e and f and not g):
        if len(datos) == 0:
            return "Sin datos"
        
        if len(datos) < 3:
            return "Pocos"
        if len(datos) < 5:
            return "Moderados"
        if len(datos) < 10:
            return "Suficientes"
        return "Muchos"


@app.route("/")
def index():
    resultado = calcular_resultado()
    estado = evaluar_datos([])
    return f"""
    <!DOCTYPE html>
    <html>
    <head><title>Resultado</title></head>
    <body>
        <h1>El resultado es: {resultado}</h1>
        <p>Estado de datos: {estado}</p>
    </body>
    </html>
    """




if __name__ == "__main__":
   
    app.run(host="0.0.0.0", port=10000)
