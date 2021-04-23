class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        if len(s) != len(t):
            return False
        for i, j in zip(s, t):
            if (i in s_dict and s_dict[i] != j) or (j in t_dict and t_dict[j] != i):
                return False
            s_dict[i] = j
            t_dict[j] = i
        return True


if __name__ == '__main__':
    s = "egg"
    t = "add"
    for i, j in zip(s, t):
        print(i, j)
