from read_message import read_message
from send_message import send_message
from globals import friends
from spy_details import spy
from add_status import add_status
from add_friend import add_friend
def start_chat(name,age,rating,status):
    current_status_message = None
    show_menu = True

    while show_menu:
            menu_choices = "What do you want to do? \n" \
                           " 1. Add a status update \n " \
                           "2. Add a friend \n " \
                           "3. Send a secret message \n" \
                           " 4. Read a secret message \n" \
                           " 5. Read Chats from a user \n " \
                           "6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    current_status_message = add_status(current_status_message)
                elif menu_choice == 2:
                    no_of_friends = add_friend()
                    print 'You have %d friends' % (no_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif (menu_choice == 4):
                    read_message()
                elif menu_choice == 6:
                    show_menu=False

                else:
                    print 'Sorry you are not of the correct age to be a spy'