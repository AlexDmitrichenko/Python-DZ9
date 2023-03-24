import view
import model

def start():
    while True:
        pb = model.getPhoneBook()
        choice = view.mainMenu()
        match choice:
            case 1:
                model.openFile()
                view.showMessage('Файл успешно открыт')
            case 2:
                model.saveFile()
                view.showMessage('Файл успешно сохранен')
            case 3:
                view.showContacs(pb, 'Телефонная книга пуста или не открыта')
            case 4:
                model.addContact(view.addContact())
                view.showMessage('Выберете пункт 2 для сохранения внесенных изменений в файле')
            case 5:
                if view.showContacs(pb, 'Телефонная книга пуста или не открыта'):
                    index = view.inputIndex('Введите порядковый номер изменяемого контакта: ')
                    contact = view.changeContact(pb, index)
                    model.changeContact(contact, index)
                    view.showMessage(f'Контакт {model.getPhoneBook()[index-1].get("name")} успешно изменен!')
                    view.showMessage('Выберете пункт 2 для сохранения внесенных изменений в файле')
            case 6:
                search = view.inputSearch('Введите искомый элемент: ')
                result = model.findContact(search)
                view.showContacs(result, 'Контакты не найдены')
            case 7:
                view.showContacs(pb, 'Телефонная книга пуста или не открыта')
                index = view.inputIndex('Введите порядковый номер удаляемого контакта: ')
                contact = view.deleteContact(pb, index)
                model.deleteContact(contact, index)
                view.showMessage('Контакт успешно удален!')
                view.showMessage('Выберете пункт 2 для сохранения внесенных изменений в файле')
            case 8:
                return