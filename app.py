from flask import Flask, render_template, request, jsonify
from datetime import datetime
import pytz


app = Flask(__name__)

palavras = ["teamo","beijo","bubia","linda","lilas","tesao","uniao","sonho","meiga",
            "cuida","junto","perto","rosas","janta","noite","casar","kanye","minho",
            "matue","lirio","mimos","comer","maniac","slash","miroh","creed"]

def palavra_do_dia():
    fuso = pytz.timezone("America/Sao_Paulo")
    hoje = datetime.now(fuso).date()

    base = datetime(2024, 1, 1).date()
    dias = (hoje - base).days

    return palavras[dias % len(palavras)]


def verificar_palavra(tentativa):
    palavra_secreta = palavra_do_dia()
    resultado = []

    for i, letra in enumerate(tentativa):
        if letra == palavra_secreta[i]:
            resultado.append("green")
        elif letra in palavra_secreta:
            resultado.append("yellow")
        else:
            resultado.append("gray")

    return resultado


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/verificar", methods=["POST"])
def verificar():
    tentativa = request.json["tentativa"].lower()
    palavra_secreta = palavra_do_dia()

    cores = verificar_palavra(tentativa)

    return jsonify({
        "cores": cores,
        "ganhou": tentativa == palavra_secreta
    })