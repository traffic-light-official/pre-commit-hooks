"""pre-commit hook that detects the presence of fuzzy messages in translation (po, gettext) files."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    """Входная точка скрипта."""
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check')
    args = parser.parse_args(argv)

    fuzzy_files = []

    for filename in args.filenames:
        content = Path(filename).read_bytes()
        if b'#, fuzzy' in content:
            fuzzy_files.append(filename)

    if fuzzy_files:
        for fuzzy_file in fuzzy_files:
            print(f'Fuzzy translation found: {fuzzy_file}')  # noqa: T201
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
