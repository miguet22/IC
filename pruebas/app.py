from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    resultado = 5 * 6
    if resultado > 20:
        return f"El resultado mayor a 20"


if __name__ == "__main__":
    app.run()