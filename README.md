# Desafio Técnico luizalabs

## O que é?

Este é uma API desenvolvida em Python / Django, para o desafio técnico no processo de recrutamento da luizalabs.


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

Utilize o Super Usuário criado para executar os métodos da API, ou crie um usuário com o endpoint `/user/`.

