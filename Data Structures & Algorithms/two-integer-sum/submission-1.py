class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Inputs: list of nums, target: int
        Outputs: [i,j] s.t. i + j target
        """
        # seen values and their indeces, maybe dict and key = num, val = idx
        seenNums = []

        for i in range(len(nums)):
            need_val = target - nums[i] # what number is needed
            if need_val in seenNums:
                j = nums.index(need_val)
                return[j,i]
            else:
                seenNums.append(nums[i])


