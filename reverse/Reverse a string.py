# Reverse the given string in python:

def reverse(String): 
  str = "" 
  for a in String: 
    str = a + str
  return str

    

String = "Udhaikumar"

print("The reversed string is: ",end=":")
print(reverse(String))