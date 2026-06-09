class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

        A  consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.
        The elements do not have to be consecutive in the original array.

        You must write an algorithm that runs in O(n) time.
        """

        # O(n) solution,
        # Finding worthy starting values
        # Not iterating through each value

        nums_set = set(nums)
        len_counter = 1
        len_best_so_far = 0

        for idx in range(len(nums)):
            # Initalize current value
            current = nums[idx]
            
            # A valid starting sequence must not have a number before it
            if current - 1 in nums_set:
                continue

            # While condition to calculate max consecutive length
            while current + 1 in nums_set:
                # if value found, propogate counter
                len_counter += 1

                # propogate current value
                current = current + 1

            if len_counter > len_best_so_far:
                len_best_so_far = len_counter
            
            # reset counter
            len_counter = 1

        
        return len_best_so_far

            