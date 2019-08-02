# Test case:

def test_canassertTrue():

    assert True

import join_k

def test_join_k():

    #Arrange:

    String = 'udhaikumar'
    k=1
    expected='ur'

    #Actal:

    actual = join_k.join_k(String,k)

    #Assert:

    assert expected==actual