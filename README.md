# Github API Consumer

Este projeto consiste em um analisador de usuários do Github, que utiliza a API do Github para obter dados de um usuário e criar um relatório. O relatório gerado inclui informações como nome, perfil, número de repositórios públicos, número de seguidores, número de usuários seguidos e uma lista de repositórios.

Executando o Projeto
Siga os passos abaixo para executar o projeto:

1. Configurando Ambiente Virtual

Crie e ative um ambiente virtual usando os seguintes comandos:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Instalação de Dependências

Instale as dependências necessárias usando o seguinte comando:

```bash
pip3 install -r requirements.txt
```

3. Executando os Testes

Execute o seguinte comando para rodar os testes:

```bash
pytest test_main.py
```

4. Executando o Script Principal

Execute o seguinte comando para rodar o script:

```bash
python main.py
```

O script solicitará que você insira o nome do usuário do Github que deseja analisar. Ele criará um arquivo de relatório no formato {username}.txt contendo as informações do usuário.
