def fractionToDecimal(self, numerator: int, denominator: int) -> str:
    if numerator == 0:
        return str(0)

    fraction = list()
    # if either is negative, but not both
    if (numerator < 0 or denominator < 0) and not (numerator < 0 and denominator < 0):
        fraction.append("-")

    dividend = abs(numerator)
    divisor = abs(denominator)

    fraction.append(str(dividend // divisor))
    remainder = dividend % divisor
    # whole number
    if remainder == 0:
        return "".join(fraction)
    # decimal remainder
    fraction.append(".")

    rem_dict = {}
    while remainder != 0:
        if remainder in rem_dict:
            fraction.insert(rem_dict[remainder], "(")
            fraction.append(")")
            break

        rem_dict[remainder] = len(fraction)
        remainder *= 10
        fraction.append(str(remainder // divisor))
        remainder %= divisor
    return "".join(fraction)


print(fractionToDecimal(1, 2))
