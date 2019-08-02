#Test case:

def test_canassertTrue():

    assert True

import replace_3

def test_replace():

    #Arrange:

    String1 = "abc"
    String2='ijk'
    expected = "ijc abk"
    #Actual:

    actual = replace_3.replace_3(String1,String2)

    #Assert:

    assert expected==actual
