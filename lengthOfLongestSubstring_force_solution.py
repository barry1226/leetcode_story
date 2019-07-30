class Solution(object):
    @staticmethod
    def substr(s: str):
        for i in range(len(s)+1):
            for j in range(i, len(s)+1):
                yield s[i:j]

    @staticmethod
    def check_str(s):
        l = [c for c in s]
        if len(l) == len(list(set(l))):
            return len(l)
        else:
            return 0

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        for item in Solution.substr(s):
            r = Solution.check_str(item)
            if r > ret:
                ret = r
        return ret


print(Solution().lengthOfLongestSubstring("xnspusgdhiixqmbfjxjcvudjsuyibyebmwsiqyoygyxymzevypzvjegebeocfuftsxdixtigsieehkchzdflilrjqfnxz"))
