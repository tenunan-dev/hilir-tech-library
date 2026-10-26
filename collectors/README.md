# Collectors

```
pip install -r requirements-collect.txt
python collectors/collect.py --list                      # eligible sources, no network
python collectors/collect.py --source mdpi-energies --limit 5
python collectors/collect.py                             # all eligible sources
python collectors/collect.py --manual                    # convert files in corpus/_inbox/
```

A source is collected automatically only when its catalog record is `verified`, its
`reuse_level` is `full-text-open` or `full-text-restricted`, its `automated_access` is not
`prohibited`, and an adapter exists (`adapters.py`). Requests check robots.txt, wait at least
3 seconds per host and identify themselves with a user agent pointing at this repo.

This gating is the owner's manual-inclusion mechanism (decision #29): agent acquisition is
unrestricted, but the corpus pipeline still runs only on verified, full-text-level,
non-prohibited records.

| Adapter | Sources | Stores |
| --- | --- | --- |
| `rss` | any record with `feeds` (MDPI journals today) | Full article text |
| `arxiv` | `arxiv` | Metadata and abstracts (CC0); not full texts |
| `osti` | `osti` | Metadata and abstracts; full text needs per-record rights review |
| `manual` | any verified source with a full-text reuse level | Files you drop in `corpus/_inbox/<id>/` |

To add a source, give its record a `feeds` list or write an adapter and register it in `ADAPTERS`.
Tests run offline: `pytest tests`.
