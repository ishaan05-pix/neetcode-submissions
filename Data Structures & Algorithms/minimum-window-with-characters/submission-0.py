
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        count = {}

        # Count the required frequency of each character in t
        for ch in t:
            count[ch] = count.get(ch, 0) + 1

        countS = {}
        have = 0
        need = len(count)

        l = 0
        min_len = float("inf")
        result = ""

        for r in range(len(s)):
            ch = s[r]
            countS[ch] = countS.get(ch, 0) + 1

            # Did this character just satisfy its requirement?
            if ch in count and countS[ch] == count[ch]:
                have += 1

            # While all requirements are satisfied, shrink the window
            while have == need:
                window_len = r - l + 1

                if window_len < min_len:
                    min_len = window_len
                    result = s[l:r + 1]

                left_char = s[l]
                countS[left_char] -= 1

                # Did removing this character break a requirement?
                if (left_char in count and
                        countS[left_char] < count[left_char]):
                    have -= 1

                l += 1

        return result