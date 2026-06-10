class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Given a string s, return true if it is a palindrome, otherwise return false.

        A palindrome is a string that reads the same forward and backward. 
        
        It is also case-insensitive and ignores all non-alphanumeric characters.

        Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).
        """

        # Brute force:
        # Make a copy of string, reverse it, and check for inequality

        reversed_str = ""

        # Start at len(s) -1, stop at 0, take a backwards step
        for char in range(len(s)-1, -1, -1):

            if s[char].isalnum() == True:
                palindrome = s[char].lower() + reversed_str
                reversed_str = palindrome

                forward_str = palindrome[::-1]


        if reversed_str == reversed_str[::-1]:
            return True
        else:
            return False