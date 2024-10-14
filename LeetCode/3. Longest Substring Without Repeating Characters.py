class Solution(object):
    def lengthOfLongestSubstring(self, s):
        check = set()
        pointer = 0
        ret = 0

        for i in range(len(s)):
            while s[i] in check:
                check.remove(s[pointer])
                pointer += 1
            check.add(s[i])
            ret = max(ret, i - pointer + 1)
        return ret