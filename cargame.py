key = 'QUIT'
user_request = ''
started = False
stopped = True

while user_request != key:
    user_request = input('Get started ....')

    if user_request.upper() == 'HELP':
        print('''
        start - To start the car
        move - To move the car
        quit - To exit the car
        ''')
    elif user_request.upper() == 'START':
        if started:
            print('Already started')
        else:
            print('You started the car')
            started = True
            stopped = False
    elif user_request.upper() == 'STOP':
        if stopped:
            print('Already stopped')
        else:
            print('You stopped the car')
            started = False
            stopped = True
    elif user_request.upper() == 'QUIT':
        print('You stopped the car')
        break
    else:
        print('I do not understand')