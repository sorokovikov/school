def print_even_numbers(numbers: list) -> None:

    _print_even_numbers(numbers, 0)


def _print_even_numbers(numbers: list, index: int) -> None:

    if len(numbers) == index:
        return

    if numbers[index] % 2 == 0:
        print(numbers[index])
    _print_even_numbers(numbers, index + 1)
