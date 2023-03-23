


def mainMenu() -> int:
    return int(input('''Главное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Добавить контакт в справочник Изменить контакт
    5. Найти контакт в справочнике Удалить контакт
    6. Выйти
    Выберите пункт меню: '''))

def showContacs(book: list[dict], errorMessage: str):
    if not book:
        print(errorMessage)
        return False
    else:
        for i, contact in enumerate(book, 1):
            print(f'{i}. {contact.get("name"):<20}'
                f'{contact.get("phone"):<20}'
                f'{contact.get("comment"):<20}')
        return True

def addContact () -> dict:
    name = input('Введите Фамилию и Имя через: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    return {'name': name, 'phone': phone, 'comment': comment}


