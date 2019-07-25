#Find the characters appears more than once:

def most_char(String):

    freq = {}

    for a in String:

        if a in freq:

            freq[a]+=1

        else:

            freq[a]=1

    for i in freq:

        if freq[i]>1:

            print(i)

String = "udhaikumar"
most_char(String)
