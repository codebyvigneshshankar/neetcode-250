class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = 2 * len(nums)
        new_list = []
        for i in range(len(nums)):
            new_list.append(nums[i])
        nums.extend(new_list) 
        return nums