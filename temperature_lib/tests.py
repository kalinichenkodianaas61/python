from temperature_lib import is_frost, average_temp, to_faranheit_all, first_frost, frost_only

def test_all():
    # test cases for is_frost, average_temp, to_faranheit_all, first_frost, frost_only functions

    # test cases for is_frost
    assert is_frost(-6.7) == True
    assert is_frost(0) == False
    assert is_frost(23) == False

    # test cases for average_temp
    assert average_temp([1.3, 12, 11, 16]) == 9.5
    assert average_temp([]) == None
    assert average_temp([-6, 0, 6]) == 0

    # test cases for to_faranheit_all
    assert to_faranheit_all([0, 100]) == [32.0, 212.0]
    assert to_faranheit_all([]) == []
    assert to_faranheit_all([-30]) == [-22.0]

    # test cases for first_frost
    assert first_frost([-6, 0, 6]) == 0
    assert first_frost([]) == -1
    assert first_frost([1, 2, 22]) == -1

    # test cases for frost_only
    assert frost_only([-6, 0, 6]) == [-6]
    assert frost_only([]) == []
    assert frost_only([1, 2, 22]) == []

    print("all tests passed")

if __name__ == "__main__":
    test_all()    

