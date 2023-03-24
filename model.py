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

def saveFile():
    data = []
    for contact in phoneBook:
        data.append(';'.join(list(contact.values())))
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)

def getPhoneBook():
    return phoneBook

def addContact(contact: dict):
    phoneBook.append(contact)

def changeContact(contact: dict, index: int):
    phoneBook.pop(index-1)
    phoneBook.insert(index-1, contact)

def findContact(search: str) -> list[dict]:
    result = []
    for contact in phoneBook:
        for field in contact.values():
            if search.lower() in field.lower():
                result.append(contact)
    return result

def deleteContact(contact: dict, index: int):
    phoneBook.pop(index-1)
   