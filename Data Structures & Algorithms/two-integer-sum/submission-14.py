class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Inputs: list of nums, target: int
        Outputs: [i,j] s.t. i + j target
        """
        # seen numbers in a list
        seenNums = []

        for i in range(len(nums)):
            need_val = target - nums[i] # what number is needed
            if need_val in seenNums:
                j = nums.index(need_val)
                return[j,i]
            else:
                seenNums.append(nums[i])

#23/23 test cases @ 7.7MB, 27ms


