alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text, shift_amount):
    encrypted_message = ""
    new_position = 0
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position > 26:
            new_position = new_position - 26
        encrypted_message += alphabet[new_position]

    print(f'encryed message is :{encrypted_message}')


def decrypt(encoded_text, shift):
    decrypted_message = ""
    new_position = 0
    for letter in encoded_text:
        position = alphabet.index(letter)
        new_position = position - shift
        if new_position < 0:
            new_position = new_position + 26
        decrypted_message += alphabet[new_position]

    print(f'encryed message is :{decrypted_message}')
    # TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  # TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
  # e.g.
  # cipher_text = "mjqqt"
  # shift = 5
  # plain_text = "hello"
  # print output: "The decoded text is hello"

    # TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

if direction == 'encode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(plain_text=text, shift_amount=shift)


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

if direction == 'decode':
    encoded = input("Type your encryped message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    decrypt(encoded_text=encoded, shift=shift)
