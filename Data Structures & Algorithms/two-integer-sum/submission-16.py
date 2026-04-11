class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Inputs: list of nums, target: int
        Outputs: [i,j] s.t. i + j target

        Nested for loop with high time complexity,
        compares ierations
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                a = i
                b = j

                if nums[a] + nums[b] == target:
                    return [a,b]
                else:
                    continue
#Nested for loop solution: 23/23 test cases @ 8.2MB, 28ms

