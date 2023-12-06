from flask import Blueprint, render_template, request, redirect, url_for, session
import requests
from funcoes import Funcoes 
from functools import wraps
from settings import HEADERS_API, ENDPOINT_LOGIN


bp_login = Blueprint('login', __name__, url_prefix='/', template_folder='templates')

@bp_login.route("/", methods=['GET', 'POST']) 
def login(): 
    return render_template("formLogin.html")

@bp_login.route("/logoff", methods=['GET', 'POST'])
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

    cpf = request.form['usuario']
    grupo = request.form['grupo']
    senha = Funcoes.cifraSenha(request.form['senha'])
    
    session.clear()

    payload = {'cpf': cpf, 'senha': senha, 'grupo': grupo}  
 

    response = requests.get(ENDPOINT_LOGIN + cpf, headers=HEADERS_API, json=payload)
    result = response.json()

    if (result):
      session['login'] = cpf
      session['grupo'] = grupo
  
      return redirect(url_for('index.formIndex'))
    else:
      raise Exception("Falha de Login! Verifique seus dados e tente novamente!")

  except Exception as e:

    return redirect(url_for('login.login', msgErro=e.args[0]))

def validaSessao (f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'login' not in session: 
            return redirect(url_for('login.login', msgErro ='Usuário não logado!'))
        else:
            return f(*args, **kwargs)
        
    return decorated_function