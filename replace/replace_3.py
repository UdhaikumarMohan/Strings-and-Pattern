# Write code to create a single string from two given strings, separated by a space and swap the first two characters of each string. (input: 'abc', 'ijk', output: 'ijc abk')

def replace_3(String1,String2):

    String = (String2[:2]+String1[2:]+' '+String1[:2]+String2[2:])

    return String

String1='abc' 
String2='ijk'

print(replace_3(String1,String2))