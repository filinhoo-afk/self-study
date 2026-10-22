# Задача: дан список целых чисел nums и число target.
# Нужно вернуть индексы двух элементов, сумма которых равна target.
# Один и тот же элемент дважды использовать нельзя. Ответ ровно один.


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  

        for i in range(len(nums)):
            number = nums[i]
            need = target - number

            if need in seen:
                return [seen[need], i]

            seen[number] = i