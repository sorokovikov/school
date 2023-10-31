def generate_balanced_parentheses_list(count: int) -> list[str]:

    balanced_parentheses: list[str] = []
    _generate_balanced_parentheses(0, 0, count, "", balanced_parentheses)
    return balanced_parentheses


def _generate_balanced_parentheses(
    on_left: int, on_right: int, count: int, str_: str, balanced_parentheses: list[str]
) -> None:

    if len(str_) == count * 2:
        balanced_parentheses.append(str_)
        return

    if on_left < count:
        _generate_balanced_parentheses(on_left + 1, on_right, count, str_ + "(", balanced_parentheses)

    if on_right < on_left:
        _generate_balanced_parentheses(on_left, on_right + 1, count, str_ + ")", balanced_parentheses)
