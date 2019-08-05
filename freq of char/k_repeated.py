# Write code to print those words that appear more than k times in a given sentence

def rep_word(String,k):

    freq = {}

    Sentence = String.split()

    for a in Sentence:

        if a in freq:

            freq[a]+=1

        else:

            freq[a]=1

    li=[]


    for a in freq:

        if freq[a]==k:
            
            li.append(a)

    return li

k=2

String = """Indian Goverment cancelled the special status of jammu and kashmir,
and divided it into two union territories named kashmir and ladakh. These partition
was opposed by the state leaders of jammu and kashmir"""

print(rep_word(String,k))