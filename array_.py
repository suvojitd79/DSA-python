
'''
given two strings. checks if they're anagrams. you can ignore spaces & capitalization
'''

# O(nlogn) - sort
# O(n) time + O(n) space - count
# O(n) time + O(1) space -bit


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
