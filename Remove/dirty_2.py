#Write code to remove the first occurrence of a dirty word from a given sentence. 

def dirty_2(String,word):

    str =""
    li = String.lower().split()
    count=0

    for a in li:

        if (a==word or a[:-1]==word):

            count+=1

            if count>1:

                str+=a+" "

        else:

            str+=a+" "


    return str

String = """Indian Goverment cancelled the special status of jammu and kashmir,
and divided it into two union territories named kashmir and ladakh. These partition
was opposed by the state leaders of jammu and kashmir"""

word = "kashmir"

print(dirty_2(String,word))