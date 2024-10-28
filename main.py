from src.hh import HH
from src.saver import JSONSaver
from src.utils import filter_vacancies, get_top_vacancies, print_vacancies
from src.vacancy import Vacancy


def main() -> None:
    """Функция, основанная сборку и запуск проекта"""

    user_word = input("Здравствуйте! Введите слово для поиска вакансий: ")
    user_pages = int(input("Введите количество страниц (до 20) для подбора вакансий: "))
    hh_vacancies = HH()
    hh_vacancies.load_vacancies(user_word, user_pages)
    all_vacancies = hh_vacancies.vacancies
    list_vacancies = []

    for i in all_vacancies:
        formatted_vacancy = Vacancy.vacancy_from_hh(i)
        list_vacancies.append(formatted_vacancy)

    user_filter = input("Осуществить фильтровку вакансий по требованиям? [Да/Нет] ")
    if user_filter.lower().strip() == "да":
        user_filter_word = input("Введите слово, с помощью которого выполнить фильтрацию: ")
        list_vacancies = filter_vacancies(list_vacancies, user_filter_word)

    user_top = int(input("Введите количество выводимых вакансий: "))

    user_sort = input("Отсортировать вакансии по зарплате? [Да/Нет] ")
    if user_sort.lower().strip() == "да":
        list_vacancies = get_top_vacancies(list_vacancies, user_top)
    else:
        list_vacancies = [list_vacancies[i] for i in range(user_top)]

    if input("Сохранить вакансии в файл? [Да/Нет] ").lower() == "да":
        name_file = input("Введите имя файла в формате '.json', где будут сохраняться вакансии: ")
        json_saver = JSONSaver(name_file)
        for vacancy in list_vacancies:
            json_saver.add_vacancy(vacancy)
    print_vacancies(list_vacancies)


if __name__ == "__main__":
    main()
