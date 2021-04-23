class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        res = ""
        while i >= 0 or j >= 0:
            a = int(num1[i]) if i >= 0 else 0
            b = int(num2[j]) if j >= 0 else 0
            sum = a + b + carry
            res = str(sum % 10) + res
            carry = 1 if sum > 9 else 0
            i -= 1
            j -= 1
        if carry == 1:
            res = "1" + res
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.addStrings("96043", "5582")
    print(res)