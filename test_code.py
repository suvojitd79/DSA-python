import pytest
import array_


def test_anagrams():
    assert array_.anagrams('d o g', 'dog', type='bit') == True
    assert array_.anagrams(
        'geeksforgeeks', 'forgeeksgeeks', type='bit') == True
