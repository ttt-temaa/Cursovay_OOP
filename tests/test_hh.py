from unittest.mock import Mock, patch

import pytest

from src.hh import HH


@pytest.fixture
def class_hh() -> HH:
    return HH()


@patch("requests.get")
def test_load_vacancies(mock_get: Mock, class_hh: HH) -> None:
    mock_get.return_value.json.return_value = {"items": ["test"]}
    mock_get.return_value.ok = True
    class_hh.load_vacancies("", 1)
    assert class_hh.vacancies == ["test"]
