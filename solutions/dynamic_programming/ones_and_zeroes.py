from typing import List

# m as number of zeroes. n as number of ones. THIS IS in 3D
def ones_and_zeroes_sol(strs: List[str], m:int, n:int) -> int:
    len_of_list = len(strs)
    dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len_of_list)]

    # for i in range(0, len(strs)):
    #     dp[0][0][i] = len(str)

    # the base case is 0, 0 - defaulted to 0 because you can't have any strings if no m or n.

    for index, words in enumerate(strs):
        num_zeroes = words.count("0")
        num_ones = words.count("1")

        for x in range(0, m + 1):
            for y in range(0, n + 1):
                if index == 0:
                    if x - num_zeroes >= 0 and y - num_ones >= 0:
                        dp[index][x][y] = 1
                    continue
                if x - num_zeroes >= 0 and y - num_ones >= 0:
                    dp[index][x][y] = max(dp[index - 1][x][y], dp[index - 1][x - num_zeroes][y - num_ones] + 1)
                else:
                    dp[index][x][y] = dp[index - 1][x][y]

    for layer in dp:
        for row in layer:
            print(row)
        print()  # Separate each layer visually

    return dp[len(strs)-1][m][n]