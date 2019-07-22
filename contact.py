class Contact:

    contacts = []
    next_id = 1

    def __init__(self, first_name, last_name, email, note):
        """This method should initialize the contact's attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.note = note
        self.id = Contact.next_id

        Contact.next_id += 1


    def __str__(self):
        return f'''Contact #{self.id}: 
        {self.first_name} {self.last_name} 
        {self.email}
        {self.note}'''


    @classmethod
    def create(cls, new_first_name, new_last_name, new_email, new_note):
        """This method should call the initializer,
        store the newly created contact, and then return it
        """
        new_contact = Contact(new_first_name, new_last_name, new_email, new_note)

        cls.contacts.append(new_contact)

        return(new_contact)

        

    @classmethod
    def all(cls):
        """This method should return all of the existing contacts"""
        for contact in cls.contacts:
            print(f'{contact}\n')

    @classmethod
    def find(cls, request_id):
        """ This method should accept an id as an argument
        and return the contact who has that id
        """

            # for book in cls.entire_library:
            #     if book.author.find(user_input) >= 0:
            #         print(book)

        # print(cls.contacts[request_id])

        # for book in cls.entire_library:
        #         if book.genre == user_input:
        #             print(book)

        for contact in cls.contacts:
            if contact.id == request_id:
                return(contact)

        return 'There is no contact with that ID.'


    def update(self):
        """ This method should allow you to specify
        1. which of the contact's attributes you want to update
        2. the new value for that attribute
        and then make the appropriate change to the contact
        """


    @classmethod
    def find_by(cls, search_parameter):
        """This method should work similarly to the find method above
        but it should allow you to search for a contact using attributes other than id
        by specifying both the name of the attribute and the value
        eg. searching for 'first_name', 'Betty' should return the first contact named Betty
        """

        # book.author.find(user_input) >= 0:

        for contact in cls.contacts:
            if contact.first_name.find(search_parameter) >= 0:
                return(contact)

        return 'There is no contact with that ID.'


    @classmethod
    def delete_all(cls):
        """This method should delete all of the contacts"""


    def full_name(self):
        """Returns the full (first and last) name of the contact"""


    def delete(self):
        """This method should delete the contact
        HINT: Check the Array class docs for built-in methods that might be useful here
        """

    # Feel free to add other methods here, if you need them.

