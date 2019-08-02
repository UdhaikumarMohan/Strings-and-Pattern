# Write code to remove the character at the nth index in a given string.

def remove_n(String,n):

    String = String[:n]+String[n+1:]
    return String

n=5
String = "Udhai kumar"
print(remove_n(String,n))