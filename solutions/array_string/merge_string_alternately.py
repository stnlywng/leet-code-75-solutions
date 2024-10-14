from typing import List

def merge_string_alt_solution(word1: str, word2: str) -> str:
    # figure out the lengths.
    word1_length = len(word1)
    word2_length = len(word2)

    accum = ""

    # if max_length is 3, then we want to go 0, 1, 2.
    # range is not inclusive of the last one!
    for index in range(0, max(word1_length, word2_length)):
        if index < word1_length:
            accum += word1[index]
        if index < word2_length:
            accum += word2[index]

    return accum