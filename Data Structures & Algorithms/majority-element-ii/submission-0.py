class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        countMap = {}
        countList = []
        for i in range(len(nums)):
            countMap[nums[i]] = 1 + countMap.get(nums[i], 0)
        for key in countMap:
            if countMap[key] > len(nums) // 3:
                countList.append(key)
        return countList
