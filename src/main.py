from flask import Flask
from settings import HOST, PORT, DEBUG

# import blueprint criado
from mod_funcionario.funcionario import bp_funcionario

app = Flask(__name__)
# registro das rotas do blueprint
app.register_blueprint(bp_funcionario)

@app.route('/')
def formIndex():
    return "<h1>Rota da página inicial da nossa WEB APP</h1>", 200

@app.route('/funcionario/')
def formListaFuncionario():
    return "<h1>Rota da página de Funcionários da nossa WEB APP</h1>", 200

@app.route('/cliente/')
def formListaCliente():
    return "<h1>Rota da página de Clientes da nossa WEB APP</h1>", 200

@app.route('/produto/')
def formListaProduto():
    return "<h1>Rota da página de Produtos da nossa WEB APP</h1>", 200

if __name__ == "__main__":
    """ Inicia o aplicativo WEB Flask """
    app.run(host=HOST, port=PORT, debug=DEBUG)
