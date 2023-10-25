def print_even_numbers(numbers: list) -> None:

    if len(numbers) == 0:
        return

    number = numbers.pop(0)

    if number % 2 == 0:
        print(number)
    print_even_numbers(numbers)
