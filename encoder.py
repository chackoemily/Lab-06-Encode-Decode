# Emily Chacko
def encode(password):
    new_password = ''
    for num in password:
        num = int(num)
        if num == 7:
            new_password += '0'
        elif num == 8:
            new_password += '1'
        elif num == 9:
            new_password += '2'
        else:
            new_password += str(num + 3)
    return new_password


# Enter decode () function here

program_beginning = True
while program_beginning:
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print('')
    menu_selection = int(input('Please enter an option: '))
    program_running = True
    while program_running:
        if menu_selection == 1:
            password = (input('Please enter your password to encode: '))
            encoded_password = encode(password)
            print('Your password has been encoded and stored!')
            print('')
            program_running = False
        elif menu_selection == 2:
            decoded_password = decode(encoded_password)
            print(f'The encoded password is {encoded_password},  and the original password is {decoded_password}.')
            print('')
            program_running = False
        elif menu_selection == 3:
            program_running = False
            program_beginning = False


