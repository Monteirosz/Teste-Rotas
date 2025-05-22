from flask import Flask, request, jsonify
from libs.banco import inserir_usuario, view_tabela, validar_login

app = Flask(__name__)

@app.route('/cadastro', methods=['POST'])
def rota_cadastro():
    data = request.get_json()
    user = data.get('usuario')
    senha = data.get('senha')
    email = data.get('email')
    telefone = data.get('telefone')
    
    if not all([user, senha, email, telefone]): #Verifica se todos os itens da lista são "True"
        return jsonify({'erro': 'Você precisa preencher todos os campos'})

    inserir_usuario(user, senha, email, telefone)
    return jsonify({'mensagem': 'Usuário cadastrado com sucesso'})

@app.route('/users', methods=['GET'])
def view_users():
    dados = view_tabela()
    usuarios = [{
            'usuario': user,
            'senha': senha,
            'email': email,
            'telefone': telefone
        }
        for (user, senha, email, telefone) in dados
    ]
    return jsonify(usuarios), 200

@app.route('/login', methods=['GET'])
def login():
    data = request.get_json()
    user = data.get('usuario')
    senha = data.get('senha')

    if not all([user, senha]):
        return jsonify({'erro': 'Usuário e senha são obrigatórios'})

    if validar_login(user, senha):
        return jsonify({'mensagem': 'Seja bem-vindo(a)!'})
    else:
        return jsonify({'erro': 'Usuário ou senha inválidos'})


if __name__ == '__main__':
    app.run(debug=True, port=51153)