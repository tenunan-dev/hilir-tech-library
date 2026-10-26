# Archive

Superseded versions of documents live here. **Nothing is deleted**: when a document is rewritten
past recognition, or a living document's history outgrows the file, the outgoing version is copied
here before the living one is replaced, and the living document links to the copy.

## Filename convention

`<YYYY-MM-DD>_<Document>_v<YYYY.MM.DD[.N]>.md`

- **Date prefix** — the day this version was *superseded*. Leading ISO date keeps the folder
  sorted chronologically by name.
- **Document** — the living document's name (`HOSTING`, `POSTGRES`, `STATUS-log`, ...).
- **Version** — the [CHANGELOG](../../CHANGELOG.md) version whose era this content belongs to
  (calendar versions, `YYYY.MM.DD`, `.N` for later releases the same day).

Examples: `2026-10-26_HOSTING_v2026.10.25.md` (the pre-domain-move hosting doc, superseded on
2026-10-26 by release 2026.10.26.1); `2026-10-26_STATUS-log_v2026.10.25.md` (STATUS.md session
log for 2026-10-23 – 2026-10-25, moved out when the log was trimmed).

## Rules

1. Copy the outgoing version here under the convention name — verbatim, with a short archive
   banner at the top saying what it is, when it was superseded and by what.
2. Replace the living document, and leave a link to the archive copy from the living document.
3. Never edit an archived file afterwards; corrections happen in the living document.
4. Versions older than this system (pre-2026.10.26.2) exist only in git history unless archived
   here — archiving them retroactively is optional, not required.
