def sum_number_digits(number: int) -> int:

    if number // 10 == 0:
        return number
    return number % 10 + sum_number_digits(number // 10)
