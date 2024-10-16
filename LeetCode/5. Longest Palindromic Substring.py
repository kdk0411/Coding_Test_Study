class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""
        start, end = 0, 0

        for i in range(len(s)):
            odd_len = self.expandAroundCenter(s, i, i)  # 홀수
            even_len = self.expandAroundCenter(s, i, i + 1)  # 짝수
            max_len = max(odd_len, even_len)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1