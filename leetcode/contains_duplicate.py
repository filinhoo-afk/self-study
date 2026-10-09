# Учитывая массив целых чисел, numsвернитеtrue, если какое-либо значение появляется по крайней мере дважды в массиве, и верните false, если каждый элемент различен.
# Задача на leetcode.com 
# https://leetcode.com/problems/contains-duplicate/description/


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:        
        return len(nums) != len(set(nums))