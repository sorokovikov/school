def print_even_index_elements(list_: list) -> None:

    if len(list_) < 2:
        return

    print(list_.pop(0))
    list_.pop(0)
    print_even_index_elements(list_)
