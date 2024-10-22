from typing import List

def max_conse_ones_solution(nums: List[int], k: int) -> int:
    left = 0
    zero_count = 0
    highest_length = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        highest_length + max (highest_length, right - left + 1)

    return highest_length
