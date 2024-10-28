import json

import pytest

from src.saver import JSONSaver
from src.vacancy import Vacancy


@pytest.fixture
def class_vacancy() -> Vacancy:
    return Vacancy("python developer", "url", 50000, "python")


def test_add_vacancy(class_vacancy: Vacancy) -> None:
    json_saver = JSONSaver("test.json")
    json_saver.add_vacancy(class_vacancy)
    with open("test.json") as f:
        data = json.load(f)

    assert data[-1] == {"link": "url", "name": "python developer", "requirement": "python", "salary": 50000}


def test_delete_vacancy(class_vacancy: Vacancy) -> None:
    json_saver = JSONSaver("test.json")
    json_saver.add_vacancy(class_vacancy)
    json_saver.delete_vacancy(class_vacancy)
    with open("test.json") as f:
        data = json.load(f)

    assert data == []
