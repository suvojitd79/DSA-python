
'''
given two strings. checks if they're anagrams. you can ignore spaces & capitalization

O(nlogn) - sort
O(n) time + O(n) space - count
O(n) time + O(1) space -bit
'''


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


