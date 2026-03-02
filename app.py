from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

palavras = ["teamo", "beijo", "bubia", "linda", "lilas"]
palavra_secreta = random.choice(palavras)

def verificar_palavra(tentativa):
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
    cores = verificar_palavra(tentativa)
    return jsonify({
        "cores": cores,
        "ganhou": tentativa == palavra_secreta
    })