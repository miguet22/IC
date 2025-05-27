from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    a, b, c, d, e, f, g = True, False, True, True, False, True, True
    if a and b or c and d or e and f or g or not a:
        pass

    resultado = calcular_resultado(5, 5)
    return f"""
    <html>
    <head>
        <style>
            body {{
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
            }}
            h1 {{
                font-size: 48px;
                color: #333;
            }}
        </style>
    </head>
    <body>
        <h1>{resultado}</h1>
    </body>
    </html>
    """

def calcular_resultado(x, y):
    if x == 0:
        return "x es cero"
    if y == 0:
        return "y es cero"
    if x > y:
        return "x es mayor"
    if y > x:
        return "y es mayor"
    if x * y > 10:
        return "la multi es mayor a 10"
    if x * y <= 10:
        return "la multi es menor o igual a 10"
    return f"Resultado: {x * y}"

if __name__ == "__main__":
    app.run()
