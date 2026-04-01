class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_list = []
        for i in range(len(nums)):
            new_list.append(nums[i])
        nums.extend(new_list) 
        return nums