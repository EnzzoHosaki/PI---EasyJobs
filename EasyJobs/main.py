from flask import Flask, render_template, send_from_directory, request
import os
import logica as lg
import pandas as pd

app = Flask(__name__)
app.template_folder = os.path.abspath('templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processar_formulario', methods=['POST'])
def processar_formulario():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    confirmar_senha = request.form['confirmar_senha']
    
    if senha != confirmar_senha:
        mensagem = "As senhas não coincidem. Tente novamente."
    else:
        mensagem = lg.cadastrar_usuario(nome, email, senha)

    return render_template('login.html')
    
@app.route('/login_usuario', methods=['POST'])
def login():
    email = request.form['email']
    senha = request.form['senha']
    resultado= lg.verificar_login(email, senha)

    global id 
    global tipo_usuario

    id = resultado[0] 
    tipo_usuario = resultado[1]

    if resultado != "negado":

        if tipo_usuario == "indefinido":
            return render_template('tipocadastro.html')

        if tipo_usuario == "empresa":
            return render_template('edicao_empresa.html')

        elif tipo_usuario == "candidato":
           return render_template('edicao_candidato.html')
    else:
        print("Email ou senha incorretos.")


@app.route('/cadastrar_candidato', methods=['POST'])
def cadastrar_candidato():
    nacionalidade = request.form['nacionalidade']
    sexo = request.form['sexo']
    idade = request.form['idade']
    estado_civil = request.form['estado_civil']
    endereco = request.form['endereco']
    estado = request.form['estado']
    cidade = request.form['cidade']
    telefone1 = request.form['telefone1']
    telefone2 = request.form.get('telefone2', '') 
    email_candidato = request.form['email_candidato']
    area_atuacao = request.form['area_atuacao']
    curso = request.form['curso']
    instituicao = request.form['instituicao']
    ano_inicio = request.form['ano_inicio']
    ano_conclusao = request.form['ano_conclusao']
    regime_contratacao = request.form['regime_contratacao']
    lg.coletar_informacoes_candidato(id,nacionalidade,sexo,idade,estado_civil,endereco,estado,cidade,telefone1,telefone2,email_candidato,area_atuacao,curso,instituicao,ano_inicio,ano_conclusao,regime_contratacao)
    lg.definir_tipo_usuario(id,"candidato")
    return render_template('edicao_candidato.html')

@app.route('/cadastrar_empresa', methods=['POST'])
def cadastrar_empresa():
   if request.method == 'POST':
        segmento = request.form['segmento-empresa']
        razao_social = request.form['razao-social']
        cnpj = request.form['cnpj']
        inscricao_estadual = request.form['ie']
        endereco = request.form['endereco']
        estado = request.form['estado']
        cidade = request.form['cidade']
        telefone1 = request.form['telefone1']
        telefone2 = request.form['telefone2']
        email_empresa = request.form['email']
        objetivo = request.form['objetivo']
        lg.coletar_informacoes_empresa(id,segmento,razao_social,cnpj,inscricao_estadual,endereco,estado,cidade,telefone1,telefone2,email_empresa,objetivo)
        lg.definir_tipo_usuario(id,"empresa")
        return render_template('edicao_empresa.html')


@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('templates', filename)

if __name__ == '__main__':
    app.run(debug=True)
    
    

