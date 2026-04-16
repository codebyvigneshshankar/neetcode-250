class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        l = 0
        sum = 0
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                res = min(res, r-l+1)
                sum = sum - nums[l]
                l += 1
        if res == float('inf'): return 0
        return res
