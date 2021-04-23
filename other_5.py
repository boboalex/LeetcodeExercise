class Solution:
    def is_palind(self, x):
        if x % 10 == 0:
            return False
        res = 0
        while res < x:
            num = x % 10
            res = res * 10 + num
            x //= 10
        return x == res or x == res // 10

    def find_palind_nums(self, num_list):
        res = [x for x in num_list if self.is_palind(x)]
        return res


if __name__ == '__main__':
    s = Solution()
    num_list = [i for i in range(1, 1000)]
    res = s.find_palind_nums(num_list)
    print(res)