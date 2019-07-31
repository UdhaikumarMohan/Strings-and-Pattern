# Test condition for finding the most number of characters

def test_canassertTrue():

    assert True

import most_character

def test_most_char():

    #Arrange:

    String = "udhaikumar mohan"
    expected = ['u','h','a','m']

    #Actual:

    actual = most_character.most_char(String)

    #Assert:

    assert expected==actual
