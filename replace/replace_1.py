# Given a string, write code to find a character that appears more than once and replace it with another character at all its occurrences

def replace_1(String):

    freq = {}

    for a in String:

        if a in freq:

            freq[a]+=1

        else:

            freq[a]=1

    for a in freq:

        if freq[a]>1:

            String = (String.replace(a,"$"))

    return String

String = "udhaikumar mohan"
print(replace_1(String))