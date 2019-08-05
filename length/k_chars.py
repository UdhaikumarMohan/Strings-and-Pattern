#Write a function that takes a sentence and returns only those words that contains k or more characters

def chars(String,k):

    str = ""

    li = String.split()

    for a in li:

        if len(a)>=k:

            str+=a+" "

    return str


String = "A quick brown fox jumps over the lazy dog"
k=2
print(chars(String,k))



