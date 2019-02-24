message = input('Enter a message to reverse: ')
translated = ''

i = len(message) - 1
while i >= 0:
    translated += message[i]
    i -= 1

print(translated)