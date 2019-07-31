#Find the characters appears more than once:

def most_char(String):

    freq = {}

    for a in String:

        if a in freq:

            freq[a]+=1

        else:

            freq[a]=1

        if " " in freq:

            del freq[" "]

    most_occur=[]

    for i in freq:

        if freq[i]>1:

            most_occur.append(i)

    return most_occur

#String = input(str("Enter the Input: "))
#print(most_char(String))
