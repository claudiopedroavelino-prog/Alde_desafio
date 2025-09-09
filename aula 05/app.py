from flask import Flask, request, jsonify , render_template , redirect , url_for
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_jwt_extended import verify_jwt_in_request, decode_token

import sqlite3

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = '422517' 
jwt = JWTManager(app)

@app.route("/")
def index():
    mostrar = "false"
    return render_template("index.html" , mostrar = mostrar)

@app.route("/registro", methods = ["post"])
def registro():
    nome = request.form.get("nome")
    apelido = request.form.get("apelido")
    senha = request.form.get("senha")
    telefone = request.form.get("telefone")
    banco_de_dados = sqlite3.connect("dados.db")
    cursor = banco_de_dados.cursor()
    cursor.execute("""create table if not exists usuario(
                                   
                                   id integer primary key, 
                                   nome char(45),
                                   apelido char(45),
                                   senha char(45),
                                   telefone char(45)

                                   )""")
    cursor.execute("""insert into usuario(nome , apelido , senha , telefone) values (?,?,?,?)""",(nome , apelido , senha , telefone))
    lista = cursor.execute("""select * from usuario""")
    obter = lista.fetchall()
    print(obter)
    banco_de_dados.commit()
    banco_de_dados.close()
    mostrar = "false" 
    return redirect("/inicio"),201

@app.route("/Login",methods = ["post"])
def Login():
    telefone = request.form.get("telefone")
    senha = request.form.get("senha")
    banco_de_dados = sqlite3.connect("dados.db")
    cursor = banco_de_dados.cursor()
    lista = cursor.execute("select telefone , senha from usuario order by id asc;")
    obter = lista.fetchall()
    for x in obter:
        print(f"{x[0]}")
        print(f"senha:{x[1]}")
    for x in obter:

        if x[0]== telefone and x[1] == senha:
                token = create_access_token(identity=telefone)
                return redirect(url_for('logado', token=token))
    print(obter)
    banco_de_dados.commit()
    banco_de_dados.close()
    return "Credenciais inválidas", 401




@app.route("/logado")
def logado():
    token = request.args.get("token")
    if not token:
        return render_template("index.html")
    try:
        decoded = decode_token(token)
        telefone = decoded['sub']
    except Exception:
        return "Token inválido ou expirado", 401
    banco_de_dados = sqlite3.connect("dados.db")
    cursor = banco_de_dados.cursor()
    lista = cursor.execute("select * from usuario order by id asc;")
    obter = lista.fetchall()
    mostrar = "true"
    return render_template("index.html" , mostrar = mostrar , obter = obter)

    
@app.route("/inicio")
def inicio():
    mostrar = "false"
    return render_template("index.html" , mostrar = mostrar)


if __name__ == "__main__":
    app.run(debug=True)
