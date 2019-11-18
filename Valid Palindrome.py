class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaS = ""
        for x in s:
            if x.isalnum():
                alphaS+=x.lower()
        return alphaS == alphaS[::-1]