import pytest
import array_


def test_anagrams():
    assert array_.anagrams('d o g', 'dog', type='bit') == True
    assert array_.anagrams(
        'geeksforgeeks', 'forgeeksgeeks', type='bit') == True


def test_pairsum():
    assert array_.pairsum([1, 3, 2, 2], 4)[1] == 2
    assert array_.pairsum([1, 4, 45, 6, 10, 8], 16)[1] == 1
    assert array_.pairsum([1, 3, 23, 9, 0], 9)[1] == 1
