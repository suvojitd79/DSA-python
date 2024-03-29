'''
given two strings. checks if they're anagrams. you can ignore spaces & capitalization

O(nlogn) - sort
O(n) time + O(n) space - count
O(n) time + O(1) space -bit
'''


from collections import OrderedDict


def anagrams(s1, s2, type='sort'):
    if not type in ['sort', 'count', 'bit']:
        raise ValueError('{0} can not be applied '.format(type))
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    if len(s1) != len(s2):
        return False
    elif type == 'sort':
        return sorted(s1) == sorted(s2)
    elif type == 'bit':
        ans = 0
        for i in range(len(s1)):
            ans = ans ^ ord(s1[i]) ^ ord(s2[i])
        return ans == 0


'''
given a list of integers and an integer(k), return the number of pairs such that each pair sum to the given value k
'''


def pairsum(l, k):
    if len(l) == 0:
        return
    d_ = dict()
    _ = []
    for v in l:
        if v in d_:
            d_.update({v: d_[v]+1})
        else:
            d_[v] = 1
    for v in l:
        if k-v in d_ and ((v == k-v and d_[k-v] > 1) or (v != k-v and d_[k-v] > 0)):
            _.append([v, k-v])

    for __ in _:
        if _.count(__) > 1:
            _.remove(__)
        elif [__[1], __[0]] in _:
            _.remove([__[1], __[0]])
    return _, len(_)


'''
given two arrays, where second array is constructed by shuffling the 1st array and deleting one random element from the first array, find the deleted element
'''


def missing2array(l1, l2):
    ans = 0
    for x in l1:
        ans ^= x
    for x in l2:
        ans ^= x
    return ans


'''
given an array, find the contiguous subarray with max-sum
'''


def maxsum(l):
    if len(l) == 0:
        return float('-inf')
    max_so_far = l[0]
    max_global = l[0]
    start = end = 0
    for x in range(1, len(l)):

        if l[x] > 0 and (l[x] + max_so_far < l[x]):
            max_so_far = l[x]
            start = x
        else:
            max_so_far += l[x]

        if max_so_far > max_global:
            max_global = max_so_far
            end = x

    return max_global, start, end


'''
sentence reversal
i: i love coding
o: coding love i
'''


def sentence_reversal(s=''):
    s = s.strip()  # remove the leading & trailing white space characters
    l = s.split()
    l.reverse()
    return ' '.join(l)


'''
string compression
i: AABBSSSSA
o: A3B2S4
'''


def compression(s):
    d = OrderedDict()
    for _ in s:
        if _ in d:
            d.update({_: d[_]+1})
        else:
            d.update({_: 1})
    ans = ''
    for _ in d:
        ans += _+str(d[_])
    return ans


'''
unique chars
i: abcd -> true
i: abacd -> false
'''


def isunique(s):
    _ = set()
    for x in s:
        if x in _:
            return False
        else:
            _.add(x)
    return True


