import pandas as pd
from getpass import getpass
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os


if not os.path.exists("usuarios.xlsx"):
    df = pd.DataFrame(columns=["ID", "Nome", "Email", "Senha", "Tipo"])
    df.to_excel("usuarios.xlsx", index=False)


if not os.path.exists("candidatos.xlsx"):
    df = pd.DataFrame(columns=["ID", "Nacionalidade", "Sexo", "Idade", "EstadoCivil", "Endereco", "Estado", "Cidade", "Telefone1", "Telefone2", "EmailCandidato", "AreaAtuacao"])
    df.to_excel("candidatos.xlsx", index=False)


if not os.path.exists("empresas.xlsx"):
    df = pd.DataFrame(columns=["ID", "Segmento", "RazaoSocial", "CNPJ", "InscricaoEstadual", "Endereco", "Estado", "Cidade", "Telefone1", "Telefone2", "EmailEmpresa", "Objetivo"])
    df.to_excel("empresas.xlsx", index=False)

    
if not os.path.exists("vinculacoes.xlsx"):
    df_vinculacoes = pd.DataFrame(columns=["ID", "ID_Empresa", "ID_Candidato"])
    df_vinculacoes.to_excel("vinculacoes.xlsx", index=False)
    

def gerar_novo_id(df):
    if df.empty:
        return 1
    else:
        return df["ID"].max() + 1

def cadastrar_usuario(nome,email,senha):
    df_usuarios = pd.read_excel("usuarios.xlsx")

    if email in df_usuarios["Email"].values:
        return("Este email já está cadastrado.")
    else:
        tipo = "indefinido"
        novo_id = gerar_novo_id(df_usuarios)
        novo_usuario = pd.DataFrame({"ID": [novo_id], "Nome": [nome], "Email": [email], "Senha": [senha], "Tipo": [tipo]})
        df_usuarios = pd.concat([df_usuarios, novo_usuario], ignore_index=True)
        df_usuarios.to_excel("usuarios.xlsx", index=False)
        return("Cadastro realizado com sucesso.")

def definir_tipo_usuario(id,tipo):
    df_usuarios = pd.read_excel("usuarios.xlsx")
    df_usuarios.loc[df_usuarios["ID"] == id, "Tipo"] = tipo
    df_usuarios.to_excel("usuarios.xlsx", index=False)
    
def coletar_informacoes_empresa(id,segmento,razao_social,cnpj,inscricao_estadual,endereco,estado,cidade,telefone1,telefone2,email_empresa,objetivo):


    dados_empresa = {
        "ID": id,
        "Segmento": segmento,
        "RazaoSocial": razao_social,
        "CNPJ": cnpj,
        "InscricaoEstadual": inscricao_estadual,
        "Endereco": endereco,
        "Estado": estado,
        "Cidade": cidade,
        "Telefone1": telefone1,
        "Telefone2": telefone2,
        "EmailEmpresa": email_empresa,
        "Objetivo": objetivo
    }

    df_empresas = pd.read_excel("empresas.xlsx")
    df_empresas = pd.concat([df_empresas, pd.DataFrame([dados_empresa])], ignore_index=True)
    df_empresas.to_excel("empresas.xlsx", index=False)


def coletar_informacoes_candidato(id,nacionalidade,sexo,idade,estado_civil,endereco,estado,cidade,telefone1,telefone2,email_candidato,area_atuacao,curso,instituicao,ano_inicio,ano_conclusao,regime_contratacao):

            formacoes = []
            formacoes.append({
                    "ID": id,
                    "Curso": curso,
                    "Instituicao": instituicao,
                    "AnoInicio": ano_inicio,
                    "AnoConclusao": ano_conclusao
                })
                
            dado="Para versao futura"
            
            df_candidatos = pd.read_excel("candidatos.xlsx")
            novo_candidato = {
                "ID": id,
                "Nacionalidade": nacionalidade,
                "Sexo": sexo,
                "Idade": idade,
                "EstadoCivil": estado_civil,
                "Endereco": endereco,
                "Estado": estado,
                "Cidade": cidade,
                "Telefone1": telefone1,
                "Telefone2": telefone2,
                "EmailCandidato": email_candidato,
                "AreaAtuacao": area_atuacao,
                "Formacoes": formacoes,
                "Experiencias": dado,
                "Qualificacoes": dado,
                "RegimeContratacao": regime_contratacao,
                "Projetos": dado
            }
            df_candidatos = pd.concat([df_candidatos, pd.DataFrame([novo_candidato])], ignore_index=True)
            df_candidatos.to_excel("candidatos.xlsx", index=False)



def verificar_login(email,senha):
    df_usuarios = pd.read_excel("usuarios.xlsx")
    usuario = df_usuarios[df_usuarios["Email"] == email]

    if not usuario.empty and str(usuario["Senha"].iloc[0]) == str(senha):
        id = usuario["ID"].iloc[0]
        tipo_usuario = usuario["Tipo"].iloc[0]
        return ([id,tipo_usuario])
    else: 
        return ("negado")
        


def editar_usuario(id, nome=None, email=None, senha=None, tipo=None):
    df_usuarios = pd.read_excel("usuarios.xlsx")
    usuario_idx = df_usuarios[df_usuarios["ID"] == id].index

    if not usuario_idx.empty:
        if nome is not None:
            df_usuarios.loc[usuario_idx, "Nome"] = nome
        if email is not None:
            df_usuarios.loc[usuario_idx, "Email"] = email
        if senha is not None:
            df_usuarios.loc[usuario_idx, "Senha"] = senha
        if tipo is not None:
            df_usuarios.loc[usuario_idx, "Tipo"] = tipo

        df_usuarios.to_excel("usuarios.xlsx", index=False)
        return "Usuário editado com sucesso."
    else:
        return "ID de usuário não encontrado."


def editar_empresa(id, segmento=None, razao_social=None, cnpj=None, inscricao_estadual=None,
                   endereco=None, estado=None, cidade=None, telefone1=None, telefone2=None,
                   email_empresa=None, objetivo=None):
    df_empresas = pd.read_excel("empresas.xlsx")
    empresa_idx = df_empresas[df_empresas["ID"] == id].index

    if not empresa_idx.empty:
        if segmento is not None:
            df_empresas.loc[empresa_idx, "Segmento"] = segmento
        if razao_social is not None:
            df_empresas.loc[empresa_idx, "RazaoSocial"] = razao_social

        df_empresas.to_excel("empresas.xlsx", index=False)
        return "Informações da empresa editadas com sucesso."
    else:
        return "ID de empresa não encontrado."


def buscar_candidatos(campo_busca, valor_busca):
    df_candidatos = pd.read_excel("candidatos.xlsx")
    resultados = []

    for _, candidato in df_candidatos.iterrows():
        if campo_busca == "formacao":
            cursos = [curso["Curso"].lower() for curso in candidato["Formacoes"]]
            if valor_busca.lower() in cursos:
                resultados.append({
                    "ID": candidato["ID"],
                    "Nome": candidato["Nome"],
                    "Detalhes": "Link para detalhes",
                })

    return resultados


def vincular_empresa_candidato(id_empresa, id_candidato, acao):

    df_vinculacoes = pd.read_excel("vinculacoes.xlsx")

    if acao == "vincular":
        if ((df_vinculacoes["ID_Empresa"] == id_empresa) & (df_vinculacoes["ID_Candidato"] == id_candidato)).any():
            return "Esta vinculação já existe."
        
        nova_vinculacao = {
            "ID": gerar_novo_id(df_vinculacoes),
            "ID_Empresa": id_empresa,
            "ID_Candidato": id_candidato
        }

        df_vinculacoes = pd.concat([df_vinculacoes, pd.DataFrame([nova_vinculacao])], ignore_index=True)
        df_vinculacoes.to_excel("vinculacoes.xlsx", index=False)

        return "Vinculação criada com sucesso."

    elif acao == "desvincular":
        idx = ((df_vinculacoes["ID_Empresa"] == id_empresa) & (df_vinculacoes["ID_Candidato"] == id_candidato))
        if idx.any():
            df_vinculacoes = df_vinculacoes[~idx]
            df_vinculacoes.to_excel("vinculacoes.xlsx", index=False)
            return "Vinculação removida com sucesso."
        else:
            return "Esta vinculação não existe."

    else:
        return "Ação inválida. Use 'vincular' ou 'desvincular'."


def gerar_relatorio_pdf(tipo_entidade, id_entidade):
    if not os.path.exists("vinculacoes.xlsx"):
        return "A tabela de vinculações não existe."

    df_vinculacoes = pd.read_excel("vinculacoes.xlsx")

    if tipo_entidade == "funcionario":
        empresas_vinculadas = df_vinculacoes[df_vinculacoes["ID_Candidato"] == id_entidade]["ID_Empresa"].tolist()

        if not empresas_vinculadas:
            return "O funcionário não está vinculado a nenhuma empresa."

        df_empresas = pd.read_excel("empresas.xlsx")
        dados_relatorio = df_empresas[df_empresas["ID"].isin(empresas_vinculadas)][["RazaoSocial", "Estado", "Telefone1"]]

        if dados_relatorio.empty:
            return "Não há dados de empresas para gerar o relatório."

        nome_arquivo_pdf = f"relatorio_funcionario_{id_entidade}.pdf"
        pdf = canvas.Canvas(nome_arquivo_pdf, pagesize=letter)
        cell_width = 200
        cell_height = 20

        pdf.drawString(50, 750, "Nome")
        pdf.drawString(250, 750, "Estado")
        pdf.drawString(450, 750, "Telefone")

        y_position = 730
        for _, empresa in dados_relatorio.iterrows():
            pdf.drawString(50, y_position, str(empresa['RazaoSocial']))
            pdf.drawString(250, y_position, str(empresa['Estado']))
            pdf.drawString(450, y_position, str(empresa['Telefone1']))
            y_position -= cell_height

        pdf.save()
        return f"Relatório gerado com sucesso: {nome_arquivo_pdf}"

    elif tipo_entidade == "empresa":
        candidatos_vinculados = df_vinculacoes[df_vinculacoes["ID_Empresa"] == id_entidade]["ID_Candidato"].tolist()

        if not candidatos_vinculados:
            return "A empresa não possui candidatos vinculados."

        df_candidatos = pd.read_excel("candidatos.xlsx")
        dados_relatorio = df_candidatos[df_candidatos["ID"].isin(candidatos_vinculados)][["Nome", "AreaAtuacao"]]

        if dados_relatorio.empty:
            return "Não há dados de candidatos para gerar o relatório."

        nome_arquivo_pdf = f"relatorio_empresa_{id_entidade}.pdf"
        pdf = canvas.Canvas(nome_arquivo_pdf, pagesize=letter)
        cell_width = 200
        cell_height = 20

        pdf.drawString(50, 750, "Nome")
        pdf.drawString(250, 750, "Área de Atuação")

        y_position = 730
        for _, candidato in dados_relatorio.iterrows():
            pdf.drawString(50, y_position, str(candidato['Nome']))
            pdf.drawString(250, y_position, str(candidato['AreaAtuacao']))
            y_position -= cell_height

        pdf.save()
        return f"Relatório gerado com sucesso: {nome_arquivo_pdf}"

    else:
        return "Tipo de entidade inválido. Use 'empresa' ou 'funcionario.'"
