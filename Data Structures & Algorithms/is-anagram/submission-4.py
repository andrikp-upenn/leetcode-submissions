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

# 25/25 test cases @ 8.7 MB, 36ms
# Time: O(n log n) — sorting is not free, it takes n log n operations
# Space: O(n) — storing the two sorted arrays


        
        