def alphabets(String):
    
    vowels=0
    consonants=0
    for a in String:

        if (a=='a' or a=='e' or a=='i' or a=='o' or a=='u' or a=='A' or a=='E' or a=='I' or a=='O' or a=='U'):

            vowels+=1

        else:

            consonants+=1

    print(vowels)
    print(consonants)

String = "Udhaikumar"
alphabets(String)

