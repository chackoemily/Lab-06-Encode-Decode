def decoder(string):
    decoded_string = ''
    for i in range(len(string)):
        if string[i] == '0':
            decoded_string += '7'
        elif string[i] == '1':
            decoded_string += '8'
        elif string[i] == '2':
            decoded_string += '9'
        elif string[i] == '3':
            decoded_string += '0'
        elif string[i] == '4':
            decoded_string += '1'
        elif string[i] == '5':
            decoded_string += '2'
        elif string[i] == '6':
            decoded_string += '3'
        elif string[i] == '7':
            decoded_string += '4'
        elif string[i] == '8':
            decoded_string += '5'
        elif string[i] == '9':
            decoded_string += '6'
    return decoded_string

encoded_string = '1234567890'
print(decoder(encoded_string))