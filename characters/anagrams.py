# Write code to check if the two given strings form an anagram (e.g. binary and brainy are anagrams. Same characters are used exactly once)

def anagram(String1,String2):

    flag = True

    String1 = sorted(String1.lower())
    String2 = sorted(String2.lower())

    if not (String1==String2):

        flag = False
    
    return flag

String1 = "Binary"
String2 = "brainy"

print(anagram(String1,String2))