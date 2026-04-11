class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_s = sorted(s)
        sort_t = sorted(t)


        # If using the sorted function, it creates an array,
        # That arranges the letters in order
        if sort_s == sort_t:
            return True
        else:
            return False

        # Can also create a hashmap / dictionary to check repeated values
        # Solution #2

        
        