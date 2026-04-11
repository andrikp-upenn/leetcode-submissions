class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute force O(n^2)

        result = []
        n = len(nums)
        for i in range(n):
            product = 1 # Reset for each i
            for j in range(n):
                if i == j:
                    continue
                product = product * nums[j]

            result.append(product)
        return result

# 
                