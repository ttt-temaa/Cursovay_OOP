import pytest
from _pytest.capture import CaptureFixture

from src.utils import filter_vacancies, get_top_vacancies, print_vacancies
from src.vacancy import Vacancy


@pytest.fixture
def vacancies() -> list:
    return [
        Vacancy("python developer", "url", 50000, "developer"),
        Vacancy("python developer", "url", 40000, "python"),
        Vacancy("python developer", "url", 30000, "junior"),
        Vacancy("python developer", "url", 20000, "python"),
    ]


def test_get_top_vacancies(vacancies: list) -> None:
    data = get_top_vacancies(vacancies, 3)
    new_data = [item.salary for item in data]
    assert new_data == [50000, 40000, 30000]


def test_filter_vacancies(vacancies: list) -> None:
    data = filter_vacancies(vacancies, "python")
    new_data = [item.requirement for item in data]
    assert new_data == ["python", "python"]


def test_print_vacancies(capsys: CaptureFixture, vacancies: list) -> None:
    print_vacancies(vacancies)
    message = capsys.readouterr()
    assert message.out.strip() == (
        "Имя вакансии: python developer, ссылка: url, зарплата: 50000, требование: "
        "developer\n"
        "Имя вакансии: python developer, ссылка: url, зарплата: 40000, требование: "
        "python\n"
        "Имя вакансии: python developer, ссылка: url, зарплата: 30000, требование: "
        "junior\n"
        "Имя вакансии: python developer, ссылка: url, зарплата: 20000, требование: "
        "python"
    )
