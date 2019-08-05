# Write code to print the occurrence frequency of all the unique words in a given sentence:

def freq_word(String):

    freq = {}

    Sentence = String.split()

    for a in Sentence:

        if a in freq:

            freq[a]+=1

        else:

            freq[a]=1

    return freq

String = """Indian Goverment cancelled the special status of jammu and kashmir,
and divided it into two union territories named kashmir and ladakh. These partition
was opposed by the state leaders of jammu and kashmir"""

print(freq_word(String))
