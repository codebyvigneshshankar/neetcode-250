class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_map = {}
        result = 0
        l = 0
        maxf = 0

        for r in range(len(s)):
            count_map[s[r]] = 1 + count_map.get(s[r], 0)
            maxf = max(maxf, count_map[s[r]])

            while (r-l+1) - maxf > k:
                count_map[s[l]] -= 1
                l += 1
            result = max(result, r-l+1)
        return result 