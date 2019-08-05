# Write code to count the number of uppercase, lowercase, numeric and symbol characters in a given string

def dict_type(String):

    dict={'uppercase':0,'lowercase':0,'numeric':0,'symbols':0,'space':0}

    for a in String:

        if ord(a)>64 and ord(a)<91:

            dict['uppercase']+=1

        elif ord(a)>96 and ord(a)<123:

            dict['lowercase']+=1

        elif ord(a)>47 and ord(a)<58:

            dict['numeric']+=1

        elif ord(a)==32:

            dict['space']+=1

        else:

            dict['symbols']+=1

    return dict

String = """India scored 167 runs by the loss of 5 wickets against Windies.
By the replay WI scored 98 runs by the loss of 4 wkts. @ that moment \ was interupted
due to rain & match refree announce India won by 47 by DLS method."""

print(dict_type(String))

    