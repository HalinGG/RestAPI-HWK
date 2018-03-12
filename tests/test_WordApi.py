import myflaskapp.myflaskapp

def test_zero_words():
    assert myflaskapp.myflaskapp.getCount("") == "0"

def test_three_words():
    assert myflaskapp.myflaskapp.getCount("One two three") == "3"
