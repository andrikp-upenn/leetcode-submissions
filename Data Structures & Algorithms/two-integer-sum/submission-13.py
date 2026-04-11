class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Inputs: list of nums, target: int
        Outputs: [i,j] s.t. i + j target

        Nested for loop with high time complexity,
        compares ierations
        """
        # Allowable values
        seenNums = []
        # Builds a set of Nums with constraints
        for i in range(len(nums)):
            # the sum of the current and next val < target
            a = nums[i]
            # Final index fix
            if i+1 == None:
                continue
            else:
                b = nums[i]

            if a + b  < target:
                if a == b:
                    continue
                else:
                    seenNums.append(i)
                    seenNums.append(i+1)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                a = i
                b = j

                if nums[a] + nums[b] == target:
                    return [a,b]
                else:
                    continue
