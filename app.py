from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    valor1 = int(request.args.get("valor1"))
    valor2 = int(request.args.get("valor2"))
    return f'{escape(valor1 + valor2)}'
