#  Write code to convert the given sentence to Sentence Case (Capitalize the first letter of each word)

def capt_sen(String):

    capt_sentence = ""
    length = len(String)

    for a in range(0,length):

        if (a==0) or (ord(String[a-1])==32):

            if (ord(String[a])>96) and (ord(String[a])<123):
                
                capt_sentence+=chr((ord(String[a])-32))
                
            else:

                capt_sentence+=String[a]
        else:
            
            capt_sentence+=String[a]

    return capt_sentence

String = """lot of people believes that PIrates of somalia hijacked an American
ship"""
print(capt_sen(String))



