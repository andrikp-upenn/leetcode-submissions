class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Given an array of integers numbers that is sorted in non-decreasing order.

        Return the indices (1-indexed) of two numbers, [index1, index2], such that they add
        up to a given target number target and index1 < index2.

        Note that index1 and index2 cannot be equal, therefore you may not use the same element twice

        There will always be exactly one valid solution.

        Your solution must use O(1) additional space.

        Inputs:
        numbers: List[int]
        target: int

        Returns:
        List[int] --> [idx1, idx2]

        Constraints:
        2 <= numbers.length <= 1000
        -1000 <= numbers[i] <= 1000
        -1000 <= target <= 1000
        """

        # O(n), O(1) solution
        # Array is in increasing order,
        # start, end pointers at opposite ends
        # if the sum < target --> move end pointer inwards
        # if the sum > target --> move right pointer inwards
        # repeat until target == sum

        start = 0
        end = len(numbers) - 1

        while True: 

            current_sum = numbers[start] + numbers[end]
            if current_sum > target:
                end -=1

            elif current_sum < target:
                start +=1
            
            elif current_sum == target:
                return [start + 1, end + 1]


# 24/24 test cases
# Memory 8MB
# Time: 27ms
# Beats 82.50%

