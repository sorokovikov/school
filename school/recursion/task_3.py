def list_length(list_: list) -> int:

    if len(list_) == 0:
        return 0

    if len(list_) == 1:
        return 1

    list_.pop(0)
    return 1 + list_length(list_)
