# Write code to replace all occurrences of its first char with '$', except for the first occurrence itself. (e.g.: Input: “anand”, output: “an$nd”):

def replace_2(String):

    first_char = String[:1]

    for a in String:

        if a in first_char:

            String = String.replace(a,'$')
            String = first_char+String[1:]

    return String

String = 'udhaikumar'
print(replace_2(String))

