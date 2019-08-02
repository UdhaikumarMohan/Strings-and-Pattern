# Test case for finding the frequency of the character

def test_canassertTrue():

    assert True

import freq_of_char

def test_freq():

    #Arrange:

    String = 'udhaikumar'
    expected = {'u':2,'d':1,'h':1,'a':2,'i':1,'k':1,'m':1,'r':1}

    #Actual:

    actual = freq_of_char.freq_char(String)

    #Assert:

    assert expected == actual

