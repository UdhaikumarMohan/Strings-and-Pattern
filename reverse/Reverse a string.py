# Reverse the given string in python:

def reverse(String): 
  str = "" 
  for i in String: 
    str = i + str
  return str

    

String = "Udhaikumar"

print("The reversed string is: ",end=":")
print(reverse(String))