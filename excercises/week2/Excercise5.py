class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add(self, name: str, phone: str):
        if not self.contacts.get(name):
            self.contacts[name] = phone

    def update(self, name: str, phone: str):
        if self.contacts.get(name):
            self.contacts[name] = phone

    def get(self, name: str) -> str:
        return self.contacts.get(name) or  "" 

    def delete(self, name: str):
        if self.contacts.get(name):
            del self.contacts[name]
    
    def __str__(self):
        return "\n".join([f"{item}: {value}" for (item, value) in sorted(self.contacts.items())])
def main():
    book = ContactBook()
    book.add("petter", "00000000")
    book.add("oscar", "00000001")
    print(book)
    book.delete("petter")
    print(book)
main()