class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i,n in enumerate(nums):
            map[n] = i
        for i,n in enumerate(nums):
            compliment = target - n
            if compliment in map and map[compliment] != i:
                return [i, map[compliment]]
        return []
