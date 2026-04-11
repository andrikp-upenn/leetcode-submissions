class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        INPUT: Given an integer array nums,
        OUTPUT: Return an array output where output[i] = 
        product of all elem. of nums except nums[i]

        Constrains: Constraints:
        2 <= nums.length <= 1000
        -20 <= nums[i] <= 20

        example:
        nums = [1, 2, 4, 6]
        i = 0 --> 2*4*6 = 48
        i = 1 --> 1*4*6 = 24
        i = 2 --> 1*2*6 = 12
        O(n) wihtout using division operation
        """
        result = []
        # pre-compute two passes, then multiply them to have O(n) complexity
        # Prefix iterates from Left --> right initializing it with [1]
        # Suffix iterates backwards from Right --> left init [1] & 
        prefix = [1] * len(nums) # initialize prefix as a ls of 1
        for i in range(1, len(nums)):
            # Pass 1: go LEFT to RIGHT, build prefix products
            # idea: multiply the list as we go
            prefix[i]= prefix[i-1] * nums[i-1]

        # Pass 2: go RIGHT to LEFT, build suffix products
        suffix = [1] * len(nums) 
        for i in range(len(nums)-2, -1, -1): # Start second value from the right
        # stop at -1 & move backwards
            suffix[i] = suffix[i+1] * nums[i+1]

        # Combine left and right results
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])
        return result

# Time complexity: O(n) 
# Space complexity: O(n)
# 19/19 test cases @ 42ms / 7.9MB - Optimal Sol.



            






