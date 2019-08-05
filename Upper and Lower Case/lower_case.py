# write code to print the given string in all lower case without using built-in functions

def lower_case(String):

    low_case=""

    for a in String:

        if (ord(a)>64) and (ord(a)<91):

            low_case=low_case+chr(ord(a)+32)

        else:

            low_case+=a

    return low_case

String = "uDHAI kUMAR"
print(lower_case(String))



