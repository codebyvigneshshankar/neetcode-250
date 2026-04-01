class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in range(len(strs)):
            sortedS = ''.join(sorted(strs[i]))
            res[sortedS].append(strs[i])
        return list(res.values())