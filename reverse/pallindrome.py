# Write code to find if the given string is a palindrome:

def is_pallindrome(String):

    flag = True
    str = "" 
    for a in String: 
        str = a + str
    
    if not str==String:

        flag = False

    return flag

String = "abcbb"
print(is_pallindrome(String))
