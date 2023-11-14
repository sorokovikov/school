def GenerateBBSTArray(a: list[int]) -> list[int]:

    a.sort()
    bst_array = [0] * len(a)

    fill_balanced_list(a, 0, bst_array)
    return bst_array


def fill_balanced_list(source_list: list[int], dest_index: int, balanced_list: list[int]):

    if len(source_list) == 0:
        return

    middle_index = len(source_list) // 2
    balanced_list[dest_index] = source_list[middle_index]

    fill_balanced_list(source_list[:middle_index], (2 * dest_index + 1), balanced_list)
    fill_balanced_list(source_list[middle_index + 1:], (2 * dest_index + 2), balanced_list)
