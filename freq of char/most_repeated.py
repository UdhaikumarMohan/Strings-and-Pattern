# Write code to find the most repeated word in a given sentence.

def rep_word(String):

    freq = {}

    Sentence = String.split()

    for a in Sentence:

        if a in freq:

            freq[a]+=1

        else:

            freq[a]=1

    max=0
    word=0
    li=[]

    for a in freq:

        if freq[a]>max:

            max = freq[a]
            word=a

    for a in freq:

        if freq[a]==max:
            
            li.append(a)

    return li


String = """Indian Goverment cancelled the special status of jammu and kashmir,
and divided it into two union territories named kashmir and ladakh. These partition
was opposed by the state leaders of jammu and kashmir"""

print(rep_word(String))