
#begining of coding

from spy_detail import spy, Spy, friends, Chatmessage
from steganography.steganography import Steganography
from termcolor import colored


STATUS_MESSAGES = ['Hello! im back', 'All glitters are not gold', 'OMG so many fools','A good experience came from a bad experience']  #list name: STATUS_MESSAGES containing old status

print"hello!"   #HELLO STRING PRINT HERE
print"let's get started"

#spy choices as existing or new
question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (yes/no)? "
existing = str(raw_input(question))
print str(existing)


# add_status function definition starts
def add_status(current_status_message):
    updated_status_message = None

    if current_status_message != None:
        print 'Your current status message is %s \n' % (current_status_message)
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")

        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either yes or no.'

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You did not update your status message'

    return updated_status_message
# add_status function definition ends


#add_friend function definition starts
def add_friend():
     new_friend = Spy('', '', 0, 0.0)
     new_friend.name = raw_input("Please add your friend's name: ")
     new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

     new_friend.name = new_friend.salutation+ " " + new_friend.name

     new_friend.age = raw_input("Age?")
     new_friend.age = int(new_friend.age)

     new_friend.spy_rating = raw_input("Spy rating?")
     new_friend.spy_rating = float(new_friend.spy_rating)

     if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
         friends.append(new_friend)
         print 'Friend Added!'
     else:
         print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

     return len(friends)
#add_friend function definition ends


#select_friend function definition starts
def select_friend():
        item_number = 0

        for friend in friends:
            print '%d. %s aged %d with rating %.2f is online' % (item_number + 1, friend.name,
                                                                 friend.age,
                                                                 friend.rating)
            item_number = item_number + 1

        friend_choice = raw_input("Choose from your friends")

        friend_choice_position = int(friend_choice) - 1

        return friend_choice_position
#select_friend function definition ends


#rsens_message function starts
def send_message():

    friend_choice = select_friend()

    input_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(input_image, output_path, text)

    new_chat = Chatmessage(text, True)

    friends[friend_choice].chats.append(new_chat)

    print "Your secret message image is ready!"
# read_message function ends


#read_message function starts
def read_message():

    sender = select_friend()

    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)

    new_chat = Chatmessage(secret_text,False)


    friends[sender].chats.append(new_chat)

    print "Your secret message has been saved!"
#read_message function ends


#read chat_history function starts
def read_chat_history():
    read_for = select_friend()
    print 'Chat history:'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print colored(chat.time.strftime("%d %B %Y"), 'blue'),
            print colored('Rashmi said : ' , 'red'),
            print (chat.message)

        else:
            print colored(chat.time.strftime("%d %B %Y"),'blue'),
            print colored('%s said:' % ( friends[read_for].name),'red'),
            print (chat.message)
#read chat_history function ends

#  start_chat function definition
def start_chat(spy):
    current_status_message = None
    spy.name = spy.salutation + " " + spy.name

    if spy.age > 15 and spy.age < 40:
      print "Authentication complete. Welcome " + spy.name + "  age: " + str(spy.age) + "  and rating of spy: " + str(spy.rating) + "  Proud to have you onboard"
      show_menu = True
      while show_menu:  # while loop
        menu_choices = "What do you want to do? \n1. Add a status update \n2. Add new friend \n3. Send new messages \n4. Read old messages \n5. Read_chat_history \n6 Close Application" #multiple choices for the operation to be done
        menu_choice = raw_input(menu_choices)
        if len(menu_choices)>0:
         menu_choice = int(menu_choice)

        if menu_choice == 1:                                                              # choices
            print 'You chose to update the status'
            current_status_message = add_status(current_status_message)
        elif menu_choice == 2:
           print 'You chose to add new friend'
           number_of_friends = add_friend()
           print 'You have %d friends' % (number_of_friends)
        elif menu_choice == 3:
            print 'You chose to send a message'
            send_message()
        elif menu_choice == 4:
            print 'You chose to read messages'
            read_message()
        elif menu_choice == 5:
            print 'You chose to read chat history'
            read_chat_history()
        else:
           show_menu = False
           print 'You chose to leave the chat'
#start_chat function ends


#checking wether user existing or new
if existing == "yes":
   #Continue with the default user/details imported from the helper file.
   start_chat(spy)    #start_chat function declaration or calling
else:
    #when user is new to spychat
    spy = Spy('', '', 0, 0.0)
    # spy_name variable
    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
    if len(spy.name) > 0:
         print 'Welcome dear(*_*)' + spy.name + '.We are Glad to have you back with us.'

            # spy_saultation.
         spy.salutation = raw_input("What should we call you (Mr. or Ms.)? ")
         spy.name = spy.salutation + " " + spy.name
          # Here are some important things about our spy like age & rating:
         print "Alright " + spy.name + ". I'd like to know a little bit more about you before we proceed..."

            # input spy_age
         spy.age = int(raw_input("What is your age?"))
         print type(spy.age)                     #tells about the datatype of spy_age
         if spy.age > 15 and spy.age < 40:       # condition
            print"hey! you can proceed further"  # action
            spy.rating = float(raw_input("What is your spy rating?"))
            # print spy_rating
            if spy.rating > 4.5:
                print 'Great ace!'
            elif spy.rating > 3.5 and spy.rating <= 4.5:
                print 'You are one of the good ones.'
            elif spy.rating >= 2.5 and spy.rating <= 3.5:
                print 'You can always do better'
            elif spy.rating <2.5:
                print 'We can always use somebody to help in the office.'
         else:
              print"sorry! your age is invalid to be a spy"

         spy_is_online = True                      # spy_is online or not
         # Using + for string concatenation
         print "Authentication complete. Welcome " + spy.name + "  age: " + str(spy.age) + "  and rating of spy: " + str(spy.rating) + "  Proud to have you onboard"
         start_chat(spy)    #function declaration or calling

    else:
         print "A spy needs to have a valid name. Try again and pls re-enter your name"
