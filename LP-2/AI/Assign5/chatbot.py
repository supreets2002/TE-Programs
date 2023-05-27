# Chatbot for College

import random

# Chatbot exit condition
global exit
exit = 0

def chatbot_response(user_questions):
    global exit
    FACILITIES = ['Our College has various facilities like Canteen and Hostel.',
                  'Our College has various facilities like Canteen and Playground.',
                  'Facilities like Canteen, Playground and Hostel are provided by our College.']

    FEES = ['For Computer Department it is 1,25,000/- and for Mechanical Department it is 1,20,000/-.']

    TIMINGS = ['Our College is opened from 10AM to 3:30PM.',
               'We are available from 10AM to 3:30PM.']

    CLUBS = ['We have various clubs that help you to upscale your skills.',
             'We provide club activities in various fields.',
             'There are more than 5 different clubs to upgrade your skills.']


    possible_questions = {'FACILITIES':FACILITIES,
                          'FEES':FEES,
                          'TIMINGS':TIMINGS,
                          'CLUBS':CLUBS}
    
    user_questions = user_questions.upper()
    breakdown = list(user_questions.split(' '))
    print("Bot:",end=" ")
    
    if 'FACILITIES' in breakdown or 'FACILITY' in breakdown:
        print(random.choice(FACILITIES))
        return print("-----------------------------------------------")
        
    elif 'FEE' in breakdown or 'FEES' in breakdown:
        print(FEES[0])
        return print("-----------------------------------------------")
    
    elif 'TIMING' in breakdown or 'TIMINGS' in breakdown or 'TIME' in breakdown:
        print(random.choice(TIMINGS))
        return print("-----------------------------------------------")
        
    elif 'CLUBS' in breakdown or 'CLUB' in breakdown:
        print(random.choice(CLUBS))
        return print("-----------------------------------------------")
    
    elif 'BYE' in breakdown or 'GOODBYE' in breakdown or 'CYA' in breakdown or 'EXIT' in breakdown:
        exit+=1
        print("Happy to help! :)")
    
    else:
        print("I didn't understand your question.")
        return print("-----------------------------------------------")
        


# Chatbot greetings
print("--------------ChatBot---------------")
print("Hello and Greetings, I'm a Chatbot from College.")
get_user_name = input("May I know your name: ")

print("Hello "+get_user_name+". How may I help you?")
print("-----------------------------------------------")

while exit!=1:
    user_input = input(get_user_name+': ')
    chatbot_response(user_input)