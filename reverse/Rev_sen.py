# Write code to reverse every word in a given sentence

def rev_sen(String):

    rev_sentence=""
    Sp_str = String.split()

    for a in Sp_str:

        rev_sentence = a+" "+rev_sentence

    return rev_sentence

String = """A quick brown fox jumps over the lazy dog"""
print(rev_sen(String))



