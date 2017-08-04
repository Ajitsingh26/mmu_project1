spy_name=raw_input("what is your name :")

spy_slautation=raw_input("what should we call you MR. or Miss ? :")
#concatination of salutation and name
#check weather spy has input something or not
if len(spy_name)>0:
    #code block if the condition is true
    spy_name=spy_slautation + "" + spy_name
    print "welcome " +spy_name+ " glad to have you back with us"


