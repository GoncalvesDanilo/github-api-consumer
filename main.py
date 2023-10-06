import requests
import json


class GithubUser:
    def __init__(self, username):
        self.username = username
        self.api_url = f"https://api.github.com/users/{username}"

    def generate_report(self):
        user_data = self.__get_user_data()

        report = f"Relatório do usuário {self.username}\n\n"
        report += f"Nome: {user_data['name']}\n"
        report += f"Perfil: {user_data['html_url']}\n\n"
        report += f"Número de repositórios públicos: {user_data['public_repos']}\n"
        report += f"Número de seguidores: {user_data['followers']}\n"
        report += f"Número de usuários seguidos: {user_data['following']}\n\n"
        report += "Lista de Repositórios:\n\n"

        repos = self.__get_user_repositories()
        for repo in repos:
            report += f"- {repo['name']}: {repo['html_url']}\n"

        with open(f"{self.username}.txt", "w") as file:
            file.write(report)

    def __get_user_data(self) -> dict:
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            return json.loads(response.text)
        except Exception as e:
            raise Exception("Erro ao obter dados do usuário.", e)

    def __get_user_repositories(self):
        repos_url = self.api_url + "/repos"
        try:
            response = requests.get(repos_url)
            response.raise_for_status()
            return json.loads(response.text)
        except Exception as e:
            raise Exception("Erro ao obter dados dos repositórios.", e)


if __name__ == "__main__":
    username = input("Insira o nome do usuário: ")
    analyzer = GithubUser(username)

    try:
        analyzer.generate_report()
        print("Relatório gerado com sucesso!")
    except Exception as e:
        print("Erro ao gerar o relatório. \n Detalhes:", e)
