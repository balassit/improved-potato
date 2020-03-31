def getDigitSum(num):
    res = 0
    while num >= 1:
        res = res + num % 10  # Get digit by digit
        num = num // 10
    return res


def equalDigitSum(A):
    n = len(A)
    if not A or n <= 1:
        return -1
    sumMap = {}  # map where digitSums are the keys and the max num of digitSums is temp stored
    res = -1  # since we have no negative numbers, we can safely use this as initial val
    for num in A:
        digitSum = getDigitSum(num)
        # if not in mapping, add the num
        if digitSum not in sumMap:
            sumMap[digitSum] = num
        else:
            # set result to either max of current sum, or curr num + stored num of digitSum
            res = max(res, sumMap[digitSum] + num)
            # update mapping value to max of curr val in map or curr num
            sumMap[digitSum] = max(sumMap[digitSum], num)
    return res


print(equalDigitSum([51, 71, 17, 42]))  # 93
print(equalDigitSum([42, 33, 60]))  # 102
print(equalDigitSum([51, 32, 43]))  # -1
# O(Nlog(k)) time because logK for getDigitSum where k is num of digits and N is length of list
# O(N) space complexity storing mappings
