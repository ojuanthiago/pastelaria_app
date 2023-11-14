from flask import Flask, session 
import os 
from datetime import timedelta 
from settings import HOST, PORT, DEBUG, TEMPO_SESSION 

# import blueprint criado
from mod_cliente.cliente import bp_cliente
from mod_erro.erro import bp_erro
from mod_funcionario.funcionario import bp_funcionario
from mod_index.index import bp_index
from mod_login.login import bp_login 
from mod_produto.produto import bp_produto

app = Flask(__name__)
# registro das rotas do blueprint
app.register_blueprint(bp_erro)
app.register_blueprint(bp_cliente)
app.register_blueprint(bp_funcionario)
app.register_blueprint(bp_index)
app.register_blueprint(bp_login)
app.register_blueprint(bp_produto)

if __name__ == "__main__":
    """ Inicia o aplicativo WEB Flask """
    app.run(host=HOST, port=PORT, debug=DEBUG)

app.secret_key = os.urandom(12).hex()


# ajuste SAMESITE 
app.config.update(
    SESSION_COOKIE_SAMESITE='None', 
    SESSION_COOKIE_SECURE=True,
    #DEBUG=True,
) 
# método para renovar o tempo da sessão 
@app.before_request 
def before_request(): 
    session.permanent = True 
    session['tempo'] = int(TEMPO_SESSION) 
    # o padrão é 31 dias... 
    app.permanent_session_lifetime = timedelta(minutes=session['tempo']) 
