# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' at the end. If the length of the given string is less than 3, leave it unchanged.

def replace_4(String):

    if len(String)>=3:

        if (String[-3:]=='ing'):

            String = String+"ly"

        else:

            String = String+"ing"

    else:

        String = String

    return String

String = "Adding"
print(replace_4(String))



