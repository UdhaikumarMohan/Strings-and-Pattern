#Write a function that takes a sentence and returns only those words that contains 4 or more characters

def chars(String):

    str = ""

    li = String.split()

    for a in li:

        if len(a)>=4:

            str+=a+" "

    return str


String = "A quick brown fox jumps over the lazy dog"
print(chars(String))



