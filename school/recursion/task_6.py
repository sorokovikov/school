def print_even_index_elements(list_: list) -> None:

    _print_even_index_elements(list_, 0)


def _print_even_index_elements(list_: list, index: int) -> None:

    if len(list_) == index:
        return

    if index % 2 == 0:
        print(list_[index])
    _print_even_index_elements(list_, index + 1)
