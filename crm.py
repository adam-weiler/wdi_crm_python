from contact import Contact


class CRM:

    def main_menu(self):
        print('Do you want to add, modify, delete, display all, search by attribute, or exit?')
        main_request = 'Add'
        #main_request = input()
    pass
    
    def print_main_menu(self):
        pass
    
    def call_option(self):
        pass
    

    def add_new_contact(self):
        print('Enter the first name:')
        new_first_name = 'John'
        # new_first_name = input()

        print('Enter the last name:')
        new_last_name = 'Smith'
        # new_last_name = input()

        print('Enter the email:')
        new_email = 'johnsmith@compuserve.net'
        # new_email = input()

        print('Enter a note:')
        new_note = 'John is a great guy!'
        # new_note = input()

        contact1 = Contact.create(new_first_name, new_last_name, new_email, new_note)

        # print(john_smith.first_name)
        # print(contact1)



        contact2 = Contact.create('Bit', 'Bot', 'bettymakes@bitmakerlabs.com', 'Loves Pokemon Go.')

        # print(contact2)


        contact3 = Contact.create('Betty', 'Maker', 'bitbot@bitmaker.com', 'beep boop')

        # print(contact3)






    
    def modify_existing_contact(self):
        print('Enter user id to modify:')
        user_id = 1
        # user_id = input()

        print('Do you want to change first name, last name, email, or note?')
        modify_request = 'Add'
        #modify_request = input()


        print(f'What do you want for {modify_request}?')


    

    def delete_contact(self):
        pass

    
    def display_all_contacts(self):
        print('\nDisplay all contacts:')
        Contact.all()
        


    def search_by_attribute(self):
        # print('\nDo you want to search by ID, or name?') #todo Add last_name, email, notes.
        # search_attribute = 'ID'
        # # search_attribute = input()

        # print('What is the ID?')
        # search_id = 2
        # # search_id = int(input())

        # return Contact.find(search_id)



        print('\nDo you want to search by ID, first name?') #todo Add last_name, email, notes.
        search_attribute = 'first name'
        # search_attribute = input()

        print('What is the first name?')
        search_parameter = 'Betty'
        # search_parameter = int(input())

        return Contact.find_by(search_parameter)





# john_smith = Contact('John', 'Smith', 'johnsmith@compuserve.net', 'a note')

our_crm = CRM()

our_crm.add_new_contact()

# our_crm.display_all_contacts()

print(our_crm.search_by_attribute())



