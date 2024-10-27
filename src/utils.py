from src.vacancy import Vacancy


def get_top_vacancies(vacancies: list[Vacancy], n: int) -> list:
    """Функция возвращения топа вакансий"""

    vacancies.sort(reverse=True)
    new_list = []
    for i in range(n):
        new_list.append(vacancies[i])
    return new_list


def filter_vacancies(vacancies: list[Vacancy], filter_word: str) -> list:
    """Функция фильтрации вакансии по слову в требованиях"""

    new_list = []
    for i in vacancies:
        if filter_word in i.requirement:
            new_list.append(i)

    return new_list


def print_vacancies(vacancies: list[Vacancy]) -> None:
    """Функция, которая выводит вакансии"""

    for i in vacancies:
        print(i)
