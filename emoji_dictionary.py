message = input(">")
words=message.split(' ')
emojis={
    ":)":"😊",
    ":(":"😒"
}
print(words)
output=""
for item in words:
    output+=emojis.get(item,item)+" "
print(output)