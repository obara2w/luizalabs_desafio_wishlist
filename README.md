# Desafio Técnico luizalabs

## O que é?

Esta é uma API desenvolvida em Python, para o desafio técnico no processo de recrutamento da luizalabs.

Frameworks/Libs utilizadas:

* Django - <https://www.djangoproject.com/>
* Djangorestframework - <https://www.django-rest-framework.org/>
* drf-spectacular - <https://github.com/tfranzel/drf-spectacular>

Banco de dados utilizado:
* PostgreSQL - <https://www.postgresql.org/>

A API está publicada no seguinte endereço:

https://desafioluizalabs.obaraweb.com/

A documentação pode ser acessada em:

https://desafioluizalabs.obaraweb.com/swagger-ui/


Usuários que podem ser usados na API:
  
* Username: `admin` / Password: `qweasdws`
* Username: `user` / Password: `qweasdws`

## Como usar

### Passo 1: Instale os programas necessários

1.  Instale o Python 3
2.  Instale o  `virtualenv`

    ```sh
    pip3 install virtualenv
    ```

### Passo 2: Clone este repositório

1.  Clone este projeto em algum diretório.

### Passo 3: Configure um novo ambiente virtual

1.  No terminal, execute:

     ```sh
    virtualenv .env
    ```

    para configurar um novo ambiente virtual.

    **Nota**: Isso criará um ambiente virtual usando a versão Python com a qual o `virtualenv` foi executado (que será a versão com a qual foi instalado). Para usar uma versão específica do Python, use:

    ```sh
    virtualenv --python=<caminho_para_outra_versao_python> .env
    # Por exemplo
    virtualenv --python=/usr/bin/python3.5 .env
    ```

2.  Caso esteja usando o shell `bash`, execute:

    ```sh
    source .env/bin/activate
    ```

    Se você estiver no Windows, use o PowerShell ou cmd e execute:

    ```sh
    .env\Scripts\activate.bat
    ```

    Para ativar o seu novo ambiente virtual Python


**Note**: O restante deste documento pressupõe que o ambiente virtual está ativo, a menos que seja especificado de outra forma.

Se você quiser sair do ambiente virtual, basta executar `deactivate` no terminal.

**Note**: Você precisa ativar o ambiente virtual toda vez que quiser trabalhar no projeto em um novo terminal.


3.  Agora você pode instalar todos os pacotes necessários executando:

    ```sh
    pip install -r requirements.txt
    ```

### Passo 4: Configure o banco de dados

1. Crie uma data base e um usuário em seu banco de dados postgres.

2. Configure as variáveis de ambiente:

    Crie um arquivo com nome `.env` na raiz do projeto com a seguinte estrutura:

    ```
    DB_NAME=[YOUR_DATABASE_NAME]
    DB_USER=[YOUR_DATABASE_USER]
    DB_PASSWORD=[YOUR_DATABASE_PASSWORD]
    DB_HOST=[YOUR_DATABASE_HOST]
    DB_PORT=[YOUR_DATABASE_PORT]
    ```
    Onde:
    
    `[YOUR_DATABASE_NAME]` é o nome da data base criada na etapa anterior,

    `[YOUR_DATABASE_USER]` é o nome do usuário criado na etapa anterior,

    `[YOUR_DATABASE_PASSWORD]` é a senha do usuário criado na etapa anterior,

    `[YOUR_DATABASE_HOST]` é o hostname do seu banco de dados,

    e `[YOUR_DATABASE_PORT]` é a porta onde seu banco de dados está escutando.

3.  No terminal, execute:

     ```sh
    python manage.py migrate
    ```
    
    Para criar as tabelas usadas pela API.

4. Crie um Super Usuário executando:
    
     ```sh
    python manage.py createsuperuser --email admin@desafioluizalabs.com.br --username admin
    ```

    E informe uma senha para o novo usuário.


### Passo 5: Execute o projeto em seu ambiente local de desenvolvimento

Para executar este projeto em modo de desenvolvimento, execute:

```sh
python manage.py runserver
```

A API poderá ser acessada pela endereço http://localhost:8000/ em seu browser.

Utilize o Super Usuário criado para executar os operaçãos da API, ou crie um usuário com o operação `/user/`.


## Como executar os testes unitários

Para executar os testes, execute:

```sh
python manage.py test
```

## Deploy no GCP

### Passo 1: Crie os recursos necessários

1. No Console do Google Cloud, na página do seletor de projetos, selecione ou crie um projeto do Google Cloud.

2. Ative a Cloud SQL Admin API.

### Passo 2: Instale os programas necessários

1.  Instale o Google Cloud SDK.

2.  Baixe e instale o Cloud SQL Proxy.

3.  No terminal, execute:

    ```sh
    gcloud auth login
    ```
    
    Para fazer login no gcloud, e execute:

    ```sh
    gcloud config set project [PROJECT_ID]
    ```

    Onde `[PROJECT_ID]` é o ID do seu projeto no Google Cloud.

### Passo 3: Crie uma instância do Cloud SQL

1. Crie uma instancia Cloud SQL para postgres 12.

2. Com o SDK do Google Cloud e execute: 

    ```sh
    gcloud sql instances describe [YOUR_INSTANCE_NAME]
    ```
    onde `[YOUR_INSTANCE_NAME]` é o nome da instância do Cloud SQL criada na etapa anterior, no retorno do comando, observe o valor mostrado em connectionName.

    Inicie o Cloud SQL Proxy, executando:
    ```sh
    cloud_sql_proxy -instances="[YOUR_INSTANCE_CONNECTION_NAME]"=tcp:5432
    ```
    Onde o valor `[YOUR_INSTANCE_CONNECTION_NAME]` é o valor recuperado da etapa anterior em connectionName.

3. Crie um usuário e um banco de dados no Cloud SQL:

    Para criar um banco de dados, utilize o Console do Google Cloud.
    1. Acesse a página "Instâncias" do Cloud SQL.
    2. Selecione a instância à qual você quer adicionar o banco de dados.
    3. Selecione a guia BANCOS DE DADOS.
    4. Clique em Criar banco de dados.
    5. Na caixa de diálogo "Criar um banco de dados", especifique o nome do banco de dados.
    6. Clique em Criar.

    Para criar um usuário, também utilize o Console do Google Cloud.
    1. Acesse a página "Instâncias" do Cloud SQL.
    2. Selecione a instância para abrir a página "Visão geral" correspondente.
    3. Selecione Usuários no menu de navegação.
    4. Clique em "ADICIONAR USUÁRIO".
    5. Na página Adicionar uma conta de usuário à instância, informe um nome de usuário e uma senha.
    6. Clique em Criar.

### Passo 4: Configure o Banco de dados no Cloud SQL

1. Configure as variáveis de ambiente para configurar o banco de dados:

    Caso não tenha criado ainda, crie um arquivo com nome `.env` na raiz do projeto com a seguinte estrutura:

    ```
    DB_NAME=[YOUR_DATABASE_NAME]
    DB_USER=[YOUR_DATABASE_USER]
    DB_PASSWORD=[YOUR_DATABASE_PASSWORD]
    DB_HOST=localhost
    DB_PORT=5432
    ```
    Onde:
    
    `[YOUR_DATABASE_NAME]` é o nome da data base criada no Cloud SQL,

    `[YOUR_DATABASE_USER]` é o nome do usuário criado no Cloud SQL

    e `[YOUR_DATABASE_PASSWORD]` é a senha do usuário criado no Cloud SQL.

2.  No terminal, execute:

     ```sh
    python manage.py migrate
    ```
    
    Para criar as tabelas usadas pela API.

3. Crie um Super Usuário executando:
    
     ```sh
    python manage.py createsuperuser --email admin@desafioluizalabs.com.br --username admin
    ```

    Informe uma senha para o novo usuário

4. Execute o servidor local e teste a API utilizando o banco de dados no Cloud SQL.

    ```sh
    python manage.py runserver
    ```

    A API poderá ser acessada pela endereço http://localhost:8000/ em seu browser.

5. Execute os testes.

    ```sh
    python manage.py test
    ```

### Passo 5: Fazer deploy no App Engine

1. Configure as variáveis de ambiente do App Engine:

    Abra o arquivo `app.yaml` e configure com os seguintes valores:

        DB_NAME: "[YOUR_DATABASE_NAME]"
        DB_USER: "[YOUR_DATABASE_USER]"
        DB_PASSWORD: "[YOUR_DATABASE_PASSWORD]"
        DB_HOST: "/cloudsql/[YOUR_INSTANCE_CONNECTION_NAME]"
        DB_PORT: "[YOUR_DATABASE_PORT]"
    
    Onde: 

    `[YOUR_DATABASE_NAME]` é o nome da data base no Cloud SQL,

    `[YOUR_DATABASE_USER]` é o nome do usuário no Cloud SQL,

    `[YOUR_DATABASE_PASSWORD]` é a senha do usuário no Cloud SQL,

    `[YOUR_INSTANCE_CONNECTION_NAME]` é a connectionName da sua instância do Cloud SQL,

    e `[YOUR_DATABASE_PORT]` é a porta onde sua instância do Cloud SQL está escutando.

2.  No terminal, execute:

    ```sh
    python manage.py collectstatic
    ```
    
    para criar os arquivos estáticos usados pela sua aplicação, e execute:

    ```sh
    gcloud app deploy
    ```

    Escolha uma região de sua preferência e aguarde a notificação sobre a conclusão do deploy.
