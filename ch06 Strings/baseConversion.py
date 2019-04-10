# Write a program that performs base conversion. The string represents an integer in base b1.
# The output should be the string representing the integer in base b2.
# ex: If string is "617" b1 = 7 and b2 = 13, then result is "1A7"


# Naive
def cb_naive(num, b1, b2):
    position = len(num) - 1
    baseTen = 0
    for i in num:
        baseTen += int(i) * pow(b1, position)
        position -= 1
    exponent = 0
    converted_num = ''
    while baseTen >= 0:
        