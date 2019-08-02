# Test Case:

def test_canassertTrue():

    assert True

import join_str

def test_join_str():

    #Arrange:

    String = 'udhaikumar'
    expected='udar'

    #Actal:

    actual = join_str.join(String)

    #Assert:

    assert expected==actual