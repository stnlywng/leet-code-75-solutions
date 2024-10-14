from typing import List

def move_zero_solution(nums: List[int]) -> None:
    track_last_zero_index = len(nums) # think of last 0 (don't swap here) as one after the array.
    index = 0 # setup for the "for-loop"

    while index < track_last_zero_index:
        item = nums[index] # get the item

        if item == 0:
            # keep swapping until the current + 1 is the last-zero. bring it to the end!
            for current in range(index, track_last_zero_index - 1):
                nums[current], nums[current + 1] = nums[current + 1], nums[current]

            track_last_zero_index -= 1
        else:
            # put it in the else block because if item is 0 don't want to increment. might've swapped with a 0 right away!
            index += 1