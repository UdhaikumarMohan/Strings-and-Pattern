#Give a string and remove all the consonants and print the rest.

def vowels(String):

    vowels = ['a','e','i','o','u','A','E','I','O','U']

    without_cons = ""

    for a in String:

        if a in vowels:

            without_cons+=a

    return without_cons

String = "Udhaikumar"
print("The String without consonants: ", vowels(String))