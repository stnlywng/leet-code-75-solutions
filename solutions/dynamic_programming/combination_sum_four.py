from typing import List

def combo_sum_four_sol(nums: List[int], target: int) -> int:
    dp = [0] * (target + 1)
    dp[0] = 1

    for index in range(0, target + 1):
        for number in nums:
            new_target = index - number

            if new_target == 0:
                dp[index] += 1
            elif new_target > 0:
                dp[index] += dp[new_target]

    return dp[target]
