from flask import Flask, request, render_template, url_for, redirect, session, flash, jsonify
import os
import json

app = Flask(__name__)
DATA_FILE = "dados.json"


#==========================================================================
# Funções DATABASE

def read_database():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def write_database(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


@app.route("/users", methods=["GET"])
def get_users():
    users = read_database()
    return jsonify(users)


@app.route("/users", methods=["POST"])
def add_user():
    users = read_database()
    new_data = request.get_json()
    users.append(new_data)
    write_database(users)
    return jsonify({"message": "User succesfully added", "user": new_data}), 201


#==========================================================================
# Página principal da aplicação
@app.route("/")
def main_page():
    return render_template("index.html")


#==========================================================================
# Função para se cadastrar no JSON

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        name = request.form.get("name")
        username = request.form.get("username")
        password = request.form.get("password")
        gender = request.form.get("gender")
        if [name, username, password, gender]:
    return(render_template("cadastro.html"))


#==========================================================================
# Possível login se já cadastrado.

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username and password:
            return 0
    return(render_template("login.html"))

if __name__ == "__main__":
    app.run(debug=True)