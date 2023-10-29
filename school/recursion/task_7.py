def find_second_max(numbers: list[int]) -> int:

    if numbers[0] > numbers[1]:
        first = numbers[0]
        second = numbers[1]
    else:
        first = numbers[1]
        second = numbers[0]

    return _find_second_max(numbers, 2, first, second)


def _find_second_max(numbers: list[int], index: int, first: int, second: int) -> int:

    if len(numbers) == index:
        return second

    if numbers[index] <= first and numbers[index] > second:
        second = numbers[index]
    if numbers[index] > first:
        second, first = first, numbers[index]

    return _find_second_max(numbers, index + 1, first, second)


# imperative version
#
# for i in range(2, len(numbers)):
#     if numbers[i] <= first and numbers[i] > second:
#         second = numbers[i]
#     if numbers[i] > first:
#         second, first = first, numbers[i]
#
# return second
