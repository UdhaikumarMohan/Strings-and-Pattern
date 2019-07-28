# Given a string, print only those characters that appear more than k times

def k_char(String,k):

    freq = {}

    for a in String:

        if a in freq:

            freq[a]+=1

        else:

            freq[a]=1

    for i in freq:

        if freq[i]>k:

            print(i)

String = str(input("Enter the String: "))
k= int(input("Enter the K value: "))
k_char(String,k)
