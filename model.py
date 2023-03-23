phoneBook = []
path = 'phone.txt'

def openFile():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for fields in data:
        fields = fields.strip().split(';')
        contact = {'name': fields[0], 
                'phone': fields[1], 
                'comment': fields[2]}
        phoneBook.append(contact)

def getPhoneBook():
    return phoneBook

def addContact(contact: dict):
    phoneBook.append(contact)
