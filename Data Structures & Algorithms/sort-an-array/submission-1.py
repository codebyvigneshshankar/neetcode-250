class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        else:
            pivot = nums[len(nums) // 2]
        
        values_greater = []
        values_middle = []
        values_lower = []
        for num in nums:
            if num > pivot:
                values_greater.append(num)
            elif num < pivot:
                values_lower.append(num)
            else:
                values_middle.append(num)
        return self.sortArray(values_lower) + values_middle + self.sortArray(values_greater)
        