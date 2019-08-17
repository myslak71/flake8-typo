"""Typo checker module."""
import ast
import optparse
from io import StringIO
from typing import Generator, Tuple, List
import tokenize

from hunspell import Hunspell

from flake8_typo import __version__

import pkg_resources
from flake8.options.manager import OptionManager
from flake8.utils import stdin_get_value
from pycodestyle import readlines
import tokenize


def get_comments(
        source
) -> Generator[Tuple[Tuple[int, int], Tuple[int, int], List[str]], None, None]:
    """Get a list of comments and docstrings."""
    prev_token_type = tokenize.INDENT

    for token in tokenize.generate_tokens(StringIO(source).readline):
        if token.type == tokenize.COMMENT or (
                token.type == tokenize.STRING and prev_token_type == tokenize.INDENT
        ):
            yield (token.start, token.end, token.string.split('\n'))
        prev_token_type = token.type


class TypoChecker:
    """Typo checker class."""

    name = 'flake8-typo'
    options = optparse.Values()
    version = __version__

    def __init__(self, tree: ast.Module, filename: str) -> None:
        """Initialize class values. Parameter `tree` is required by flake8."""
        self.filename = filename

    def run(self) -> Generator[Tuple[int, int, str, type], None, None]:
        """Run the linter and return a generator of errors."""
        with open(self.filename, 'r') as file:
            comments = get_comments(file.read())

        # for comment in comments
        z = list(comments)

        spell = Hunspell()
        x = spell.spell(z[1][2][0])
        print(x)
        yield (0, 0, f'KOL001 Bad language found: ', TypoChecker)

    @classmethod
    def parse_options(cls, options: optparse.Values) -> None:
        """Get parser options from flake8."""
        cls.options = options

    def _get_file_content(self) -> List[str]:
        """Return file content as a list of lines."""
        if self.filename in ('stdin', '-', None):
            return stdin_get_value().splitlines(True)
        else:
            return readlines(self.filename)
