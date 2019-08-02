# Write code to remove the characters that occur at odd indices in a given string

def remove_odd(String):

    Str_odd=''
    length = len(String)

    for a in range(0,length):

        if (a==0 or a%2==0):

           Str_odd= Str_odd+String[a]
            
    return Str_odd

String = "0123456789"
print(remove_odd(String))