import os


def find_all_files(root_path: str) -> list[str]:

    found_files: list[str] = []
    _find_all_files(found_files, root_path)
    return found_files


def _find_all_files(found_files: list[str], root_path) -> None:

    if os.path.isfile(root_path):
        found_files.append(root_path)
        return

    if os.path.isdir(root_path):
        for file in os.listdir(root_path):
            dir_path = os.path.join(root_path, file)
            _find_all_files(found_files, dir_path)
