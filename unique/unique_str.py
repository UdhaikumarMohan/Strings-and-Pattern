# Given a string, write code to count the number of unique characters in the string:

def unique_str(String):

    freq = {}

    for a in String:

        if a in freq:

            freq[a]+=1

        else:

            freq[a]=1

    count=0

    for a in freq:

        if freq[a]==1:

            count+=1

    return count

String = "udhaikumar mohan"
print(unique_str(String))