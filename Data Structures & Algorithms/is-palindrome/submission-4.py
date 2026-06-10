class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Given a string s, return true if it is a palindrome, otherwise return false.

        A palindrome is a string that reads the same forward and backward. 
        
        It is also case-insensitive and ignores all non-alphanumeric characters.

        Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).
        """
        # Two pointer solution O(1)
        # Check the start and end of the string.
        # and move toward eachother

        start = 0
        end = len(s) - 1

        while start < end:
            # check for alphanumerical chars

            # Check if they're not alnum
            # if False --> move both
            if s[start].isalnum() == False:
                start += 1
            elif s[end].isalnum() == False:
                end -= 1
            
            # If True --> check and continue
            elif s[start].lower() == s[end].lower():
                start += 1
                end -= 1
            else:
                return False

            # If exit loop successfully:
        return True

                    


                        
                
                    
            

