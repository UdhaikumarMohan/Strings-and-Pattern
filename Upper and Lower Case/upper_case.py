# write code to print the given string in all upper case without using built-in functions

def upper_case(String):

    up_case=""

    for a in String:

        if (ord(a)>96) and (ord(a)<123):

            up_case=up_case+chr(ord(a)-32)

        else:

            up_case+=a

    return up_case

String = "Udhaikumar Mohan"
print(upper_case(String))



