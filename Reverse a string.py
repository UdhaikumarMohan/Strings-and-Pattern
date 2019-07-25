# Reverse the given string in python:

def rev_string(String):

    length = len(String)

    if(length%2==0):

        x = (length/2)+1

    x = (length//2)

    for a in range(0,x):

        temp = String[a]
        String.replace(String[a],String[(length-1)-a])
        String.replace(String[(length-1)-a],temp)

    return String

String = "Udhaikumar"

print(rev_string(String))