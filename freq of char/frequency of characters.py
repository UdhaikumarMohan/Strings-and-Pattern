# Find the frequency of all characters in the given string:

def freq_char(String):

    freq = {}

    for a in String:

        if a in freq:

            freq[a]+=1

        else:

            freq[a]=1

    return freq

String = "udhaikumar"
print(freq_char(String))
