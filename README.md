# EasyJobs

O EasyJobs é um sistema web simplificado para gerenciamento de empregos. Ele permite que os usuários se cadastrem como candidatos em busca de oportunidades ou como empresas em busca de talentos. Este projeto é construído em Python usando o framework Flask para o backend e Pandas para armazenamento e manipulação de dados.

## Recursos

### Usuários

- **Registro e Autenticação:**
  - Os usuários podem se cadastrar fornecendo nome, e-mail e senha.
  - As senhas são armazenadas de forma segura.
  - A autenticação do usuário é baseada em e-mail e senha.

- **Tipos de Usuários:**
  - Os usuários podem ser "Candidato" ou "Empresa".
  - Candidatos podem fornecer informações detalhadas sobre sua educação e experiência.
  - Empresas podem detalhar informações sobre a empresa e suas vagas.

- **Atualização e Exclusão de Conta:**
  - Os usuários têm a opção de atualizar suas informações ou excluir suas contas.

### Empresas

- **Registro e Edição:**
  - Empresas podem se cadastrar fornecendo informações como setor, CNPJ, endereço e objetivos.
  - Detalhes da empresa, como setor e objetivo, podem ser editados posteriormente.

- **Busca por Candidatos:**
  - Empresas podem buscar candidatos com base em critérios específicos.
  - Os resultados podem ser visualizados em uma lista formatada.

### Candidatos

- **Registro e Edição:**
  - Candidatos podem fornecer informações detalhadas sobre sua educação, experiência e habilidades.
  - Detalhes do candidato, como área de especialização e qualificações, podem ser editados posteriormente.

- **Busca por Vagas:**
  - Candidatos podem buscar oportunidades de emprego com base em critérios específicos.
  - Os resultados podem ser visualizados em uma lista formatada.

### PDFs Personalizados

- **Geração de Relatórios:**
  - Geração de PDF individual com informações detalhadas para candidatos e empresas.
  - Os PDFs incluem dados relevantes, como formação acadêmica, experiência e detalhes da empresa.

## Como Executar

1. **Instalar Dependências:**
   - Certifique-se de ter o Python e o pip instalados.
   - Execute `pip install flask pandas reportlab` para instalar as dependências.

2. **Executar a Aplicação:**
   - Navegue até o diretório do projeto e execute `python main.py`.
   - A aplicação estará acessível em [http://localhost:5000](http://localhost:5000).

3. **Interagir com o Sistema:**
   - Abra um navegador e vá para [http://localhost:5000](http://localhost:5000).
   - Explore recursos de registro, autenticação, busca e geração de PDF.

4. **Encerrar a Aplicação:**
   - Para encerrar a aplicação, pressione `Ctrl + C` no terminal onde a aplicação está sendo executada.

## Estrutura do Projeto

- **`main.py`:**
  - Contém o código principal do backend usando Flask.
  - Gerencia rotas, processa formulários e interage com a lógica principal.

- **`logica.py`:**
  - Contém a lógica principal do sistema, incluindo operações CRUD e autenticação.

- **`templates/`:**
  - Contém arquivos HTML para renderização de páginas.

- **Arquivos de Dados:**
  - `usuarios.xlsx`, `candidatos.xlsx`, `empresas.xlsx`: Armazenam dados de usuários, candidatos e empresas.
  - `vinculacoes.xlsx`: Armazena relacionamentos entre empresas e candidatos.

- **`/img`:**
  - Diretório contendo imagens estáticas usadas no sistema.

