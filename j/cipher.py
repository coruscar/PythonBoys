alphabet = 'abcdefghijklmnopqrstuvwxyz'
ke = input('please enter a key: ')
key = int(ke)
newMsg = ''

msg = input('enter a msg to encrypt: ')


for character in msg: 
    if character in alphabet:
        position = alphabet.find(character)
        newPos = (position + key) % 26
        newChar = alphabet[newPos]
        newMsg = newMsg + newChar
    else: 
        newMsg += character
print('new msg is:', newMsg)