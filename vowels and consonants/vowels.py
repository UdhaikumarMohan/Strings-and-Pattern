#Give a string and remove all the vowels and print the rest.

def vowels(String):

    vowels = ['a','e','i','o','u','A','E','I','O','U']

    without_vows = ""

    for a in String:

        if a not in vowels:

            without_vows+=a

    return without_vows

String = "Udhaikumar"
print("The String without vowels: ", vowels(String))