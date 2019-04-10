### BRUTE FORCE CASTING METHOD
### ITS SHIT
def multiTwo(x, y):
    num1, num2 = "", ""
    productArray = []
    for i in x:
        num1 += str(i)
    for j in y:
        num2 += str(j)
    product = str(abs(int(num1) * int(num2)))
    for k in product:
        productArray.append(int(k))
    if int(num1) < 0 or int(num2) < 0:
        productArray[0] = productArray[0] * -1
        return productArray
    else:
        return productArray


### "GRADE SCHOOL" METHOD
def multiply(num1, num2):
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    result = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10
    
    # Remove the leading zeroes.
    result = result[next((i for i, x in enumerate(result)
                    if x != 0), len(result)):] or [0]
    return [sign * result[0]] + result[1:]
            