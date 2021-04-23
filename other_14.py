import random

class Solution:
    def rand_int(self):
        binary_res = 0
        for i in range(10):
            rand_num = random.randint(0, 1)
            binary_res = binary_res * 2 + rand_num
        binary_res /= 1024
        binary_res *= 1000
        res = int(binary_res)
        return res


if __name__ == '__main__':
    s = Solution()
    for i in range(10):
        res = s.rand_int()
        print(res)
    # print(random.randint(0,2))