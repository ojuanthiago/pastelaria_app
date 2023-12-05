from flask import Blueprint, render_template, request, redirect, url_for, session
from funcoes import Funcoes 
from functools import wraps

bp_login = Blueprint('login', __name__, url_prefix='/', template_folder='templates')

@bp_login.route("/", methods=['GET', 'POST']) 
def login(): 
    return render_template("formLogin.html")

@bp_login.route("/logoff", methods=['GET'])
def logoff():
    # limpa um valor individual
    session.pop('login', None)
    # limpa toda sessão
    session.clear()
    # retorna para a tela de login
    return redirect(url_for('login.login'))

@bp_login.route('/login', methods=['POST'])
def validaLogin():
    try:
        # dados enviados via FORM
        cpf = request.form['usuario']
        senha = Funcoes.cifraSenha(request.form['senha'])

        session.clear()

        if (cpf == "abc" and senha == Funcoes.cifraSenha('Bolinhas')):
        # abre a aplicação na tela home
            session['login'] = cpf
            return redirect(url_for('index.formIndex'))
        
        elif (cpf == "abc" and senha != Funcoes.cifraSenha('Bolinhas')):
            raise Exception("Falha de Login! Verifique sua senha.")  
          
        elif (cpf != "abc" and senha == Funcoes.cifraSenha('Bolinhas')):
            raise Exception("Falha de Login! Verifique seu nome de usuário.")   
         
        else:
            raise Exception("Falha de Login! Verifique seus dados e tente novamente!")    
        
    except Exception as e:
        # retorna para a tela de login
        return redirect(url_for('login.login', msgErro=e.args[0]))    
def validaSessao (f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'login' not in session: 
            return redirect(url_for('login.login', msgErro ='Usuário não logado!'))
        else:
            return f(*args, **kwargs)
        
    return decorated_function