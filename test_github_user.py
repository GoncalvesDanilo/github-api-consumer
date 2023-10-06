import pytest
from unittest.mock import patch
from main import GithubUser


@pytest.fixture
def mock_requests_get():
    with patch("main.requests.get") as mock_get:
        yield mock_get


def test_get_user_data_success(mock_requests_get):
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.text = '{"name": "Test User", "html_url": "https://github.com/test_user", "public_repos": 5, "followers": 10, "following": 8}'

    analyzer = GithubUser("test_user")
    user_data = analyzer._GithubUser__get_user_data()

    assert user_data is not None
    assert user_data["name"] == "Test User"
    assert user_data["html_url"] == "https://github.com/test_user"
    assert user_data["public_repos"] == 5
    assert user_data["followers"] == 10
    assert user_data["following"] == 8


def test_get_user_data_failure(mock_requests_get):
    mock_requests_get.return_value.status_code = 404

    analyzer = GithubUser("nonexistent_user")

    with pytest.raises(Exception, match="Erro ao obter dados do usuário."):
        analyzer._GithubUser__get_user_data()


def test_get_user_repositories_success(mock_requests_get):
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.text = '[{"name": "repo1", "html_url": "https://github.com/test_user/repo1"}, {"name": "repo2", "html_url": "https://github.com/test_user/repo2"}]'

    analyzer = GithubUser("test_user")
    repos = analyzer._GithubUser__get_user_repositories()

    assert repos is not None
    assert len(repos) == 2
    assert repos[0]["name"] == "repo1"
    assert repos[0]["html_url"] == "https://github.com/test_user/repo1"
    assert repos[1]["name"] == "repo2"
    assert repos[1]["html_url"] == "https://github.com/test_user/repo2"


def test_get_user_repositories_failure(mock_requests_get):
    mock_requests_get.return_value.status_code = 404

    analyzer = GithubUser("nonexistent_user")

    with pytest.raises(Exception, match="Erro ao obter dados dos repositórios."):
        analyzer._GithubUser__get_user_repositories()
