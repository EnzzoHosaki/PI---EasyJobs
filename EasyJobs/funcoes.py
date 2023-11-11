import pandas as pd
from getpass import getpass
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


def buscar_candidatos_por_criterios():
    df_candidatos = pd.read_excel("candidatos.xlsx")

    campos_disponiveis = ["Formacoes", "Experiencias", "Qualificacoes", "RegimeContratacao", "Projetos"]

    print("Campos de pesquisa disponíveis:")
    for i, campo in enumerate(campos_disponiveis, start=1):
        print(f"{i}. {campo}")

    escolha = input("Digite o número dos campos de pesquisa separados por vírgula (ex: 1,2,3): ")
    escolha = [int(e.strip()) for e in escolha.split(",")]

    campos_escolhidos = [campos_disponiveis[i - 1] for i in escolha]

    criterios = {}

    for campo in campos_escolhidos:
        termos_busca = input(f"Digite os termos de busca para o campo '{campo}' (separados por vírgula, ex: termo1,termo2): ")
        termos_busca = [termo.strip() for termo in termos_busca.split(",")]

        if campo == "Formacoes":
            criterios[campo] = [{"Curso": termo, "Instituicao": termo} for termo in termos_busca]
        elif campo == "Experiencias":
            criterios[campo] = [{"Empresa": termo, "AnoEntrada": termo, "AnoSaida": termo, "Cargo": termo, "Atividades": termo} for termo in termos_busca]
        elif campo == "Qualificacoes":
            criterios[campo] = [{"Qualificacao": termo} for termo in termos_busca]
        elif campo == "RegimeContratacao":
            criterios[campo] = termos_busca
        elif campo == "Projetos":
            criterios[campo] = [{"NomeProjeto": termo, "DescricaoProjeto": termo, "PalavrasChave": termo, "LinkProjeto": termo} for termo in termos_busca]

    def atende_critérios(row):
        for crit, valor in criterios.items():
            if crit in row:
                if isinstance(valor, list):
                    if not any(all(item.items() <= d.items() for d in row[crit] if isinstance(d, dict)) for item in valor):
                        return False
                else:
                    if not any(termo in row[crit] for termo in valor): 
                        return False
        return True

    candidatos_filtrados = df_candidatos[df_candidatos.apply(atende_critérios, axis=1)]

    if not candidatos_filtrados.empty:
        print("\nCandidatos que atendem aos critérios:")
        print(candidatos_filtrados)
    else:
        print("\nNenhum candidato atende aos critérios.")

def gerar_novo_id(df):
    if df.empty:
        return 1
    else:
        return df["ID"].max() + 1

def cadastrar_usuario(nome,email,senha):
    df_usuarios = pd.read_excel("usuarios.xlsx")

    if email in df_usuarios["Email"].values:
        print("Este email já está cadastrado.")
    else:
        tipo = "indefinido"
        novo_id = gerar_novo_id(df_usuarios)
        novo_usuario = pd.DataFrame({"ID": [novo_id], "Nome": [nome], "Email": [email], "Senha": [senha], "Tipo": [tipo]})
        df_usuarios = pd.concat([df_usuarios, novo_usuario], ignore_index=True)
        df_usuarios.to_excel("usuarios.xlsx", index=False)
        print("Cadastro realizado com sucesso.")

def definir_tipo_usuario(id):
    df_usuarios = pd.read_excel("usuarios.xlsx")

    if id in df_usuarios["ID"].values:
        tipo_usuario = df_usuarios[df_usuarios["ID"] == id]["Tipo"].iloc[0]

        if tipo_usuario == "indefinido":
            while True:
                tipo = input("Digite o tipo de usuário (empresa ou candidato): ").strip().lower()
                if tipo in ["empresa", "candidato"]:
                    df_usuarios.loc[df_usuarios["ID"] == id, "Tipo"] = tipo
                    df_usuarios.to_excel("usuarios.xlsx", index=False)
                    return tipo
                else:
                    print("Tipo de usuário inválido. Use 'empresa' ou 'candidato'.")
    else:
        print("ID de usuário não encontrado.")
        return None

def coletar_informacoes_empresa(id):
    
    segmento = input("Digite o segmento da empresa: ")
    razao_social = input("Digite a razão social da empresa: ")
    cnpj = input("Digite o CNPJ da empresa: ")
    inscricao_estadual = input("Digite a inscrição estadual da empresa: ")
    endereco = input("Digite o endereço da empresa: ")
    estado = input("Digite o estado da empresa: ")
    cidade = input("Digite a cidade da empresa: ")
    telefone1 = input("Digite o telefone 1 da empresa: ")
    telefone2 = input("Digite o telefone 2 da empresa: ")
    email_empresa = input("Digite o email da empresa: ")
    objetivo = input("Digite o objetivo da empresa: ")

   
    return {
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

def coletar_informacoes_candidato(id):
    df_usuarios = pd.read_excel("usuarios.xlsx")

   
    if id in df_usuarios["ID"].values:
        tipo_usuario = df_usuarios[df_usuarios["ID"] == id]["Tipo"].iloc[0]

        if tipo_usuario == "candidato":
            nacionalidade = input("Digite sua nacionalidade: ")
            sexo = input("Digite seu sexo: ")
            idade = input("Digite sua idade: ")
            estado_civil = input("Digite seu estado civil: ")
            endereco = input("Digite seu endereço: ")
            estado = input("Digite seu estado: ")
            cidade = input("Digite sua cidade: ") 
            telefone1 = input("Digite seu telefone 1: ")
            telefone2 = input("Digite seu telefone 2: ")
            email_candidato = input("Digite seu email: ")
            area_atuacao = input("Digite sua área de atuação (separada por vírgulas, ex: TI, Marketing): ")
            
            
            formacoes = []
            while True:
                curso = input("Digite o curso de formação: ")
                instituicao = input("Digite a instituição de ensino: ")
                ano_inicio = input("Digite o ano de início: ")
                ano_conclusao = input("Digite o ano de conclusão: ")
                formacoes.append({
                    "ID": id,
                    "Curso": curso,
                    "Instituicao": instituicao,
                    "AnoInicio": ano_inicio,
                    "AnoConclusao": ano_conclusao
                })
                mais_formacoes = input("Deseja adicionar mais uma formação? (s/n): ").strip().lower()
                if mais_formacoes != "s":
                    break
            
            
            experiencias = []
            while True:
                empresa = input("Digite o nome da empresa: ")
                ano_entrada = input("Digite o ano de entrada na empresa: ")
                ano_saida = input("Digite o ano de saída da empresa: ")
                cargo = input("Digite o cargo: ")
                atividades = input("Digite as principais atividades desempenhadas no cargo: ")
                experiencias.append({
                    "ID": id,
                    "Empresa": empresa,
                    "AnoEntrada": ano_entrada,
                    "AnoSaida": ano_saida,
                    "Cargo": cargo,
                    "Atividades": atividades
                })
                mais_experiencias = input("Deseja adicionar mais uma experiência? (s/n): ").strip().lower()
                if mais_experiencias != "s":
                    break
            
           
            qualificacoes = []
            while True:
                qualificacao = input("Digite uma qualificação ou atividade complementar: ")
                qualificacoes.append({
                    "ID": id,
                    "Qualificacao": qualificacao
                })
                mais_qualificacoes = input("Deseja adicionar mais uma qualificação ou atividade complementar? (s/n): ").strip().lower()
                if mais_qualificacoes != "s":
                    break
            
            
            projetos = []
            while True:
                nome_projeto = input("Digite o nome do projeto: ")
                descricao_projeto = input("Digite a descrição do projeto: ")
                palavras_chave = input("Digite as palavras-chave do projeto (separadas por vírgulas, ex: Python, Web): ")
                link_projeto = input("Digite o link do projeto: ")
                projetos.append({
                    "ID": id,
                    "NomeProjeto": nome_projeto,
                    "DescricaoProjeto": descricao_projeto,
                    "PalavrasChave": palavras_chave,
                    "LinkProjeto": link_projeto
                })
                mais_projetos = input("Deseja adicionar mais um projeto? (s/n): ").strip().lower()
                if mais_projetos != "s":
                    break
            
           
            regime_contratacao = input("Digite o regime de contratação (separado por vírgulas, ex: CLT, PJ): ")
            
            
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
                "Experiencias": experiencias,
                "Qualificacoes": qualificacoes,
                "RegimeContratacao": regime_contratacao,
                "Projetos": projetos
            }
            df_candidatos = pd.concat([df_candidatos, pd.DataFrame([novo_candidato])], ignore_index=True)
            df_candidatos.to_excel("candidatos.xlsx", index=False)
            
            print("Informações do candidato cadastradas com sucesso.")
        else:
            print("Este usuário é do tipo empresa, não é possível adicionar informações de candidato.")
    else:
        print("ID de usuário não encontrado.")

def verificar_login(email,senha):

    df_usuarios = pd.read_excel("usuarios.xlsx")
    usuario = df_usuarios[df_usuarios["Email"] == email]

    if not usuario.empty and str(usuario["Senha"].iloc[0]) == str(senha):
        print("Login bem-sucedido.")
        id = usuario["ID"].iloc[0]
        tipo_usuario = usuario["Tipo"].iloc[0]

        if tipo_usuario == "indefinido":
            tipo_usuario = definir_tipo_usuario(id)

        if tipo_usuario == "empresa":
            df_empresas = pd.read_excel("empresas.xlsx")
            empresa_existente = df_empresas[df_empresas["ID"] == id]
            if not empresa_existente.empty:
                print("Direcionando para a busca de candidatos por critérios...\n")
                buscar_candidatos_por_criterios()
            else:
                print("Você é uma empresa, mas ainda não preencheu seus dados. Preencha seus dados antes de buscar candidatos.")
                coletar_informacoes_empresa(id)
        elif tipo_usuario == "candidato":
            df_candidatos = pd.read_excel("candidatos.xlsx")
            candidato_existente = df_candidatos[df_candidatos["ID"] == id]
            if not candidato_existente.empty:
                print("Direcionando para a busca de vagas por critérios...\n")
            else:
                print("Você é um candidato, mas ainda não preencheu suas informações. Preencha suas informações antes de buscar vagas.")
                coletar_informacoes_candidato(id)
    else:
        print("Email ou senha incorretos.")

def exibir_elementos_cadastrados(tipo):
    if tipo == "empresa":
        df = pd.read_excel("empresas.xlsx")
    elif tipo == "candidato":
        df = pd.read_excel("candidatos.xlsx")
    else:
        print("Tipo de usuário inválido.")
        return

    if not df.empty:
        print("\nElementos cadastrados:")
        print(df)
    else:
        print("\nNenhum elemento cadastrado.")

def exibir_elementos_cadastrados_geral():
    df = pd.read_excel("usuarios.xlsx")
    if not df.empty:
        print("\nElementos cadastrados (Geral):")
        print(df)
    else:
        print("\nNenhum elemento cadastrado (Geral).")

