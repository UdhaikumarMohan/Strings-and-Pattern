#Test case:

def test_canassertTrue():

    assert True

import replace_2

def test_replace():

    #Arrange:

    String = "udhaikumar"
    expected = "udhaik$mar"

    #Actual:

    actual = replace_2.replace_2(String)

    #Assert:

    assert expected==actual
