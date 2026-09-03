# SpecMine v1.1 — Data Dictionary

Every released table, with the columns present in the Parquet files. Types are the MySQL types of the source schema.


## `spec_files` — 124 columns

Broad-census spine: one row per spec file, full GitHub repository object, file/commit provenance, tool attribution, trace roll-ups. Raw Markdown is in specs.jsonl.gz.

| column | type | description |
|---|---|---|
| `file_url_sha16` | char(16) | 16-hex digest of the file's GitHub blob URL (primary key of the broad census). |
| `file_url` | text | GitHub blob URL of the spec file. |
| `file_path` | text | path within its repository. |
| `file_name` | varchar(255) | file name. |
| `file_sha` | varchar(64) |  |
| `git_url` | text |  |
| `search_run_id` | varchar(64) |  |
| `repo_id` | bigint(20) |  |
| `repo_node_id` | varchar(255) |  |
| `repo_name` | varchar(511) | owner/repo slug (join key to every other layer). |
| `repo_url` | text |  |
| `repo_homepage` | text |  |
| `repo_description` | text |  |
| `repo_fork` | tinyint(1) |  |
| `repo_private` | tinyint(1) |  |
| `repo_visibility` | varchar(32) |  |
| `owner_login` | varchar(255) | repository owner's GitHub login. |
| `owner_id` | bigint(20) |  |
| `owner_node_id` | varchar(255) |  |
| `owner_type` | varchar(64) | User or Organization. |
| `owner_html_url` | text |  |
| `owner_site_admin` | tinyint(1) |  |
| `repo_stars` | int(11) | star count at capture time. |
| `repo_forks` | int(11) |  |
| `repo_watchers` | int(11) |  |
| `repo_subscribers_count` | int(11) |  |
| `repo_network_count` | int(11) |  |
| `repo_open_issues` | int(11) |  |
| `repo_size_kb` | int(11) |  |
| `repo_language` | varchar(255) | primary language. |
| `repo_license` | varchar(255) |  |
| `repo_license_key` | varchar(128) |  |
| `repo_license_spdx_id` | varchar(128) | SPDX id of the repo license (NULL/NOASSERTION if none). |
| `repo_default_branch` | varchar(255) |  |
| `repo_topics` | text |  |
| `repo_archived` | tinyint(1) |  |
| `repo_disabled` | tinyint(1) |  |
| `repo_is_template` | tinyint(1) |  |
| `repo_allow_forking` | tinyint(1) |  |
| `repo_web_commit_signoff_required` | tinyint(1) |  |
| `repo_has_issues` | tinyint(1) |  |
| `repo_has_projects` | tinyint(1) |  |
| `repo_has_wiki` | tinyint(1) |  |
| `repo_has_pages` | tinyint(1) |  |
| `repo_has_downloads` | tinyint(1) |  |
| `repo_has_discussions` | tinyint(1) |  |
| `repo_clone_url` | text |  |
| `repo_ssh_url` | text |  |
| `repo_svn_url` | text |  |
| `repo_git_url` | text |  |
| `repo_mirror_url` | text |  |
| `repo_created_at` | varchar(64) |  |
| `repo_updated_at` | varchar(64) |  |
| `repo_pushed_at` | varchar(64) |  |
| `file_last_commit_sha` | varchar(64) |  |
| `file_last_commit_node_id` | varchar(255) |  |
| `file_last_commit_html_url` | text |  |
| `file_last_commit_message` | longtext |  |
| `file_last_commit_comment_count` | int(11) |  |
| `file_last_commit_at` | varchar(64) | timestamp of the most recent commit to the file. |
| `file_last_commit_author` | text |  |
| `file_last_commit_author_login` | varchar(255) |  |
| `file_last_commit_author_id` | bigint(20) |  |
| `file_last_commit_author_type` | varchar(64) |  |
| `file_last_commit_author_html_url` | text |  |
| `file_last_commit_author_site_admin` | tinyint(1) |  |
| `file_last_commit_committer` | text |  |
| `file_last_commit_committer_at` | varchar(64) |  |
| `file_last_commit_committer_login` | varchar(255) |  |
| `file_last_commit_committer_id` | bigint(20) |  |
| `file_last_commit_committer_type` | varchar(64) |  |
| `file_last_commit_committer_html_url` | text |  |
| `file_last_commit_committer_site_admin` | tinyint(1) |  |
| `file_last_commit_tree_sha` | varchar(64) |  |
| `file_last_commit_parents` | text |  |
| `file_last_commit_verified` | tinyint(1) |  |
| `file_last_commit_verification_reason` | varchar(64) |  |
| `file_last_commit_verified_at` | varchar(64) |  |
| `size_partition_label` | text |  |
| `updated_at` | timestamp |  |
| `not_spec_filter` | tinyint(1) | 0 for kept specs (only kept rows ship). |
| `file_first_commit_sha` | varchar(64) |  |
| `file_first_commit_node_id` | varchar(255) |  |
| `file_first_commit_html_url` | text |  |
| `file_first_commit_message` | longtext |  |
| `file_first_commit_comment_count` | int(11) |  |
| `file_first_commit_at` | varchar(64) | timestamp the file was first committed (adoption signal). |
| `file_first_commit_author` | text |  |
| `file_first_commit_author_login` | varchar(255) |  |
| `file_first_commit_author_id` | bigint(20) |  |
| `file_first_commit_author_type` | varchar(64) |  |
| `file_first_commit_author_html_url` | text |  |
| `file_first_commit_author_site_admin` | tinyint(1) |  |
| `file_first_commit_committer` | text |  |
| `file_first_commit_committer_at` | varchar(64) |  |
| `file_first_commit_committer_login` | varchar(255) |  |
| `file_first_commit_committer_id` | bigint(20) |  |
| `file_first_commit_committer_type` | varchar(64) |  |
| `file_first_commit_committer_html_url` | text |  |
| `file_first_commit_committer_site_admin` | tinyint(1) |  |
| `file_first_commit_tree_sha` | varchar(64) |  |
| `file_first_commit_parents` | text |  |
| `file_first_commit_verified` | tinyint(1) |  |
| `file_first_commit_verification_reason` | varchar(64) |  |
| `file_first_commit_verified_at` | varchar(64) |  |
| `file_total_commits` | int(11) | commits touching this artifact up to the crawl cutoff. |
| `commit_history_status` | varchar(16) | done | empty | error | truncated. |
| `commit_history_fetched_at` | varchar(32) |  |
| `spec_tool` | varchar(32) | attributed SDD tool or path bucket (path-fingerprint attribution). |
| `spec_role` | varchar(24) | lifecycle role: living / change_proposal / archived / feature / config / na. |
| `file_content_sha` | char(64) | sha256 of the fetched artifact content (dedup key). |
| `file_content_bytes` | int(11) | size of fetched content. |
| `content_fetch_status` | varchar(16) | done | missing | toobig | error. |
| `content_fetched_at` | varchar(32) |  |
| `feature_branch` | varchar(255) | the 'Feature Branch:' header value, when present. |
| `n_linked_prs` | int(11) | rolled-up PR references. |
| `n_linked_issues` | int(11) | rolled-up issue references. |
| `n_sibling_docs` | int(11) | rolled-up sibling-document references. |
| `n_code_links` | int(11) | rolled-up code-file references. |
| `has_tasks` | tinyint(4) | has an associated tasks.md. |
| `has_plan` | tinyint(4) | has a plan.md. |
| `has_proposal` | tinyint(4) | has a proposal.md. |
| `has_design` | tinyint(4) | has a design.md. |
| `trace_rollup_at` | varchar(32) |  |

## `spec_file_commits` — 24 columns

Complete per-file commit history for the broad census.

| column | type | description |
|---|---|---|
| `id` | bigint(20) |  |
| `file_url_sha16` | char(16) | 16-hex digest of the file's GitHub blob URL (primary key of the broad census). |
| `repo_name` | varchar(512) | owner/repo slug (join key to every other layer). |
| `file_path` | text | path within its repository. |
| `seq_from_oldest` | int(11) |  |
| `commit_sha` | varchar(64) | commit hash. |
| `node_id` | varchar(255) |  |
| `html_url` | text |  |
| `message` | longtext | commit message. |
| `comment_count` | int(11) |  |
| `authored_at` | varchar(64) | author timestamp. |
| `author_name` | text |  |
| `author_login` | varchar(255) | commit author GitHub login. |
| `author_id` | bigint(20) |  |
| `author_type` | varchar(64) |  |
| `committed_at` | varchar(64) | committer timestamp. |
| `committer_name` | text |  |
| `committer_login` | varchar(255) | committer GitHub login. |
| `committer_id` | bigint(20) |  |
| `committer_type` | varchar(64) |  |
| `tree_sha` | varchar(64) |  |
| `parents` | text |  |
| `verified` | tinyint(1) |  |
| `verification_reason` | varchar(64) |  |

## `spec_content_features` — 40 columns

39 parsed structural and requirement-template features per spec.

| column | type | description |
|---|---|---|
| `file_url_sha16` | char(16) | 16-hex digest of the file's GitHub blob URL (primary key of the broad census). |
| `n_bytes` | int(11) |  |
| `n_lines` | int(11) |  |
| `n_words` | int(11) |  |
| `n_headings` | int(11) |  |
| `max_heading_depth` | int(11) |  |
| `n_code_fences` | int(11) |  |
| `n_mermaid` | int(11) |  |
| `n_tables` | int(11) |  |
| `n_links` | int(11) |  |
| `n_images` | int(11) |  |
| `n_list_items` | int(11) |  |
| `n_checkboxes` | int(11) |  |
| `n_checked` | int(11) |  |
| `n_shall` | int(11) |  |
| `n_gherkin` | int(11) |  |
| `n_scenario_blocks` | int(11) |  |
| `n_delta_headers` | int(11) |  |
| `n_needs_clarification` | int(11) |  |
| `n_todo` | int(11) |  |
| `has_ears` | tinyint(4) |  |
| `has_gherkin` | tinyint(4) |  |
| `has_user_story` | tinyint(4) |  |
| `has_requirements` | tinyint(4) |  |
| `has_acceptance_criteria` | tinyint(4) |  |
| `has_user_scenarios` | tinyint(4) |  |
| `has_non_goals` | tinyint(4) |  |
| `has_out_of_scope` | tinyint(4) |  |
| `has_overview` | tinyint(4) |  |
| `has_success_criteria` | tinyint(4) |  |
| `has_edge_cases` | tinyint(4) |  |
| `has_open_questions` | tinyint(4) |  |
| `has_dependencies` | tinyint(4) |  |
| `has_purpose` | tinyint(4) |  |
| `has_mandatory_marker` | tinyint(4) |  |
| `is_tiny` | tinyint(4) |  |
| `has_unfilled_placeholder` | tinyint(4) |  |
| `has_lorem` | tinyint(4) |  |
| `lang` | varchar(8) |  |
| `content_family` | varchar(24) |  |

## `spec_links` — 5 columns

Census-wide traceability index: typed references from each spec to code, sibling docs, PRs, issues, and branches.

| column | type | description |
|---|---|---|
| `id` | bigint(20) |  |
| `spec_url_sha16` | char(16) | file_url_sha16 of the spec this reference belongs to (FK to spec_files). |
| `rel` | varchar(16) | reference target type: code / sibling / pr / ref / branch / issue / anchor. |
| `target` | varchar(500) | the referenced value (path, PR number, issue, branch, ...). |
| `provenance` | varchar(24) | how the reference was found: tasks / tree / commit_msg / branch_header / content. |

## `kiro_files` — 17 columns

Kiro census: requirements/design/tasks artifacts under .kiro/specs/, enriched in v1.1 with content hashes and commit counts (raw content in kiro_specs.jsonl.gz).

| column | type | description |
|---|---|---|
| `id` | bigint(20) |  |
| `repo_name` | varchar(511) | owner/repo slug (join key to every other layer). |
| `owner_login` | varchar(255) | repository owner's GitHub login. |
| `repo_id` | bigint(20) |  |
| `file_path` | varchar(1000) | path within its repository. |
| `file_name` | varchar(255) | file name. |
| `kind` | varchar(16) | artifact kind (kiro: requirements/design/tasks; openspec: proposal.md/design.md/tasks.md/...). |
| `feature` | varchar(400) | the Kiro feature/spec folder name. |
| `file_sha` | varchar(64) |  |
| `html_url` | text |  |
| `git_url` | text |  |
| `fetched_at` | varchar(32) |  |
| `file_content_sha` | char(64) | sha256 of the fetched artifact content (dedup key). |
| `file_content_bytes` | int(11) | size of fetched content. |
| `content_fetch_status` | varchar(16) | done | missing | toobig | error. |
| `file_total_commits` | int(11) | commits touching this artifact up to the crawl cutoff. |
| `commit_history_status` | varchar(16) | done | empty | error | truncated. |

## `kiro_repos` — 29 columns

v1.1: full GitHub repository object for every Kiro-census repository (fetched Aug 2026).

| column | type | description |
|---|---|---|
| `repo_name` | varchar(511) | owner/repo slug (join key to every other layer). |
| `repo_id` | bigint(20) |  |
| `repo_node_id` | varchar(255) |  |
| `repo_url` | text |  |
| `repo_homepage` | text |  |
| `repo_description` | text |  |
| `repo_fork` | tinyint(1) |  |
| `repo_visibility` | varchar(32) |  |
| `owner_login` | varchar(255) | repository owner's GitHub login. |
| `owner_id` | bigint(20) |  |
| `owner_type` | varchar(64) | User or Organization. |
| `repo_stars` | int(11) | star count at capture time. |
| `repo_forks` | int(11) |  |
| `repo_watchers` | int(11) |  |
| `repo_open_issues` | int(11) |  |
| `repo_size_kb` | int(11) |  |
| `repo_language` | varchar(128) | primary language. |
| `repo_license_key` | varchar(64) |  |
| `repo_license_spdx_id` | varchar(64) | SPDX id of the repo license (NULL/NOASSERTION if none). |
| `repo_default_branch` | varchar(255) |  |
| `repo_topics` | text |  |
| `repo_archived` | tinyint(1) |  |
| `repo_disabled` | tinyint(1) |  |
| `repo_is_template` | tinyint(1) |  |
| `repo_created_at` | varchar(64) |  |
| `repo_updated_at` | varchar(64) |  |
| `repo_pushed_at` | varchar(64) |  |
| `fetch_status` | varchar(16) |  |
| `fetched_at` | varchar(64) |  |

## `kiro_file_commits` — 16 columns

v1.1: complete per-artifact commit history for the Kiro census, capped at the same crawl end as the broad census (2026-07-11).

| column | type | description |
|---|---|---|
| `id` | bigint(20) |  |
| `kiro_file_id` | bigint(20) | FK to kiro_files.id. |
| `repo_name` | varchar(511) | owner/repo slug (join key to every other layer). |
| `file_path` | text | path within its repository. |
| `seq_from_oldest` | int(11) |  |
| `commit_sha` | varchar(64) | commit hash. |
| `authored_at` | varchar(64) | author timestamp. |
| `author_name` | text |  |
| `author_login` | varchar(255) | commit author GitHub login. |
| `author_id` | bigint(20) |  |
| `committed_at` | varchar(64) | committer timestamp. |
| `committer_name` | text |  |
| `committer_login` | varchar(255) | committer GitHub login. |
| `committer_id` | bigint(20) |  |
| `message` | longtext | commit message. |
| `html_url` | text |  |

## `kiro_content_features` — 40 columns

v1.1: the same 39 structural features computed over Kiro artifact content.

| column | type | description |
|---|---|---|
| `kiro_file_id` | bigint(20) | FK to kiro_files.id. |
| `n_bytes` | int(11) |  |
| `n_lines` | int(11) |  |
| `n_words` | int(11) |  |
| `n_headings` | int(11) |  |
| `max_heading_depth` | int(11) |  |
| `n_code_fences` | int(11) |  |
| `n_mermaid` | int(11) |  |
| `n_tables` | int(11) |  |
| `n_links` | int(11) |  |
| `n_images` | int(11) |  |
| `n_list_items` | int(11) |  |
| `n_checkboxes` | int(11) |  |
| `n_checked` | int(11) |  |
| `n_shall` | int(11) |  |
| `n_gherkin` | int(11) |  |
| `n_scenario_blocks` | int(11) |  |
| `n_delta_headers` | int(11) |  |
| `n_needs_clarification` | int(11) |  |
| `n_todo` | int(11) |  |
| `has_ears` | tinyint(4) |  |
| `has_gherkin` | tinyint(4) |  |
| `has_user_story` | tinyint(4) |  |
| `has_requirements` | tinyint(4) |  |
| `has_acceptance_criteria` | tinyint(4) |  |
| `has_user_scenarios` | tinyint(4) |  |
| `has_non_goals` | tinyint(4) |  |
| `has_out_of_scope` | tinyint(4) |  |
| `has_overview` | tinyint(4) |  |
| `has_success_criteria` | tinyint(4) |  |
| `has_edge_cases` | tinyint(4) |  |
| `has_open_questions` | tinyint(4) |  |
| `has_dependencies` | tinyint(4) |  |
| `has_purpose` | tinyint(4) |  |
| `has_mandatory_marker` | tinyint(4) |  |
| `is_tiny` | tinyint(4) |  |
| `has_unfilled_placeholder` | tinyint(4) |  |
| `has_lorem` | tinyint(4) |  |
| `lang` | varchar(8) |  |
| `content_family` | varchar(24) |  |

## `openspec_artifact_files` — 12 columns

OpenSpec change proposals, designs, and task lists with parsed task counts and raw content.

| column | type | description |
|---|---|---|
| `id` | bigint(20) |  |
| `repo_name` | varchar(511) | owner/repo slug (join key to every other layer). |
| `file_path` | varchar(700) | path within its repository. |
| `kind` | varchar(24) | artifact kind (kiro: requirements/design/tasks; openspec: proposal.md/design.md/tasks.md/...). |
| `content` | longtext | raw Markdown of the artifact. |
| `content_sha` | char(64) |  |
| `n_bytes` | int(11) |  |
| `n_tasks` | int(11) | parsed task-list item count. |
| `n_tasks_done` | int(11) | checked task-list items. |
| `n_code_refs` | int(11) | code paths named in tasks.md. |
| `fetch_status` | varchar(16) |  |
| `fetched_at` | varchar(32) |  |

## `openspec_code_refs` — 8 columns

OpenSpec task-to-code references resolved against the repository git tree at the anchoring commit.

| column | type | description |
|---|---|---|
| `id` | bigint(20) |  |
| `repo_name` | varchar(511) | owner/repo slug (join key to every other layer). |
| `artifact_path` | varchar(700) | path of the OpenSpec artifact the ref came from. |
| `code_path` | varchar(500) | code path named by a task. |
| `task_done` | tinyint(4) | 1 if the naming task was checked off. |
| `anchor_sha` | char(40) | commit the tree was resolved against. |
| `exists_at_anchor` | tinyint(4) | 1 if code_path existed in the tree at anchor_sha. |
| `resolved_path` | varchar(700) | matched tree path, if any. |

## `repo_trees` — 5 columns

Metadata of the repository git tree that tree-provenance references resolve against.

| column | type | description |
|---|---|---|
| `repo_name` | varchar(511) | owner/repo slug (join key to every other layer). |
| `status` | varchar(16) | fetch status. |
| `n_entries` | int(11) | entries in the repository git tree. |
| `truncated` | tinyint(4) | 1 if GitHub truncated the tree listing. |
| `fetched_at` | varchar(32) |  |

## `pull_requests` — 25 columns

PR layer (the 11 per-tool <tool>_prs tables unioned, 10 non-empty, with a `tool` column): every pull request that touches a spec file, one row per PR.

| column | type | description |
|---|---|---|
| `tool` | varchar(16) | SDD tool this PR row was discovered under (10 of the 11 swept tools appear; specweave yielded none). |
| `id` | bigint(20) |  |
| `repo_name` | varchar(511) | owner/repo slug (join key to every other layer). |
| `pr_number` | int(11) | pull request number. |
| `title` | text | PR title. |
| `state` | varchar(12) | open/closed. |
| `is_merged` | tinyint(4) | 1 if merged. |
| `merged_at` | varchar(32) | merge timestamp. |
| `created_at` | varchar(32) | PR creation timestamp. |
| `closed_at` | varchar(32) |  |
| `author_login` | varchar(255) | commit author GitHub login. |
| `head_branch` | varchar(400) | source branch. |
| `base_branch` | varchar(255) | target branch. |
| `n_files` | int(11) | files changed in the PR. |
| `n_specdir_files` | int(11) |  |
| `n_spec_files` | int(11) | spec files changed. |
| `n_code_files` | int(11) | code files changed. |
| `n_md_files` | int(11) |  |
| `n_other_files` | int(11) |  |
| `additions` | int(11) | lines added. |
| `deletions` | int(11) | lines removed. |
| `files_status` | varchar(12) |  |
| `touches_code` | tinyint(4) | 1 when the PR changes at least one code file outside the spec directory (co-change signal). |
| `n_code_outside` | int(11) | code files changed outside the spec directory. |
| `n_prs_in_repo` | int(11) | total spec-touching PRs in the repo. |

## `pr_files` — 12 columns

PR layer (the 11 per-tool <tool>_pr_files tables unioned): the per-file changeset of each spec-touching PR (complete up to GitHub's 3,000-file-per-PR cap), each file flagged spec/code.

| column | type | description |
|---|---|---|
| `tool` | varchar(16) | SDD tool this PR row was discovered under (10 of the 11 swept tools appear; specweave yielded none). |
| `id` | bigint(20) |  |
| `repo_name` | varchar(511) | owner/repo slug (join key to every other layer). |
| `pr_number` | int(11) | pull request number. |
| `file_path` | varchar(1000) | path within its repository. |
| `change_status` | varchar(12) | per-file status: added / modified / removed. |
| `additions` | int(11) | lines added. |
| `deletions` | int(11) | lines removed. |
| `is_specdir` | tinyint(4) | 1 if the file sits under the spec directory. |
| `is_spec` | tinyint(4) | 1 if the changed file is a spec. |
| `is_code` | tinyint(4) | 1 if the changed file is source code. |
| `ext` | varchar(16) | file extension. |
