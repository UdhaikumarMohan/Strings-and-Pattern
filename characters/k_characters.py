# Given a string, print only those characters that appear more than k times

def k_char(String,k):

    freq = {}

    for a in String:

        if a in freq:

            freq[a]+=1

        else:

            freq[a]=1

    k_char=[]

    for i in freq:

        if freq[i]>=k:

            k_char.append(i)
    
    return k_char

#String = str(input("Enter the String: "))
#k= int(input("Enter the K value: "))
#print(k_char(String,k))
