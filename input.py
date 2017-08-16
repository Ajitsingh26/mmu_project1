
from spy_details import spy_name,spy_salutation,spy_age ,spy_rating
from start_chat import start_chat
print "lets get started...!"
question="Do you want ot continue as "+spy_salutation+ " " +spy_name

existing =raw_input(question)

if (existing =="y" or existing=="Y"):
    start_chat(spy_name,spy_age,spy_rating)
elif (existing =="n" or existing=="N"):

        spy_name=raw_input("what is your name :")


        #concatination of salutation and name
        #check weather spy has input something or not
        if len(spy_name)>0:
            #code block if the condition is true  
            spy_age=0
            spy_rating=0.0
            spy_is_online=False

            spy_slautation = raw_input("what should we call you MR. or Miss ? :")
            if spy_slautation.isalpha():
                spy_name = spy_slautation + " " + spy_name
                print "welcome " + spy_name + " glad to have you back with us"
                print "Alright " + spy_name + " let us know more about you "


            else:
                print "please enter character only"

            spy_age = int(raw_input("Enter your age:"))

            if spy_age>12 and spy_age<50:
                print "You are Eligible"

                spy_rating= float(raw_input("Enter your rating:"))
                if spy_rating>=4.5:
                    print "great rating"
                elif spy_rating>=3:
                    print "good rating"
                elif spy_rating<3:
                    print"poor rating"
                spy_is_online = True

                print "Authentication complete. Welcome " + spy_name + "  age: " + str(spy_age) + " and rating of: " + str(spy_rating) + " Proud to have you on board"
            else:
                print"you are not eligible"

        else:
            print"there is an error"

else:
    print"good bye"

