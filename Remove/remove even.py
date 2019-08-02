# Write code to remove the characters that occur at even indices in a given string

def remove_even(String):

    Str_even=''
    length = len(String)

    for a in range(0,length):

        if (a==1 or not a%2==0):

           Str_even= Str_even+String[a]
            
    return Str_even

String = "0123456789"
print(remove_even(String))