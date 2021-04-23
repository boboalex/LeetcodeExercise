class Solution:
    def find_sequence(self, num_list):
        N = len(num_list)
        res = []
        i = 0
        while i < N - 1:
            j = i
            while j + 1 < N and num_list[j + 1] - num_list[i] == j + 1 - i:
                j += 1

            if j != i:
                res.append([num_list[i], num_list[j]])
                i = j + 1
            else:
                i += 1
        return res


if __name__ == '__main__':
    s = Solution()
    num_list = [3, 2, 7, 8, 1, 4, 10, 11, 12]
    res = s.find_sequence(num_list)
    print(res)
