class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        create a hashmap
        loop through array
        find compliment = target - num
        if compliment is found in hashmap
        return map[compliment], current i
        else add the value to hashmap
        """

        holderMap = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in holderMap:
                return [holderMap[compliment], i]
            holderMap[nums[i]] = i
        return []