from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    a, b, c, d, e, f, g = True, False, True, True, False, True, True
    if a and b or c and d or e and f or g or not a:
        pass
    
    return calcular_resultado(5, 5)

def calcular_resultado(x, y):
    if x == 0:
        return "x es cero"
    if y == 0:
        return "y es cero"
    if x > y:
        return "x es mayor"
    if y > x:
        return "y essss mayor"
    if x * y > 10:
        return "la multi es mayor a 10"
    if x * y <= 10:
        return "la multi es menor o igual a 10"
    return f"Resultado: {x * y}"

if __name__ == "__main__":
    app.run()