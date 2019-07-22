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
        for contact in Contact.contacts:
            print(f'{contact}\n')


    def search_by_attribute(self):
        pass


# john_smith = Contact('John', 'Smith', 'johnsmith@compuserve.net', 'a note')

our_crm = CRM()

our_crm.add_new_contact()

our_crm.display_all_contacts()