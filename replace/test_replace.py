#Test case:

def test_canassertTrue():

    assert True

import replace

def test_replace():

    #Arrange:

    String = "udhaikumar"
    expected = "u$$a$$u$a$"

    #Actual:

    actual = replace.replace(String)

    #Assert:

    assert expected==actual
