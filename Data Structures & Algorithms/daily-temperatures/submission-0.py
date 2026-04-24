class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        day_stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while day_stack and temp > day_stack[-1][0]:
                stackT, stackInd = day_stack.pop()
                res[stackInd] = i - stackInd
            day_stack.append((temp,i))
        return res