# Write code to remove the all occurrence of a dirty word from a given sentence.

def dirty_1(String,word):

    str =""
    li = String.lower().split()

    for a in li:

        if not (a==word or a[:-1]==word):

            str+=a+" "

    return str

String = """Indian Goverment cancelled the special status of jammu and kashmir,
and divided it into two union territories named kashmir and ladakh. These partition
was opposed by the state leaders of jammu and kashmir"""

word = "kashmir"

print(dirty_1(String,word))