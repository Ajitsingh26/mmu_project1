from add_status import add_status

from spy_details import spy
from start_chat import start_chat
print "lets get started...!"
question="Do you want ot continue as "+spy['salutation']+ " " +spy['name'] +" "

existing =raw_input(question)

if (existing =="y" or existing=="Y"):
    start_chat(spy['name'],spy['age'],spy['rating'],spy['is_online'])
elif (existing =="n" or existing=="N"):

        spy_name=raw_input("what is your name :")


        #concatination of salutation and name
        #check weather spy has input something or not
        if len(spy_name)>0:
            #code block if the condition is true
            spy['age']=0
            spy['rating']=0.0
            spy['is_online']=False

            spy_slautation = raw_input("what should we call you MR. or Miss ? :")
            if spy['salutation'].isalpha():
                spy['name'] = spy['salutation'] + " " + spy['name']
                print "welcome " + spy['name'] + " glad to have you back with us"
                print "Alright " + spy['name'] + " let us know more about you "


            else:
                print "please enter character only"

                spy['age'] = raw_input("Enter your age:").isdigit()


                if spy['age']>=12 and spy['age']<=50:
                    print "You are Eligible"

                    spy['rating']= float(raw_input("Enter your rating:"))
                    if spy['rating']>=4.5:
                        print "great rating"
                    elif spy['rating']>=3:
                        print "good rating"
                    elif spy['rating']<3:
                        print"poor rating"
                        spy['is_online'] = True

                    print "Authentication complete. Welcome " + spy['name'] + "  age: " + str(spy['age']) + " and rating of: " + str(spy['rating']) + " Proud to have you onboard"
                else:
                    print"you are not eligible"


        else:
            print"there is an error"

else:
    print"good bye"

