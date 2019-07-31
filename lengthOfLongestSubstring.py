class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret, r = 0, 0
        left = 0
        char_set = set()
        for right in range(len(s)):
            r += 1
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
                r -= 1
            char_set.add(s[right])
            if r > ret:
                ret = r
        return ret


print(Solution().lengthOfLongestSubstring("fgjrauieghnui"))
