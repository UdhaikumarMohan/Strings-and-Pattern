# Write a function that takes a list of words and returns the length of the shortest word

def shortest(Array):

    length = len(Array[0])

    for a in Array:

        if len(a)<length:

            length = len(a)

    return length

Array = ['Bishop','Heber','College','Tiruchirappalli','udhai']
print(shortest(Array))

    

