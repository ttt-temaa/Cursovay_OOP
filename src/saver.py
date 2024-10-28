import json
from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class Saver(ABC):
    """Абстрактный класс для saver"""

    @abstractmethod
    def __init__(self, filename: str):
        pass

    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        pass


class JSONSaver(Saver):
    """Класс для сохранения информации о вакансиях в JSON-файл"""

    def __init__(self, filename: str):
        self.__filename = filename
        with open(filename, "w", encoding="UTF8") as file:
            json.dump([], file)

    def __dump(self, item: list) -> None:
        """Метод записи в json файл"""

        with open(self.__filename, "w", encoding="UTF8") as file:
            json.dump(item, file, ensure_ascii=False)

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Метод добавления вакансий в json файл"""

        data = {
            "name": vacancy.name,
            "link": vacancy.link,
            "salary": vacancy.salary,
            "requirement": vacancy.requirement,
        }

        with open(self.__filename, "r", encoding="UTF8") as file:
            item = json.load(file)
        if data not in item:
            item.append(data)
            self.__dump(item)

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Метод удаления вакансий из json файла"""

        data = {
            "name": vacancy.name,
            "link": vacancy.link,
            "salary": vacancy.salary,
            "requirement": vacancy.requirement,
        }

        with open(self.__filename, "r", encoding="UTF8") as file:
            item = json.load(file)
        item.remove(data)
        self.__dump(item)

    @property
    def filename(self) -> str:
        return self.__filename
