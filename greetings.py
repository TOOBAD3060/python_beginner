greetings = input('How are you? ')

words = greetings.split(' ')
emojis = {
    'fine': '😍',
    'sad': '😭',
}

output = ''
for word in words:
    output += emojis.get(word, word) + " "
print(output)