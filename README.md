# PI---EasyJobs

## Aplicação de Cadastro e Busca de Usuários
### Descrição
Este repositório contém uma aplicação web simples desenvolvida em Python utilizando o framework Flask. A aplicação é projetada para o cadastro de usuários do tipo "empresa" e "candidato", permitindo a busca de candidatos por critérios específicos.

### Estrutura de Arquivos
1. **app.py:** Este arquivo contém a configuração do servidor Flask e as rotas principais da aplicação.

2. **logica.py:** Aqui, estão implementadas as funções lógicas da aplicação, incluindo o cadastro de usuários, a definição de tipos, a coleta de informações de empresas e candidatos, a verificação de login, a edição de informações de usuários e a busca de candidatos.

3. **funcoes.py:** Esse arquivo oferece funções adicionais para buscar candidatos por critérios específicos, gerar novos IDs, cadastrar usuários, definir tipos de usuários, coletar informações de empresas e candidatos, verificar login, editar informações de usuários e empresas, buscar candidatos e gerar relatórios em PDF.

4. **templates:** Esta pasta contém os arquivos HTML utilizados para renderizar as páginas da aplicação.

## Como Executar
1. Certifique-se de ter o Python instalado em seu sistema.

2. Instale as dependências necessárias usando o seguinte comando:

`pip install flask pandas reportlab`

3. Execute a aplicação com o seguinte comando:

`python app.py`

4. Abra seu navegador e acesse http://localhost:5000/ para visualizar a aplicação.

## Funcionalidades Principais

- **Cadastro de Usuários:** A aplicação permite o cadastro de usuários do tipo "empresa" e "candidato". Os dados são armazenados em arquivos Excel (usuarios.xlsx, empresas.xlsx, candidatos.xlsx) na primeira execução.

- **Login e Redirecionamento:** O sistema verifica o login e redireciona os usuários para a página apropriada com base em seu tipo.

- **Edição de Informações:** Usuários podem editar suas informações, incluindo empresas cadastrando detalhes sobre seus objetivos e candidatos fornecendo detalhes sobre suas experiências e projetos.

- **Busca de Candidatos por Critérios:** O sistema permite a busca de candidatos com base em critérios específicos, utilizando a função buscar_candidatos_por_criterios.

## Observações
- Este é um projeto simples e pode ser estendido para incluir mais funcionalidades, melhorar a interface do usuário e implementar recursos adicionais.

- Certifique-se de adequar a segurança da aplicação para um ambiente de produção antes de implantá-la.

Sinta-se à vontade para explorar, modificar e expandir este projeto conforme necessário. Se precisar de ajuda ou tiver dúvidas, entre em contato!
