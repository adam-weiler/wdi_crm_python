from contact import Contact
import sys #Need to trigger the exit command.


class CRM:

    def main_menu(self):
        print('Starting the CRM app')
        while True:
            print('\nWhat would you like to do?')
            self.print_main_menu()
            user_selected = 8
            # user_selected = int(input())
            self.call_option(user_selected)

            # print('Do you want to add, modify, delete, display all, search by attribute, or exit?')
            # main_request = 'Add'
            #main_request = input()
            break
    



    def print_main_menu(self):
        print('[1] Add a new contact')
        print('[2] Modify an existing contact')
        print('[3] Delete a contact')
        print('[4] Display all the contacts')
        print('[5] Search by attribute')


        # print('[7] Display full name')
        print('[8] Delete all contacts')


        print('[9] Exit')
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

        # Display full name
        # elif user_selected == 7:
        #     self.search_by_attribute()

        # Delete all
        elif user_selected == 8:
            self.delete_all_contacts()

        elif user_selected == 9:
            sys.exit()
            pass
    

    def add_new_contact(self):
        print('\nAdding a new contact')
        print('Enter the first name:')
        first_name = 'John'
        # new_first_name = input()

        print('Enter the last name:')
        last_name = 'Smith'
        # new_last_name = input()

        print('Enter the email:')
        email = 'johnsmith@compuserve.net'
        # new_email = input()

        print('Enter a note:')
        note = 'John is a great guy!'
        # new_note = input()

        Contact.create(first_name, last_name, email, note)

        # print(john_smith.first_name)
        # print(contact1)



        Contact.create('Bit', 'Bot', 'bettymakes@bitmakerlabs.com', 'Loves Pokemon Go.')

        # print(contact2)


        Contact.create('Betty', 'Maker', 'bitbot@bitmaker.com', 'beep boop')

        # print(contact3)






    
    def modify_existing_contact(self):
        print('\nModify an existing contact')
        print('Enter user id to modify:')
        user_id = 1
        # user_id = input()

        print('Do you want to change first name, last name, email, or note?')

        print('[1] Modify first name')
        print('[2] Modify last name')
        print('[3] Modify email')
        print('[4] Modify note')

        modify_attribute = 1
        #modify_attribute = input()


        print('What is new value?')
        modify_value = 'Johnny'


        # print(f'What do you want for {modify_request}?')




    

    def delete_contact(self):
        print('\nDelete a contact\n')
        print('Enter user id to delete:')
        user_id = 2
        # user_id = input()

        # Contact.delete(user_id)

        # print(Contact.find(user_id))


        Contact.delete(Contact.find(user_id))



    
    def delete_all_contacts(self):
        print('\nDelete all contacts')
        print('Please enter \'yes\' to confirm:')

        Contact.delete_all()










    
    def display_all_contacts(self):
        print('\nDisplay all contacts:')
        Contact.all()
        


    def search_by_attribute(self):
        print('\nSearch by Attribute')
        print('What do you want to search by?') #todo Add last_name, email, notes.
        
        print('[1] Search by ID')
        print('[2] Search by first name')
        print('[3] Search by last name')
        print('[4] Search by email')
        print('[5] Search by note')
        


        # search_attribute = 1
        # search_attribute = input()

        # print(f'What is the ID?')
        # search_id = 2
        # # search_id = int(input())

        # return Contact.find(search_id)







        search_attribute = 2 #or 3 or 4 or 5
        # search_attribute = input()

        print(f'What is your search term?')
        search_parameter = 'B'
        # search_term = int(input())

        print(Contact.find_by(search_attribute, search_parameter))






        # print('\nDo you want to search by ID, first name?') #todo Add last_name, email, notes.
        # search_attribute = 'first name'
        # # search_attribute = input()

        # print('What is the first name?')
        # search_parameter = 'Betty'
        # # search_parameter = int(input())

        # return Contact.find_by(search_parameter)






# john_smith = Contact('John', 'Smith', 'johnsmith@compuserve.net', 'a note')

our_crm_app = CRM()

our_crm_app.add_new_contact()

our_crm_app.main_menu()



# 
print('\n\n\n')

our_crm_app.display_all_contacts()

# print(our_crm_app.search_by_attribute())



# our_crm_app.delete_contact()


# our_crm_app.display_all_contacts()
