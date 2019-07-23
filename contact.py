from peewee import SqliteDatabase, Model, CharField, TextField

db = SqliteDatabase('crm.db')

class Contact(Model):
    first_name = CharField()
    last_name = CharField()
    email = CharField()
    note = TextField()
    # contacts = [] #This will be stored in the database.
    # next_id = 1 #This will be stored in the database.

    class Meta:
        database = db # db is the SqliteDatabase instance from Line 3.

    # def __init__(self, first_name, last_name, email, note): #This will be handled by the database.
    #     """This method should initialize the contact's attributes"""
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.email = email
    #     self.note = note
    #     self.id = Contact.next_id

    #     Contact.next_id += 1 #The next Contact will have a higher id.

    # def __str__(self): #This will be handled by the database.
    #     return f'''Contact #{self.id}: 
    #     {self.first_name} {self.last_name} 
    #     {self.email}
    #     {self.note}'''

    # @classmethod
    # def create(cls, new_first_name, new_last_name, new_email, new_note): #This will be handled by the database.
    #     """This method should call the initializer,
    #     store the newly created contact, and then return it
    #     """
    #     new_contact = Contact(new_first_name, new_last_name, new_email, new_note)
    #     cls.contacts.append(new_contact)
    #     return(new_contact)     

    # @classmethod
    # def all(cls): #This will be handled by the database.
    #     """This method should return all of the existing contacts"""
    #     if len(cls.contacts) > 0:
    #         for contact in cls.contacts:
    #             print(f'{contact}\n')
    #     else:
    #         print('There are no contacts.')

    # @classmethod #This will be handled by the database.
    # def find(cls, request_id):
    #     """ This method should accept an id as an argument
    #     and return the contact who has that id
    #     """
    #     for contact in cls.contacts:
    #         if contact.id == request_id:
    #             return(contact)
    #     #For loop has finished and contact was not found.
    #     print('There is no contact with that ID.')
    #     return False

    # def update(self, modify_attribute, modify_parameter): #This will be handled by the database.
    #     """ This method should allow you to specify
    #     1. which of the contact's attributes you want to update
    #     2. the new value for that attribute
    #     and then make the appropriate change to the contact
    #     """
    #     if modify_attribute == 1:
    #         self.first_name = modify_parameter
    #         return 'Contact has been updated.'
    #     elif modify_attribute == 2:
    #         self.last_name = modify_parameter
    #         return 'Contact has been updated.'
    #     elif modify_attribute == 3:
    #         self.email = modify_parameter
    #         return 'Contact has been updated.'
    #     elif modify_attribute == 4:
    #         self.note = modify_parameter
    #         return 'Contact has been updated.'
    #     return 'Invalid attribute.'

    # @classmethod
    # def find_by(cls, search_attribute, search_parameter): #This will be handled by the database.
    #     """This method should work similarly to the find method above
    #     but it should allow you to search for a contact using attributes other than id
    #     by specifying both the name of the attribute and the value
    #     eg. searching for 'first_name', 'Betty' should return the first contact named Betty
    #     """
    #     if search_attribute == 1:
    #         for contact in cls.contacts:
    #             if contact.first_name.find(search_parameter) >= 0:
    #                 print('We found this contact by first name:')
    #                 return contact
    #     elif search_attribute == 2:
    #         for contact in cls.contacts:
    #             if contact.last_name.find(search_parameter) >= 0:
    #                 print('We found this contact by last name:')
    #                 return contact
    #     elif search_attribute == 3:
    #         for contact in cls.contacts:
    #             if contact.email.find(search_parameter) >= 0:
    #                 print('We found this contact by email:')
    #                 return contact
    #     elif search_attribute == 4:
    #         for contact in cls.contacts:
    #             if contact.note.find(search_parameter) >= 0:
    #                 print('We found this contact by note:')
    #                 return contact
    #     return 'There is no contact that matches that attribute.'

    # @classmethod
    # def delete_all(cls): #This will be handled by the database.
    #     """This method should delete all of the contacts"""
    #     cls.contacts = []
    #     cls.next_id = 1
    #     return 'Your contacts have been deleted.'

    def full_name(self):
        """Returns the full (first and last) name of the contact"""
        return "{} {}".format(self.first_name, self.last_name)

    # def delete(self): #This will be handled by the database.
    #     """This method should delete the contact
    #     HINT: Check the Array class docs for built-in methods that might be useful here
    #     """
    #     Contact.contacts.remove(self) 
    #     return '\nContact has been deleted.'

# This goes outside the class.
db.connect()
db.create_tables([Contact])