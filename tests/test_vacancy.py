import pytest

from src.vacancy import Vacancy


@pytest.fixture
def class_vacancy() -> Vacancy:
    return Vacancy("python developer", "url", 50000, "python")


def test_lt(class_vacancy: Vacancy) -> None:
    vacancy2 = Vacancy("python developer", "url", 6000, "python")
    assert class_vacancy > vacancy2


def test_le(class_vacancy: Vacancy) -> None:
    vacancy2 = Vacancy("python developer", "url", 50000, "python")
    assert class_vacancy >= vacancy2


def test_str(class_vacancy: Vacancy) -> None:
    assert str(class_vacancy) == "Имя вакансии: python developer, ссылка: url, зарплата: 50000, требование: python"


def test_vacancy_from_hh() -> None:
    vacancy = Vacancy.vacancy_from_hh({"name": "python", "alternate_url": "url", "salary": None, "snippet": None})

    assert str(vacancy) == "Имя вакансии: python, ссылка: url, зарплата: 0.0, требование: NotFound"
