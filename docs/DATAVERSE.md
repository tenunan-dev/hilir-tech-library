# Exporting to Dataverse (Power Apps tables)

Puts the library into Dataverse so Power Apps, Power Automate and Copilot Studio can use it
inside Microsoft 365, with no server to host.

## 1. Export

```
python tools/export_dataverse.py                       # build/dataverse/*.csv, safe for shared environments
python tools/export_dataverse.py --include-restricted  # personal environment only
```

| File | Rows | Content |
| --- | --- | --- |
| `sources.csv` | one per catalog record | All catalog fields; lists as `;`-separated text; `topics` spells out the codes |
| `documents.csv` | one per corpus document | Metadata for every document; `body` only where `text_included` is `yes` |
| `taxonomy.csv` | one per code | Sector, discipline and region codes with names and sub-topics |
| `technologies.csv` | one per technology card | Maturity, TRL, suppliers, process steps, equipment, costs with basis, Mermaid block diagram, sources |

By default only open-licence documents carry text. Restricted documents (private reference copies) get a row with title, url and licence but no text, because a Dataverse environment is usually readable by colleagues. Use `--include-restricted` only in an environment no one else can read.

## 2. Create the tables

In [Power Apps](https://make.powerapps.com), pick the environment, then **Tables > Import > Import data from Excel or .CSV** (or **New table > Import**), once per file. Suggested settings:

| Table | Primary column | Alternate key | Column types to set |
| --- | --- | --- | --- |
| Library Source | `name` | `source_id` | `url` URL; `quality_tier` whole number; `last_verified` date; `notes` multiline text |
| Library Document | `title` | `document_id` | `url` URL; `published`, `retrieved_at` date and time; `body` multiline text (max length 1,048,576); `source_id` can later become a lookup to Library Source |
| Library Taxonomy | `code` | `code` | all text |
| Library Technology | `name` | `technology_id` | `principle`, `costs`, `block_diagram_mermaid` multiline text |

Leave the other columns as single line text. `sectors`, `disciplines` and `regions` can be converted to multi-select choice columns later (choices from taxonomy.csv) if you want filters in Power Apps.

## 3. Use it in Copilot Studio

1. The environment needs **Dataverse search** turned on (Power Platform admin center > environment > Settings > Features), and the agent must use **Authenticate with Microsoft**.
2. In the agent: **Add knowledge > Dataverse**, pick the three tables (up to 15 per knowledge source).
3. Description, which the orchestrator uses to decide when to search: *Curated library of oil, gas, petrochemical, hydrogen, CCUS and power technology sources, weighted to Asia Pacific and Southeast Asia, with document abstracts. Always cite the url and respect reuse_level.*
4. Glossary terms: add the codes (GAS = Gas processing and LNG, ROT = Rotating and static equipment, sea = Southeast Asia, and so on, from taxonomy.csv) and explain `reuse_level`.
5. To search inside `body` and `notes`, mark the tables and these columns **Searchable** and add them to the **Quick Find view**. Microsoft lists searching multiline text as a preview feature, and the first indexing can take up to two days.

Reference: https://learn.microsoft.com/microsoft-copilot-studio/knowledge-add-dataverse

## 4. Keeping it current

| Way | Effort | Notes |
| --- | --- | --- |
| Re-import the CSVs | Manual | Import into the existing tables; rows match on the alternate keys |
| Dataflow from OneDrive or SharePoint | Low | Save the CSVs there after each refresh; a Power Query dataflow updates the tables on a schedule |
| Dataverse Web API sync | Medium | A script upserts rows by alternate key after the weekly collection. Needs an Entra ID app registration with access to the environment, set up by the owner or an admin |

## Dataverse or the hosted MCP server?

Dataverse keeps everything inside Microsoft 365 with Microsoft sign-in and no hosting, but Copilot Studio searches it with its own Dataverse search (no sector or region filters, no Asia Pacific boost) and updates are imports. The hosted MCP server ([HOSTING.md](HOSTING.md)) gives the library's own search and is live, but needs a host. Both can be used together.
