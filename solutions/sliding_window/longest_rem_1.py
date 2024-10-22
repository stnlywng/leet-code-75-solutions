from typing import List

def longest_rem_one_sol(nums: List[int]) -> int:
    left = 0
    right = 0

    longest = 0
    zero_count = 0

    # Conditions:
    # zero_count <= 1
    # left <= right
    # right <= len(nums) - 1
    # left >= 0

    # move right until conditions break.
    # move the left until conditions are okay again.

    # if right can't go on anymore: right == len(nums) - 1 and conditions aren't broken. we can take it.
    # if left can't go anymore without breaking condition, we stop.


    while right < len(nums):
        if nums[right] == 0 and zero_count == 1:
            longest = max(longest, right - left - 1)
            zero_count += 1
            while zero_count == 2:
                left += 1
                if nums[left - 1] == 0:
                    zero_count -= 1
        elif nums[right] == 0 and zero_count == 0:
            zero_count += 1

        right += 1

        if right == len(nums) and zero_count <= 1:
            longest = max(longest, right - left - 1)

    return longest