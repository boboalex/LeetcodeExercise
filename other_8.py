class Solution:
    def bubble_sort(self, num_list):
        """
        普通冒泡排序，只需要每次从头开始走，遇到比自己小的就置换，
        每轮迭代都把最大的放在最后面
        :param num_list:
        :return:
        """
        N = len(num_list)
        for i in range(N - 1, 0, -1):
            for j in range(0, i):
                if num_list[j] > num_list[j + 1]:
                    num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
        return num_list

    def bubble_sort1(self, num_list):
        """
        改进版1：设置一个记录是否有序的变量，如果在内层遍历时，没有任何交换
        就说明已经完全有序，那么直接返回即可
        :param num_list:
        :return:
        """
        N = len(num_list)

        for i in range(N - 1, 0, -1):
            isSorted = True
            for j in range(0, i):
                if num_list[j] > num_list[j + 1]:
                    num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
                    isSorted = False
            if isSorted:
                return num_list
        return num_list

    def bubble_sort2(self, num_list):
        """

        :param num_list:
        :return:
        """

        endPos = len(num_list) - 1
        while endPos > 0:
            thisTurnEnd = endPos
            for i in range(endPos):
                if num_list[i] > num_list[i + 1]:
                    num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
                    endPos = i
            if thisTurnEnd == endPos:
                return num_list
        return num_list


if __name__ == '__main__':
    s = Solution()
    num_list = [3, 44, 5, 15, 7, 2]
    res = s.bubble_sort1(num_list)
    print(res)