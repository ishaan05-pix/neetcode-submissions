
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        hashset = set()
        max_len = 0

        while r < len(s):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1

            hashset.add(s[r])
            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len