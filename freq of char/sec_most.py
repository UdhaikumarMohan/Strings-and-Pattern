# Write code to find the second most repeated word in a given sentence

def sec_rep(String):

    freq = {}

    Sentence = String.split()

    for a in Sentence:

        if a in freq:

            freq[a]+=1

        else:

            freq[a]=1

    max=0
    sec_max=0
    word=0
    sec_max=0
    li=[]

    for a in freq:

        if freq[a]>max:

            sec_max=max
            sec_word=word
            max = freq[a]
            word=a
            
    for a in freq:        

        if freq[a]==sec_max:

            li.append(a)   

    return li


String = """Indian Goverment cancelled the special status of jammu and kashmir,
and divided it into two union territories named kashmir and ladakh. These partition
was opposed by the state leaders of jammu and kashmir"""

print(sec_rep(String))