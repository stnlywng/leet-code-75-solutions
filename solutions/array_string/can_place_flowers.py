from typing import List

# Question:

def can_place_flowers_solution(flowerbed: List[int], n: int) -> bool:
    last_flower = 0
    counter = 0

    for index, cur_soil in enumerate(flowerbed):
        distance_from_last_flower = index - last_flower
        # if it's in the beginning or the last flower is more than 1 away...
        past_flower_cond = (index == 0) or (distance_from_last_flower > 1)
        # if it's in the end or the next flower is more than 1 away...
        next_flower_cond = (index == len(flowerbed) - 1) or (flowerbed[index + 1] == 0)

        if cur_soil == 1:
            last_flower = index
        elif past_flower_cond and next_flower_cond:
            counter += 1
            last_flower = index

    return counter >= n