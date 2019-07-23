from contact import Contact
from crm import CRM

our_crm_app = CRM()

Contact.create('John', 'Smith', 'johnsmith@compuserve.net', 'John is a great guy!')
Contact.create('Bit', 'Bot', 'bettymakes@bitmakerlabs.com', 'Loves Pokemon Go.')
Contact.create('Betty', 'Maker', 'bitbot@bitmaker.com', 'beep boop')

#CRM methods
our_crm_app.main_menu()

# our_crm_app.print_main_menu()

# our_crm_app.call_option(1)
# our_crm_app.call_option(2)
# our_crm_app.call_option(3)
# our_crm_app.call_option(4)
# our_crm_app.call_option(5)
# our_crm_app.call_option(6)
# our_crm_app.call_option(7)

# our_crm_app.add_new_contact()

# our_crm_app.modify_existing_contact()

# our_crm_app.delete_contact()

# our_crm_app.delete_all_contacts()

# our_crm_app.display_all_contacts()

# our_crm_app.search_by_attribute()