# Corpus

Collected documents, one folder per source id: `corpus/<source-id>/<title>-<hash>.md`.

Each file starts with front matter copied from the catalog record (`licence`, `reuse_level`,
`permitted_use`) plus `url`, `retrieved_at` and `sha256`. Files from `full-text-restricted`
sources also carry a `use_note`: they are private reference copies, not to be redistributed
or used commercially. `manifest.jsonl` lists every stored document by hash, for de-duplication.

`_inbox/<source-id>/` is where hand-downloaded PDFs or HTML pages go for sites whose terms ban
crawlers. Add a sidecar `<file>.url` containing the original URL, then run
`python collectors/collect.py --manual`.
