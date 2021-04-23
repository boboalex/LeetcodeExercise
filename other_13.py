class Solution:
    def find_num(self, N):
        res = []
        res.append(3)
        for i in range(2, N):
            mid = i // 2
            for j in range(2, mid + 1):
                if i % j == 0:
                    break
                if j == mid:
                    res.append(i)
        return res

if __name__ == '__main__':
    s = Solution()
    res = s.find_num(100)
    print(res)