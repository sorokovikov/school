def is_palindrome(str_: str) -> bool:

    if len(str_) <= 1:
        return True

    if str_[0] != str_[-1]:
        return False

    return is_palindrome(str_[1:-1])
