# Write code to create a new string by concatenating the first k and the last k chars from a given string. If the length of the given string is less than k, then return an empty string.

def join_k(String,k):

    join_str=""
    length = len(String)

    if length<k:

        return join_str 

    join_str=String[:k]+String[-k:]

    return join_str

String = "udhaikumar"
k=1
print(join_k(String,k))