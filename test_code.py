# py.test -o log_cli=True
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


def test_missing2array():
    assert array_.missing2array([2, 1, 56, 9, 6, 7], [2, 1, 9, 6, 7]) == 56
    assert array_.missing2array([1, 2, 3, 4, 5, 6], [5, 6, 2, 3, 4]) == 1


def test_maxsum():
    assert array_.maxsum([-2, -3, 4, -1, -2, 1, 5, -3]) == (7, 2, 6)
    assert array_.maxsum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == (6, 3, 6)
    assert array_.maxsum([-1, 1]) == (1, 1, 1)


def test_sentence_reversal():
    assert array_.sentence_reversal(
        'i love coding python  ') == 'python coding love i'
    assert array_.sentence_reversal(
        'i am the fuck**g ninja') == 'ninja fuck**g the am i'


def test_compression():
    assert array_.compression('AAABB') == 'A3B2'
    assert array_.compression('AAABBCCDA') == 'A4B2C2D1'
    assert array_.compression('ABC') == 'A1B1C1'
    assert array_.compression('ABCABC') == 'A2B2C2'
    assert array_.compression('AAABBBCCAA') == 'A5B3C2'


def test_isunique():
    assert array_.isunique('ABACD') == False
    assert array_.isunique('abcde') == True
    assert array_.isunique('abcded') == False
