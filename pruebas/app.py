from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    resultado=5 * 6
    return f"El resultado es: {resultado}"


if __name__ == "__main__":
    app.run()