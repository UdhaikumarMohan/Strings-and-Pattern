#Test case:

def test_canassertTrue():

    assert True

import replace_1

def test_replace():

    #Arrange:

    String = "udhaikumar"
    expected = "$dh$ik$m$r"

    #Actual:

    actual = replace_1.replace_1(String)

    #Assert:

    assert expected==actual
