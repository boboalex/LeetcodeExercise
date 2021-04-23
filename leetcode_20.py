class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack


class Solution1:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        brace_dict = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stk = []
        for c in s:
            if c in brace_dict:
                if not stk or stk[-1] != brace_dict[c]:
                    return False
                stk.pop()
            else:
                stk.append(c)
        return not stk

    def isValid1(self, s: str) -> bool:
        brace_dict = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        stk = []
        for c in s:
            if c in brace_dict:
                pre = stk.pop()
                if brace_dict[c] != pre:
                    return False
            else:
                stk.append(c)
        return not stk

if __name__ == '__main__':
    # s = Solution()
    # res = s.isValid("()[]{}")
    # res1 = s.isValid("([)]{}")
    # print(res1)
    s = Solution1()
    res = s.isValid1("()[]{}")
    print(res)