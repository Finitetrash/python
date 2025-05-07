# Ask user if they want to encrypt or decrypt
mode = input("Do you want to encrypt or decrypt? ").lower()

# Ask for the text to process
text = input("Enter your message: ")

# Ask for the key
custom_key = input("Enter the key: ").lower()

# Vigenère cipher function
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            key_char = key[key_index % len(key)]
            key_index += 1

            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message

# Encrypt or decrypt based on user choice
if mode == 'encrypt':
    result = vigenere(text, custom_key, direction=1)
    print(f"\nEncrypted message: {result}")
elif mode == 'decrypt':
    result = vigenere(text, custom_key, direction=-1)
    print(f"\nDecrypted message: {result}")
else:
    print("\nInvalid option. Please enter encrypt or decrypt.")