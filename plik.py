"""SIEMANKO."""

from itertools import permutations, chain
from typing import List

import pkg_resources


def _get_lang_choices(cls) -> List[str]:
    """
    Get language choices.

    Remove .dat from language filenames and generate all language combinations.
    """
    languages = [
        lang_file.replace('.dat', '')
        for lang_file in pkg_resources.resource_listdir(__name__, cls.SWEAR_DATA_DIR)
    ]
    lang_permutations = [
        permutations(languages, number)
        for number, language in enumerate(languages, 1)  # Comment
    ]

    # Super
    # Long comment

    return [','.join(permutation) for permutation in chain(*lang_permutations)]
