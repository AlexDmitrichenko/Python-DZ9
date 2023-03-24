import textoffields

def mainMenu() -> int:
    print(textoffields.mainMenu)
    lengthMenu = len(textoffields.mainMenu.split('\n')) - 1 
    while True:
        choice = input('Выберите пункт меню: ')
        if choice.isdigit() and 0 <int(choice)<= lengthMenu:
            return int(choice)
        else:
            print(f'Введите число от 1 до {lengthMenu}')
    
def showContacs(book: list[dict], errorMessage: str):
    if not book:
        print(errorMessage)
        return False
    else:
        for i, contact in enumerate(book, 1):
            print(f'{i}. {contact.get("name"):<20} '
            f'{contact.get("phone"):<20} '
            f'{contact.get("comment"):<20}')
        return True

def addContact () -> dict:
    name = input('Введите Фамилию и Имя через: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    return {'name': name, 'phone': phone, 'comment': comment}

def inputIndex(message: str):
    return int(input(message))

def inputSearch(message):
    return input(message)

def changeContact(book: list[dict], index: int):
    print('Введите новые данные или оставьте пустое поле, для выхода без изменений')
    contact = addContact()
    return {'name': contact.get('name') if contact.get('name') else book[index-1].get('name'),
        'phone': contact.get('phone') if contact.get('phone') else book[index-1].get('phone'),
        'comment': contact.get('comment') if contact.get('comment') else book[index-1].get('comment')}
    
def showMessage(message: str):
    print('-'*len(message))
    print(message)
    print('-'*len(message))

def deleteContact(book: list[dict], index: int):
    return {book[index-1].get('name'), 
            book[index-1].get('phone'), 
            book[index-1].get('comment')}
