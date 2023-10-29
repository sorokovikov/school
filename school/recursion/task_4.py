def is_palindrome(str_: str) -> bool:

    return _is_palindrome(str_, 0, len(str_) - 1)


def _is_palindrome(str_: str, first: int, last: int) -> bool:

    if first == last or last < first:
        return True

    if str_[first] != str_[last]:
        return False

    return _is_palindrome(str_, first + 1, last - 1)
