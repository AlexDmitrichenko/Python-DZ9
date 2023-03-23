import view
import model

def start():
    while True:
        # pb = model.getPhoneBook()
        choice = view.mainMenu()
        match choice:
            case 1:
                model.openFile()
            case 2:
                pass
            case 3:
                pb = model.getPhoneBook()
                view.showContacs(pb, 'Телефонная книга пуста или не открыта')
            case 4:
                contact = view.addContact()
                model.addContact(contact)
            case 5:
                pass
            case _:
                pass