# Write code to check if a given string contains all 26 alphabets in any case.

def is_contains(String):

    flag = True

    alphabets = "abcdefghijklmnopqrstuvwxyz"

    String = String.lower()

    for a in alphabets:

        if a not in String:

            flag = False
            break

    return flag

String = "A quick brown fox jumps over the lazy dog"
print(is_contains(String))
