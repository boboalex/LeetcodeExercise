class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        N1, N2 = len(v1), len(v2)
        for i in range(max(N1, N2)):
            a = int(v1[i]) if i < N1 else 0
            b = int(v2[i]) if i < N2 else 0
            if a < b:
                return -1
            elif a > b:
                return 1
        return 0


if __name__ == '__main__':
    s = Solution()
    res = s.compareVersion("7.5.2.4", "7.5.3")
    print(res)
