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

        # Walk ptr_check with ptr_sum
        # as ptr_check walks, it will sum to ptr_sum +1 until end of list is reached
        # if no target is reached, we move ptr_home +1, reset ptr_check? 
        # if I reset ptr_check I must go back to 0 and make sure I don't use the same value

        # Should I store values seen?
        # I want to keep track of values visited so it is a quick lookup
        # set of number: idx
        # as check walks I can check sum,

        # Brute force: 
        # walk ptr_check until end of list, and compare with ptr_home
        # init ptr_home at start and check with ptr_check as if moves through list
        # Reset ptr_check to 0 and skip ptr_home idx
        # return List[int[idx1], int[idx2]]
        ptr_home = 0
        ptr_check = 1
        target_found = False

        # while true / false flag?
        while target_found == False:

            # Check indices and make sure they're not equal
            if ptr_home == ptr_check:
                ptr_check += 1

                # neg vals check? or does it matter?
            possible_target = numbers[ptr_home] + numbers[ptr_check]

            # Check if solved
            if possible_target == target:
                return [ptr_home+1, ptr_check+1]
                target_found = True

            # If not solved
            # Move ptr_check until end of the list
            elif ptr_check < len(numbers) - 1:
                ptr_check += 1 
            
            # If at the end of the list and no hits yet
            elif possible_target == target:
                return [ptr_home+1, ptr_check+1]
                target_found = True
            
            # Move to ptr_home and try again
            else:
                ptr_home +=1
                ptr_check = 0
        



            






