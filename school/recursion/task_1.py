def pow(number: float, power: int) -> float:

    if power == 1:
        return number

    if power == -1:
        return 1 / number

    if power > 1:
        return number * pow(number, power - 1)

    if power < 1:
        return 1 / number * pow(number, power + 1)

    # power == 0
    return 1
