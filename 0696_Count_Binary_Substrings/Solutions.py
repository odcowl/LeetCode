class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        s = s.replace('01', '0 1').replace('10', '1 0').split()
        s = map(len,s)
        return sum(min(a, b) for a, b in zip(s, s[1:]))
