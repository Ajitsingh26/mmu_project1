
def add_status(current_status_message):

    STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']
    if current_status_message != None:
        print "Your current status message is " + current_status_message + "\n"
    else:
        print 'You don\'t have any status message currently \n'
        default = raw_input("Do you want to select from the older status (y/n)? ")
        if default.upper() == "N":
            new_status_message = raw_input("What status message do you want to set?")

            if len(new_status_message) > 0:
                updated_status_message = new_status_message
                STATUS_MESSAGES.append(updated_status_message)

        elif default.upper() == 'Y':

            item_position = 1

            for message in STATUS_MESSAGES:
                print str(item_position)+" "+message
                item_position = item_position + 1

            message_selection = int(raw_input("\nChoose from the above messages "))

            if len(STATUS_MESSAGES) >= message_selection:
                updated_status_message = STATUS_MESSAGES[message_selection - 1]

        else:
            print 'The option you chose is not valid! Press either y or n.'

