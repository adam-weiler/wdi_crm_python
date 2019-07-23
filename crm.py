from contact import Contact
import sys #Needed to trigger the exit command.

class CRM:
    def main_menu(self):
        print('Starting the CRM app')
        while True:
            print('\nWhat would you like to do?')
            self.print_main_menu()
            # user_selected = 2
            user_selected = int(input())
            self.call_option(user_selected)
            # break
    

    def print_main_menu(self):
        print('[1] Add a new contact')
        print('[2] Modify an existing contact')
        print('[3] Delete a contact')
        print('[4] Display all the contacts')
        print('[5] Search by attribute')

        # print('[9] Display full name') #What does this do?

        print('[6] Delete all contacts')
        print('[7] Exit\n')
        print('Enter a number: ')


    def call_option(self, user_selected):
        if user_selected == 1:
            self.add_new_contact()
        elif user_selected == 2:
            self.modify_existing_contact()
        elif user_selected == 3:
            self.delete_contact()
        elif user_selected == 4:
            self.display_all_contacts()
        elif user_selected == 5:
            self.search_by_attribute()

        # elif user_selected == 9:
        #     self.full_name()

        elif user_selected == 6:
            self.delete_all_contacts()
        elif user_selected == 7:
            sys.exit()
    

    def add_new_contact(self):
        print('\nAdding a new contact')
        print('Enter the first name:')
        # first_name = 'John'
        first_name = input()

        print('Enter the last name:')
        # last_name = 'Smith'
        last_name = input()

        print('Enter the email:')
        # email = 'johnsmith@compuserve.net'
        email = input()

        print('Enter a note:')
        # note = 'John is a great guy!'
        note = input()

        # Contact.create(first_name, last_name, email, note)
        contact = Contact.create(first_name=first_name, last_name=last_name, email=email, note=note)
        print('New contact has been created.')

    
    def modify_existing_contact(self):
        print('\nModify an existing contact')
        print('Enter user id to modify:')
        # user_id = 3
        user_id = int(input())

        print('Do you want to change first name, last name, email, or note?')
        print('[1] Modify first name')
        print('[2] Modify last name')
        print('[3] Modify email')
        print('[4] Modify note')

        # modify_attribute = 4
        modify_attribute = int(input())

        print('What is new value?')
        # modify_parameter = 'Johnny'
        modify_parameter = input()

        if modify_attribute == 1:
            query = Contact.update(first_name=modify_parameter).where(Contact.id == user_id)
        elif modify_attribute == 2:
            query = Contact.update(last_name=modify_parameter).where(Contact.id == user_id)
        elif modify_attribute == 3:
            query = Contact.update(email=modify_parameter).where(Contact.id == user_id)
        elif modify_attribute == 4:
            query = Contact.update(note=modify_parameter).where(Contact.id == user_id)
        else:
            print('Invalid attribute.')
        
        query.execute()
        print('Contact has been updated.')
        

    def delete_contact(self):
        print('\nDelete a contact')
        print('Enter user id to delete:')
        # user_id = 2
        user_id = int(input())
        # print(Contact.delete(Contact.find(user_id)))

        Contact.get(id=user_id).delete_instance()
        print ('Your contacts have been deleted.')


    def delete_all_contacts(self):
        print('\nDelete all contacts')
        print('Please enter \'yes\' to confirm:')
        if input() == 'yes':
            # Contact.delete_all()
            Contact.delete().execute()
            print('Your contacts have been deleted.')
        else:
            print('Returning to main menu.')

    def display_all_contacts(self):
        print('\nDisplay all contacts:')
        # Contact.all()

        if len(Contact.select()) > 0:
            for contact in Contact.select():
                Contact.print_contact(contact)
        else:
            print('There are no contacts.')
        
    def search_by_attribute(self):
        print('\nSearch by Attribute')
        print('What do you want to search by?')
        print('[1] Search by first name')
        print('[2] Search by last name')
        print('[3] Search by email')
        print('[4] Search by note')
        print('[5] Search by ID')
      
        # search_attribute = 1 # or 2 or 3 or 4
        search_attribute = int(input())

        # search_attribute = 5
        # search_attribute = int(input())

        if search_attribute in range(1,5): #If search by first_name, last_name, email, or note.
            print(f'What is your search term?')
            # search_parameter = 'B'
            search_parameter = input()
            # print(Contact.find_by(search_attribute, search_parameter))  ###This doesn't work.

            if search_attribute == 1:
                query = Contact.select().where(Contact.first_name == search_parameter)
            elif search_attribute == 2:
                query = Contact.select().where(Contact.last_name == search_parameter)
            elif search_attribute == 3:
                query = Contact.select().where(Contact.email == search_parameter)
            elif search_attribute == 4:
                query = Contact.select().where(Contact.note == search_parameter)

            for contact in query:
                return(Contact.print_contact(contact))
            #For loop has finished and contact was not found.
            print('There is no contact that matches that attribute.')

        elif search_attribute == 5: #If search by ID.
            print(f'What is the ID?')
            # search_id = 2
            search_id = int(input())
            # print(Contact.find(search_id))

            query = Contact.select().where(Contact.id == search_id)
            
            for contact in query:
                return(Contact.print_contact(contact))
            #For loop has finished and contact was not found.
            print('There is no contact with that ID.')

        else: 
            print('That is an invalid selection.') #Todo add more of these. Also a while loop.