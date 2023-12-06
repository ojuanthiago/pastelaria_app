
from flask import Blueprint, render_template, request, redirect, url_for, jsonify, send_file
import requests
from mod_login.login import validaSessao
from mod_produto.geraPdf import PDF
from funcoes import Funcoes
import base64

from settings import ENDPOINT_PRODUTO, HEADERS_API
bp_produto = Blueprint('produto', __name__, url_prefix="/produto", template_folder='templates')

''' rotas dos formulários '''
@bp_produto.route('/', methods=['GET', 'POST'])
@validaSessao
def formListaProduto():
    try:
        response = requests.get(ENDPOINT_PRODUTO, headers=HEADERS_API)
        result = response.json()
        if (response.status_code != 200):
            raise Exception(result[0])
        return render_template('formListaProduto.html', result=result[0])
    except Exception as e:
        return render_template('formListaProduto.html', msgErro=e.args[0])
    
@bp_produto.route('/form-produto/', methods=['POST', 'GET'])
@validaSessao
def formProduto():
    return render_template('formProduto.html')

@bp_produto.route("/form-edit-produto", methods=['POST', 'GET'])
@validaSessao
def formEditProduto():
    try:
        # ID enviado via FORM
        id_produto = request.form['id']
        # executa o verbo GET da API buscando somente o funcionário selecionado,
        # obtendo o JSON do retorno
        response = requests.get(ENDPOINT_PRODUTO + id_produto, headers=HEADERS_API)
        result = response.json()
        if (response.status_code != 200):
            raise Exception(result[0])
            # renderiza o form passando os dados retornados
        return render_template('formProduto.html', result=result[0])
    except Exception as e:
        return render_template('formListaProduto.html', msgErro=e.args[0])

@bp_produto.route('/insert', methods=['POST'])
def insert():
    try:
        # dados enviados via FORM
        id_produto = request.form['id']
        nome = request.form['nome']
        descricao = request.form['descricao']
        valor_unitario = request.form['valor_unitario']
        # converte em base64
        foto = "data:" + request.files['foto'].content_type + ";base64," + str(base64.b64encode(request.files['foto'].read()), "utf-8")
        # monta o JSON para envio a API
        payload = {'id_produto': id_produto, 'nome': nome, 'descricao': descricao, 'foto': foto, 'valor_unitario': valor_unitario}
        # executa o verbo POST da API e armazena seu retorno
        response = requests.post(ENDPOINT_PRODUTO, headers=HEADERS_API, json=payload)
        result = response.json()
        if (response.status_code != 200 or result[1] != 200):
            raise Exception(result[0])
        # return render_template('formListaProduto.html', msg=result[0])
        # return redirect(url_for('produto.formListaProduto', msg=result[0]))
        return jsonify(erro=False, msg=result[0])
    except Exception as e:
        # return render_template('formListaProduto.html', msgErro=e.args[0])
        return jsonify(erro=True, msgErro=e.args[0])
    
@bp_produto.route('/edit', methods=['POST'])
def edit():
    try:
        # dados enviados via FORM
        id_produto = request.form['id']
        nome = request.form['nome']
        descricao = request.form['descricao']
        valor_unitario = request.form['valor_unitario']
        # converte em base64
        foto = "data:" + request.files['foto'].content_type + ";base64," + str(base64.b64encode(request.files['foto'].read()), "utf-8")
        # monta o JSON para envio a API
        payload = {'id_produto': id_produto, 'nome': nome, 'descricao': descricao, 'foto': foto, 'valor_unitario': valor_unitario}
        # executa o verbo PUT da API e armazena seu retorno
        response = requests.put(ENDPOINT_PRODUTO + id_produto, headers=HEADERS_API, json=payload)
        result = response.json()
        if (response.status_code != 200 or result[1] != 200):
            raise Exception(result[0])
        # return redirect(url_for('produto.formListaProduto', msg=result[0]))
        return jsonify(erro=False, msg=result[0])
    except Exception as e:
        # return render_template('formListaProduto.html', msgErro=e.args[0])
        return jsonify(erro=True, msgErro=e.args[0])
    
@bp_produto.route('/delete', methods=['POST'])
def delete():
    try:
        # dados enviados via FORM
        id_produto = request.form['id_produto']
        # executa o verbo DELETE da API e armazena seu retorno
        response = requests.delete(ENDPOINT_PRODUTO + id_produto, headers=HEADERS_API)
        result = response.json()
        if (response.status_code != 200 or result[1] != 200):
            raise Exception(result[0])
        # return redirect(url_for('produto.formListaProduto', msg=result[0]))
        return jsonify(erro=False, msg=result[0])
    except Exception as e:
        # return render_template('formListaProduto.html', msgErro=e.args[0])
        return jsonify(erro=True, msgErro=e.args[0])
    
''' rotas para PDF '''

@bp_produto.route('/pdfTodos', methods=['POST'])
@validaSessao
def pdfTodos():
    geraPdf = PDF()
    geraPdf.listaTodos()
    return send_file('pdfProdutos.pdf')