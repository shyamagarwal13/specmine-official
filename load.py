#!/usr/bin/env python3
"""Load the SpecMine sample and run the flagship spec->code query.

    pip install pandas pyarrow
    python load.py

Prints one row per table with its shape, then answers the question the dataset
is built to make easy: which specs change in the same pull request as code?
"""
import glob
import gzip
import json
import os

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")


def load():
    """Return {table_name: DataFrame} for every Parquet file in data/."""
    tables = {}
    for path in sorted(glob.glob(os.path.join(DATA, "*.parquet"))):
        name = os.path.splitext(os.path.basename(path))[0]
        tables[name] = pd.read_parquet(path)
    return tables


def iter_spec_text():
    """Yield each spec's raw Markdown from specs.jsonl.gz."""
    with gzip.open(os.path.join(HERE, "specs.jsonl.gz"), "rt", encoding="utf-8") as f:
        for line in f:
            yield json.loads(line)


def main():
    t = load()
    print("Loaded SpecMine sample:")
    for name, df in t.items():
        print(f"  {name:<26} {len(df):>8,} rows x {df.shape[1]:>3} cols")

    prs, prf = t["pull_requests"], t["pr_files"]
    cochange = prs[prs.touches_code == 1]
    print(f"\nSpec-touching PRs: {len(prs):,}  |  also change code (co-change): "
          f"{len(cochange):,} ({100 * len(cochange) / len(prs):.1f}%)")

    key = ["tool", "repo_name", "pr_number"]
    files = prf.merge(cochange[key], on=key)
    n_spec = int(files.is_spec.sum())
    n_code = int(files.is_code.sum())
    print(f"In those co-change PRs: {n_spec:,} spec files change alongside "
          f"{n_code:,} code files.")

    print("\nCo-change PRs by tool:")
    print(cochange.groupby("tool").size().sort_values(ascending=False).to_string())


if __name__ == "__main__":
    main()
