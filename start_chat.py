from add_status import add_status

def start_chat(spy_name , spy_age, spy_rating):
    current_status_message = None
    show_menu =True
    while show_menu:
        menu_choices="what do you want to do: \n 1.Add status \n 2.close application "
        menu_result=raw_input(menu_choices)
        menu_result=int(menu_result)

        #validating use input
        if menu_result == 1:
            #action 1
            add_status(current_status_message)
        elif (menu_result == 2):
            show_menu=False
        else:
            print"wrong choice enter again"


