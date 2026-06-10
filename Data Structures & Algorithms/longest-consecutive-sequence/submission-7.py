class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

        A  consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.
        The elements do not have to be consecutive in the original array.

        You must write an algorithm that runs in O(n) time.
        """
        # Brute force solution O(n^2)
        # Treat every number as the beginning of sequence
        # Compare length of each sequences
        # return: largest sequence in nums

        nums_set = set(nums)
        len_counter = 1 # current consecutive length count
        longest_best_so_far = 0 # keep track of longest consecutive list

    
        for idx in range(len(nums)):
            current = nums[idx] # current "starting" value
            
            while current + 1 in nums_set:
            # search through set if the current value + 1 exists
            # exit when value no longer found

                len_counter += 1 # update count

                # propogate current forward
                current = current + 1
                
            
            # Update max count condition
            if len_counter > longest_best_so_far:
                longest_best_so_far = len_counter

            # Reset length counter for next current value after each iteration
            len_counter = 1
        
        return longest_best_so_far
                
# Memory 8.3 MB
# Time: 47ms
# Time and Memory Complexity: O(n)         


    