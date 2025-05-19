code = input()
key_choice = input()
custom_key = 0

if key_choice == 'monke':
    custom_key = 1

if key_choice == 'banana':
    custom_key = 2

if key_choice == 'banana bread':
     custom_key = 3

def decoder(text, key):
    alphabet = '123abcdefghijklmnopqrstuvwxyz'
    decoded_text = ' '

    for char in text.lower():
        if char == ' ':
            decoded_text += ' '
        else:
            index = alphabet.find(char)
            new_index = index + key
            decoded_text += alphabet[new_index]

    print(decoded_text)

decoder(code, custom_key)