class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        for i in range(length-1):
            j = i + 1
            while j < length:
                if nums[i] == nums[j]:
                    return True 
                j = j + 1
        return False
        