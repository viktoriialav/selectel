from pathlib import Path

import selectel_tests


def abs_path_from_root(path: str):
    return Path(selectel_tests.__file__).parent.parent.joinpath(path).absolute().__str__()
