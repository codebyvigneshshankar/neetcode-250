class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        store_map = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in store_map:
                if stack and stack[-1] == store_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack