# Для заданной строки s верните true если она является палиндромом, или false в противном случае.
# Задача на leetcode.com
# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = []

        for x in s:
            if x.isalnum():
                letters.append(x.lower())

        s = ''.join(letters)

        return s == s[::-1]