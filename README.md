# SpecMine v1.0 — 500-repository sample

SpecMine is a large-scale corpus of **Spec-Driven Development (SDD)** artifacts
mined from public GitHub repositories: the Markdown specifications that AI coding
agents turn into code, attributed to the tool that produced them, enriched with
full repository metadata and commit history, and, for a subsample of
repositories, followed into the pull requests that change them.

This repository is the **curated 500-repository sample** provided for the MSR 2027
Mining Challenge organizing committee. It is a faithful slice of every layer of
the full dataset, small enough to clone and query in minutes. The full v1.0
snapshot (a MySQL dump plus CSV/Parquet exports and the complete spec-contents
JSONL) will be released on Zenodo with a citable DOI on acceptance.

- **Proposal:** `mining-challenge-proposal-2027` (this sample is the artifact it references).
- **Snapshot:** SpecMine v1.0, July 2026.

## What SpecMine captures (full dataset)

| Layer | Count | This sample |
|---|---:|---|
| Broad census (`spec.md`/`specs.md`, 17 named tools) | 470,795 specs / 73,030 repos | 28,583 specs / 415 repos |
| Kiro census (`.kiro/specs` requirements/design/tasks) | 98,574 artifacts / 12,910 repos | 18,585 / 100 repos |
| PR layer (spec-touching PRs, 11 tools, ≥10-star repos) | 5,992 PRs / 581 repos | 5,335 PRs / 229 repos |
| OpenSpec change artifacts | 266,230 | 22,992 |
| Traceability index (typed references) | 2,421,323 | 261,032 |

The 500 sample repositories were selected to cover every one of the 17 named
tools and 4 path buckets, the Kiro census, and the PR layer. Selection is
reproducible (see `sample_repos.txt` for the exact list): the PR-richest 229
repositories, at least three repositories per named tool, the highest-starred
broad-census repositories to fill 400, and 100 Kiro repositories.

## Layout

```
data/                         Parquet, one file per released table (zstd)
  spec_files.parquet          broad-census spine (repo object, provenance, attribution)
  spec_file_commits.parquet   per-file commit history
  spec_content_features.parquet   39 structural / requirement-template features per spec
  spec_links.parquet          traceability index (typed references)
  kiro_files.parquet          Kiro requirements / design / tasks
  openspec_artifact_files.parquet   OpenSpec proposals / designs / task lists (+ content)
  openspec_code_refs.parquet  OpenSpec task-to-code refs resolved on the git tree
  pull_requests.parquet       PR layer: 11 <tool>_prs tables unioned, with a `tool` column
  pr_files.parquet            PR layer: per-file changesets, each file flagged spec/code
  repo_trees.parquet          git-tree metadata references resolve against
specs.jsonl.gz                raw Markdown of every sample spec (one JSON object per line)
schema.sql                    CREATE TABLE for each shipped table (MySQL types)
DATA_DICTIONARY.md            every shipped column, typed and described
sample_repos.txt              the 500 repo_name values in this sample
load.py                       load the Parquet with pandas and run the flagship query
example.ipynb                 worked examples over the sample
```

Every identifier (`repo_name`, `file_url`, `pr_number`) is a live GitHub value,
so any row can be re-fetched or joined to external sources.

## Quick start

```bash
pip install pandas pyarrow            # duckdb optional
python load.py                        # loads every table, prints a summary + the co-change query
```

Pandas:

```python
import pandas as pd
prs = pd.read_parquet("data/pull_requests.parquet")
prf = pd.read_parquet("data/pr_files.parquet")

# "which specs change in the same PR as code?" — the flagship spec->code query
cochange = prs[prs.touches_code == 1]
files = prf.merge(cochange[["tool", "repo_name", "pr_number"]],
                  on=["tool", "repo_name", "pr_number"])
print(files[files.is_spec == 1].shape, "spec files changed alongside code")
```

DuckDB (query the Parquet directly, no load step):

```sql
SELECT tool, COUNT(*) AS cochange_prs
FROM 'data/pull_requests.parquet'
WHERE touches_code = 1
GROUP BY tool ORDER BY cochange_prs DESC;
```

Spec text (`specs.jsonl.gz`) joins to `spec_files` on `file_url_sha16`:

```python
import gzip, json
with gzip.open("specs.jsonl.gz", "rt") as f:
    specs = [json.loads(l) for l in f]      # {file_url_sha16, repo_name, file_path, spec_tool, spec_role, content}
```

MySQL: create the tables with `schema.sql`, then load each Parquet (for example
with `pandas.DataFrame.to_sql`, or convert to CSV and `LOAD DATA`).

## How the sample maps to the full release

- **PR layer.** The full MySQL release stores the PR layer as 11 per-tool table
  pairs (`openspec_prs`/`openspec_pr_files`, `speckit_prs`/`speckit_pr_files`, and
  so on). This sample unions them into `pull_requests.parquet` and
  `pr_files.parquet` and adds a `tool` column, which is easier to query and
  loses nothing.
- **Kept set.** The sample ships only kept specs (`not_spec_filter = 0`). The full
  release also retains filtered rows (package caches, vendored trees, pre-2024
  files) with the flag and reason that fired, so the not-a-spec filter can be
  audited and reversed.
- **Dropped columns.** Commit-email addresses, GPG-signature blobs, and avatar
  URLs are dropped at release time; raw `file_content` moves to `specs.jsonl.gz`.
  Author and committer logins and numeric IDs are kept (they are public and are
  what makes authorship analysis possible).

## Licensing, ethics, and privacy

All artifacts come from public GitHub repositories, collected within the API
terms of service. Every repository row keeps its SPDX license so you can filter
to license-compatible subsets; redistribution follows each repository's own
terms. Public handles are kept; private contact details are not. Please avoid
deanonymization and keep personal data out of published results beyond aggregate
analysis.
