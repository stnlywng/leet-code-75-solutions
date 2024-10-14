from solutions.two_pointers import move_zero_solution
from solutions.array_string import merge_string_alt_solution
from solutions.array_string import can_place_flowers_solution

# nums = [0, 2, 7, 0, 0, 11, 15, 0]
# result = move_zero_solution(nums)
# print(f"My Result: {nums}")

# word1 = "hellohello"
# word2 = "world"
# result = merge_string_alt_solution(word1, word2)
# print(f"My Result: {result}")

nums = [1, 0, 1, 0, 1]
nums2 = [1, 0, 0, 0, 1]
nums3 = [0, 0]
nums4 = [0, 0, 0, 0, 0]
result = can_place_flowers_solution(nums, 1)
print(f"My Result: {result}")
result = can_place_flowers_solution(nums2, 2)
print(f"My Result: {result}")
result = can_place_flowers_solution(nums3, 2)
print(f"My Result: {result}")
result = can_place_flowers_solution(nums4, 4)
print(f"My Result: {result}")