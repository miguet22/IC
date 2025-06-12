from flask import Flask

app = Flask(__name__)


def calcular_resultado():
    return 6 * 6

@app.route("/")
def index():
    resultado = calcular_resultado()
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Resultado</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                text-align: center;
                padding-top: 50px;
            }}
            .resultado {{
                font-size: 2em;
                color: #333;
                background-color: #fff;
                display: inline-block;
                padding: 20px 40px;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            }}
            .imagen {{
                margin-top: 30px;
            }}
        </style>
    </head>
    <body>
        <div class="resultado">
            El resultado es: <strong>{resultado}</strong>
        </div>
        <div class="resultado">
            CR7 BETTER THAN LAMINE>
        </div>
        <div class="imagen">
            <img src="/img/photo.jpg" alt="Imagen decorativa">
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
