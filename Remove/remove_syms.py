# Write code to remove all the spaces and special symbols from a given string:

def remove_syms(String):

    str=""

    for a in String:

        if ((ord(a)>64 and ord(a)<91) or (ord(a)>96 and ord(a)<123) or (ord(a)>47 and ord(a)<58)):

            str+=a

    return str

String = """India scored 167 runs by the loss of 5 wickets against Windies.
By the replay WI scored 98 runs by the loss of 4 wkts. @ that moment \ was interupted
due to rain & match refree announce India won by 47 by DLS method."""

print (remove_syms(String))

        