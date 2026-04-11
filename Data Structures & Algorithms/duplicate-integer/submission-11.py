class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values_seen = set()
        for i in nums:
            if i in values_seen:
                return True
            values_seen.add(i) # only runs if no duplicates are found yet
        return False # Only reaches here if loop finishes with no duplicates found

        print(i)

        