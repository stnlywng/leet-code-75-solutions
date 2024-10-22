
def reverse_words_string_solution(s: str) -> str:
    # strip it in the beginning and check for an only-white-space string
    s = s.strip()

    if len(s) == 0:
        return ""

    current_word = ""
    total_length = 0

    index = 0
    end_point = len(s)

    # less than or equal because on the last word we want to add it to current_word, and then after have
    #     one more run where we do the adding. It's safe from out-of-bound because of ordered 'or' statement.
    while index <= end_point:
        if index == end_point or s[index] == " ":
            if len(current_word) > 0:
                s = current_word + " " + s
                end_point += len(current_word) + 1
                index += len(current_word) + 1
                total_length += len(current_word) + 1
                current_word = ""
        else:
            current_word += s[index]
        index += 1

    # comes as [word_1 word_2 word_3 ]word_3 word_2 word_1
    # we want to get rid of the last space after we chop with our substring method.
    s = s[0:total_length]
    s = s.strip()

    return s
