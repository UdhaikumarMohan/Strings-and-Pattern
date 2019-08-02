# Write code to create a new string by concatenating the first 2 and the last 2 chars of the given string. If the length of the given string is less than 2, then return an empty string.

def join(String):

    join_str=""
    length = len(String)

    if length<2:

        return join_str 

    join_str=String[:2]+String[-2:]

    return join_str

String = "ud"
print(join(String))


