def square_function(base_number):
    return(base_number*base_number)


output=0
output=square_function(3)
print(output)


def emoji_converter(message):
    words=message.split(" ")
    emojis={
        ":)":"😃 Happy !!",
        ":(":"😕🙁 Sad ",
    }
    output=""
    for item in words:
        output+=emojis.get(item,item)+" "
    return output


message=input("How are you feeling?")
token=emoji_converter(message)
print(token)