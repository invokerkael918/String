class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """

    def longestPalindrome(self, s):
        # write your code here
        char_to_count = {}
        for ele in s:
            if ele in char_to_count:
                char_to_count[ele] += 1
            else:
                char_to_count[ele] = 1
        add_one = 0
        result = 0
        for ele in char_to_count:
            if char_to_count[ele] % 2 == 0:
                result += char_to_count[ele]
            else:
                if char_to_count[ele] > 1:
                    result += char_to_count[ele] - 1
                add_one = 1
        return result + add_one

if __name__ == '__main__':
    S =Solution().longestPalindrome("NTrQdQGgwtxqRTSBOitAXUkwGLgUHtQOmYMwZlUxqZysKpZxRoehgirdMUgy")
    print(S)


