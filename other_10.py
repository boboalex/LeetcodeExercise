def reOrderCharacters(character_list):
    lowers = 0
    for i in range(len(character_list)):
        if character_list[i] > "Z":
            j = i
            while j > lowers:
                character_list[j], character_list[j - 1] = character_list[j - 1], character_list[j]
                j -= 1
            lowers += 1
    return character_list


class Solution:
    def reOrderArray(self, nums: list):
        odd_num = 0
        for i in range(len(nums)):
            if nums[i] & 1 == 1:
                j = i
                while j > odd_num:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                    j -= 1
                odd_num += 1
        return nums


if __name__ == '__main__':
    s = Solution()
    nums = [3, 1, 7, 2, 4, 5]
    character_list = ["Z", "a", "A", "s", "F", "k"]
    res = reOrderCharacters(character_list)
    print(res)
