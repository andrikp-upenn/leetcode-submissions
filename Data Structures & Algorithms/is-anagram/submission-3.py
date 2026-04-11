class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = {} # key: str, val: repeated string
        set_t = {}

        # iterate over each string, check if string exist, 
        # add the current dict value, else 0
        for i in s:
            set_s[i] = 1 + set_s.get(i, 0)
        for j in t:
            set_t[j] = 1 + set_t.get(j, 0)

        # check that dictionaries are equal
        if set_s == set_t:
            return True
        else:
            return False

# 25/25 test cases @ 8.0 MB, 46ms
# Time: O(n) — just one pass through each string
# Space: O(n) — storing the two dictionaries

    
        
        
    


