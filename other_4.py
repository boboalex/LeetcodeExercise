class Solution:
    def sort_nums(self, str_list, sub_str):
        res_dict = {}
        for s in str_list:
            res = self.find_substrings1(s, sub_str)
            res_dict[s] = res
        return sorted(str_list, key=lambda x: res_dict[x], reverse=True)

    # def find_substrings(self, s, sub_str):
    #     i = 0
    #     N = len(s)
    #     M = len(sub_str)
    #     ans_num = 0
    #     while i < N:
    #         j = -1
    #         while j < M - 1 and i < N and s[i] == sub_str[j + 1]:
    #             i += 1
    #             j += 1
    #         if j == M - 1:
    #             ans_num += 1
    #         if j == -1:
    #             i += 1
    #     return ans_num

    def find_substrings1(self, s, sub_str):
        N = len(s)
        M = len(sub_str)
        ans_num = 0
        for i in range(N - M + 1):
            for j in range(M):
                if s[i + j] != sub_str[j]:
                    break
                if j == M - 1:
                    ans_num += 1
        return ans_num


if __name__ == '__main__':
    s = Solution()
    l1 = ["abcab", "abcabcabc", "aaab", "abvabc"]
    res = s.sort_nums(l1, "abc")
    print(res)
