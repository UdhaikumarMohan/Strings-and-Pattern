# Write a function that takes a list of words and returns the length of the longest word

def longest(Array):

    length = 0

    for a in Array:

        if len(a)>length:

            length = len(a)

    return length

Array = ['Bishop','Heber','College','Tiruchirappalli','udhai','abcdefghijklmnopqrstuvwxyz1234567890']
print(longest(Array))

    

