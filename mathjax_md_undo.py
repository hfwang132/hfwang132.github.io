#!/usr/bin/env python3
import argparse
import re
from pathlib import Path
import sys

def build_undo_regex(undo_map: dict) -> re.Pattern:
    """Compile a single alternation regex over the *keys* (escaped forms)."""
    # Longest-first to handle overlaps like r'\*\*' vs r'\*'
    alternation = "|".join(sorted(map(re.escape, undo_map.keys()), key=len, reverse=True))
    return re.compile(alternation)

def undo_replacements_to_file(src_path: Path, dst_path: Path, undo_map: dict, overwrite: bool = False) -> None:
    if src_path == dst_path:
        print("Error: output path must be different from input path.", file=sys.stderr)
        sys.exit(1)
    if dst_path.exists() and not overwrite:
        print(f"Error: output file '{dst_path}' already exists. Use --force to overwrite.", file=sys.stderr)
        sys.exit(1)

    try:
        text = src_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading '{src_path}': {e}", file=sys.stderr)
        sys.exit(1)

    pattern = build_undo_regex(undo_map)

    def _repl(m: re.Match) -> str:
        return undo_map[m.group(0)]

    undone_text = pattern.sub(_repl, text)

    try:
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        dst_path.write_text(undone_text, encoding="utf-8")
    except Exception as e:
        print(f"Error writing '{dst_path}': {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="Write an undone (reverted) version of a file by converting escaped tokens back to plain."
    )
    parser.add_argument("input", type=str, help="Path to the input file (with escaped tokens).")
    parser.add_argument("-o", "--output", type=str, help="Path to write the undone result. Defaults to <input>.undone")
    parser.add_argument("-f", "--force", action="store_true", help="Overwrite output if it exists.")
    args = parser.parse_args()

    src = Path(args.input)
    if not src.exists():
        print(f"Error: '{src}' does not exist.", file=sys.stderr)
        sys.exit(1)

    dst = Path(args.output) if args.output else src.with_suffix(src.suffix + ".undone")

    # UNDO map: escaped -> plain (target '\.' -> '.', '\*' -> '*', etc.)
    undo_map = {
        r'\_': r'_',
        r'\\\\': r'\\',
        r'\#': r'#',
        r'\.': r'.',
        r'\-': r'-',
        r'\[#ref\\\\_1](#ref\\\\_1\)': r'[1]',
        r'\[#ref\\\\_2](#ref\\\\_2\)': r'[2]',
        r'\[#ref\\\\_3](#ref\\\\_3\)': r'[3]',
        r'\(': r'(',
        r'\[': r'[',
        r'\)': r')',
        r'\]': r']',
        r'\*': r'*',
        r'\*\*': r'**',
        r'\,': r'\ ',
    }

    print(f"Input:  {src}")
    print(f"Output: {dst}")
    undo_replacements_to_file(src, dst, undo_map, overwrite=args.force)
    print("Done.")

if __name__ == "__main__":
    main()
