# Test case of K characters:

import k_characters

def test_canassertTrue():

    assert True

def test_k_char():

    #Arrange:

    String = "udhaikumar mohan"
    k=2
    expected = ['u','h','a','m']

    #Actual:

    actual = k_characters.k_char(String,k)

    #Assert:

    assert expected==actual




