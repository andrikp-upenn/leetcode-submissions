class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        INPUTS: list: nums, k: k-most frequent elements
        OUTPUTS: list[first most repeated #, kth most repeated $]

        Req: O(n) complexity

        Constraints:
        1 <= nums.length <= 10^4.
        -1000 <= nums[i] <= 1000
        1 <= k <= number of distinct elements in nums.

        """
        # Create a hashmap that sorts the int from greatest to least
        seenVals = {} # Stores seen variables

        for i in nums:
            seenVals[i] = 1 + seenVals.get(i,0)
            
        sorted_nums = sorted(seenVals, key=lambda x: seenVals[x], reverse = True)

        return sorted_nums[:k]
        