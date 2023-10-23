def pow(number: float, power: int) -> float:

    if power == 1:
        return number
    return number * pow(number, power - 1)
