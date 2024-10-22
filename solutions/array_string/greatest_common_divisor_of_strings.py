import math

# If they have a match it MUST match starting from the beginning!
# And the repeating part will be the GCD of the two lengths. 6 and 4 must have a thing of 2.

def greatest_com_dev_str_solution(str1: str, str2: str) -> str:
    divisor = ""

    greater_len = max(len(str1), len(str2))
    lesser_len = min(len(str1), len(str2))

    GCD = math.gcd(greater_len, lesser_len)

    for index in range(0, GCD):
        if str1[index] == str2[index]:
            divisor += str1[index]
        else:
            return ""

    # replaces all instances of divisor in the string with nothing.
    string1_remove_all_divisor = str1.replace(divisor, "")
    string2_remove_all_divisor = str2.replace(divisor, "")

    if string1_remove_all_divisor == "" and string2_remove_all_divisor == "":
        return divisor
    else:
        return ""
