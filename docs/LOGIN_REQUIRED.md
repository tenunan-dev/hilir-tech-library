# Pages that require login, registration or payment for full documents

Maintained continuously by collection sessions (started 2026-10-25). Purpose: a single list of every page where a
full document (PDF, dataset, standard) cannot be downloaded anonymously, so the owner knows exactly which gates to
open by hand and which sources are simply blocked. Catalog ids refer to `catalog/sources/<id>.json`.

Access rules that govern this library: no user-agent spoofing, no IP rotation, no defeating robots.txt, paywalls or
bot challenges (AGENTS.md rule 4). Where a gate is free registration, the owner can decide to register; where content
is paywalled or members-only it stays catalog-only (AGENTS.md rule 7).

## Free registration / login gates (full document after sign-up) — gates confirmed 2026-10-25

| Catalog id | Page | Gate | What you get |
| --- | --- | --- | --- |
| iea-ccus-db | https://www.iea.org/data-and-statistics/data-product/ccus-projects-database | Free IEA account (`/account/register`) | CCUS Projects Database XLSX; download button is JS/session-driven — **does not work anonymously** |
| iea-hydrogen-db | https://www.iea.org/data-and-statistics/data-product/hydrogen-production-and-infrastructure-projects-database | Free IEA account | Hydrogen Projects Database XLSX; same JS download gate |
| anl-greet | https://greet.anl.gov/index.php?content=registration&from=download1x | Free email registration form (Argonne GREET Registration Form) | GREET Excel model; note greet.anl.gov returns HTTP 500 status with full HTML on every page — collectors must treat 500-with-body as success there |
| dnv-rules | https://standards.dnv.com/explorer/ | Free Veracity sign-in (401 anonymous) | DNV standards free-of-charge PDFs |
| iogp-library | https://www.iogp.org/bookstore/ (+ /bookstore/Account/Login) | Free account ("Log In or Register") | IOGP reports |
| iogp-jip33 | https://idms.iogp.org/DocumentLibrary?tree=tags&tagKey=51 | Free account on the IOGP Publications Portal | JIP33 S-series specs; catalog URL iogp.org/workstreams/.../jip33/ is **404** — site moved to iogp-jip33.org |
| ptq-digital-refining | https://www.digitalrefining.com/article/{id}/...pdf | Free account (PDF links 302 to loginForm) | PTQ full-article PDFs; abstracts open |
| espacenet (EPO OPS) | https://www.epo.org/en/searching-for-patents/data/web-services/ops | Free EPO registration for OAuth credentials | Patent data API: free tier 4 GB/week, above that EUR 2,800/yr |
| eia-opendata | https://www.eia.gov/opendata/register.php | Free email API key (site data open) | EIA API |
| core-ac | https://core.ac.uk/services/api | Email registration for API key; **full-text downloads are Cloudflare-challenged (403), not login-gated** | Open-access repository metadata + API |
| lens-org | https://www.lens.org/register | Free account | Saved queries, exports, API tokens (search open) |
| hydrocarbon-engineering | https://www.hydrocarbonengineering.com/subscribe/ | Free subscription form | Digital magazine editions/archive; news open |
| lng-industry | https://www.lngindustry.com/subscribe/ | Free subscription form | Same Palladian platform |
| opc-foundation | https://opcfoundation.org/developer-tools/documents/ | Free account for portal bulk downloads | Spec **reader + markdown/XML downloads are open anonymously** (verified 200) |
| iso-15926 / POSC Caesar | https://www.posccaesar.org/login/ | Organisational account via Microsoft Entra ID (membership/service agreement) | PCA Platform + Library; default licence CC BY-ND 4.0; automated use only via documented APIs |

## Paid / membership (stays catalog-only until the owner subscribes) — models confirmed 2026-10-25

| Catalog id | Page | Price model |
| --- | --- | --- |
| iec-standards | https://webstore.iec.ch/ (store open; www.iec.ch 403 to curl) | Per-standard CHF 159–550 (live prices), Redline extra |
| standards-australia | https://store.standards.org.au/ | Per-document AUD 145–1,265 per PDF (live JSON prices) |
| api-standards | https://www.apiwebstore.org/ (login/cart) | Per-standard + PSSAP corporate subscription |
| asme-codes | https://www.asme.org/codes-standards/find-codes-standards | Per-code purchase, member/non-member pricing; journals by subscription |
| astm-standards | https://compass.astm.org/ (login live) | Compass subscription per seat + per-document; www.astm.org blocks curl site-wide |
| iso-tc67 / tc197 / tc265 | https://www.iso.org/committee/49690.html etc. (all 403 to curl) | Per-standard CHF; TC 67 = oil & gas materials/equipment, TC 197 = hydrogen technologies, TC 265 = CCUS |
| ampp-standards / ampp-annual / corrosion-journal | https://store.ampp.org/ (403 to curl), https://ace.ampp.org/registration, https://content.ampp.org/corrosion (CF challenge) | Standards included with AMPP membership; non-members buy per-standard; conference registration; journal by subscription |
| cen-tc12 | https://standards.cencenelec.eu/ords/f?p=CEN:105 | **Metadata free** (search, scopes, XLS export, no login) — full EN texts sold via national members; mirrors ISO/TC 67 |
| spe-journal | https://onepetro.org/SJ (403 to curl) | OnePetro per-paper (~USD 10–15) or institutional subscription |
| gpsa | https://www.gpamidstream.org/gpsa/ (CF challenge) | Data Book per copy, member discount |
| icis | https://www.icis.com/explore/ (Incapsula block) | Sales-led subscription |
| nexant-chemsystems | https://www.nexanteca.com/ | Client-only reports, contact-sales |
| cnki-overseas | https://oversea.cnki.net/ | Institutional subscription / per-article |
| ms-malaysia | https://www.jsm.gov.my/ | Per-document RM purchase |

## Members-only areas (association/relationship gates)

| Page | Gate |
| --- | --- |
| GIIGNL members' area (https://giignl.org/) | Memberstack login — paying corporate membership; no content-terms page exists |
| Hydrogen Europe Members Only Area | Association member login |
| Energistics standards (publications.opengroup.org) | Registered-user / product licence agreements; © 2026 Energistics Consortium, all rights reserved |
| NOV MYNOV / document library | MYNOV SSO (free registration) for apps and library; public site open |
| SLB customer portals | Customer accounts; public site open, all rights reserved |
| GHGT proceedings | Conference registration; licence unstated, © IEAGHG |
| OIES publications shop | Sold titles paid; papers otherwise free but rights reserved |

## Blocked to automated access (not a login gate — a block; full text needs a human browser)

| Page | What happens | Compliant alternative used |
| --- | --- | --- |
| www.osti.gov (API and full-text purl) | TCP connection timeout from this network | Same US-Government reports mirrored on netl.doe.gov, energy.gov, nrel.gov, pnnl.gov, hydrogen.energy.gov, rosap.ntl.bts.gov — used 2026-10-25 for the NETL Baseline Rev 4, DOE SAF pathways review, HEFA and ATJ analyses |
| www.nrel.gov | DNS returns empty answers for www/atb.nrel.gov from this network (checked against two resolvers, 2026-10-25) | NREL-authored papers via open-access mirrors (PMC/Europe PMC REST API) or hydrogen.energy.gov program records |
| www.pnnl.gov (search and publications paths) | WAF 403 "Request Rejected" to curl | PNNL reports mirrored on rosap.ntl.bts.gov (used for the Geleynse ATJ paper) |
| www.mdpi.com (all 6 mdpi-* journals) | CDN (Akamai) 403 on RSS, article pages and robots.txt | OAI-PMH at https://oai.mdpi.com/oai/oai2.php serves metadata + abstracts only; full text needs the owner's browser |
| pmc.ncbi.nlm.nih.gov direct PDF | Cloudflare challenge page | Europe PMC REST API fullTextXML works (used for the Tao 2017 HEFA TEA) |
| link.springer.com / biomedcentral PDF | Cookies-required redirect, then empty | Full text via Europe PMC REST API |
| europepmc.org web page | Cloudflare challenge | The REST API host www.ebi.ac.uk works |
| www.energyinst.org/statistical-review | Cloudflare challenge (403, twice) | Owner browser read |
| abb.com / new.abb.com | HTTP/2 errors, timeouts to curl | Owner browser read |
| airproducts.com | CloudFront 403 | Owner browser read |
| aspentech.com | 403 on everything including robots.txt | Owner browser read |
| dcceew.gov.au | Connection fails (000) | Owner browser read |
| dgip-indonesia (pdki-indonesia.dgip.go.id) | 403 | Owner browser read |
| exxonmobilchemical.com | 403 | Owner browser read |
| patents.google.com | 503 bot-block; JS app | Owner browser read |
| j-platpat.inpit.go.jp | JS app, terms not machine-readable | Owner browser read |
| patentscope.wipo.int | 403; JS app | Owner browser read |
| kipris.or.kr | robots.txt: Disallow: / (all bots except Bing/Google) | Owner browser read |
| id-skkmigas.go.id | 403 | Owner browser read |
| irena.org | 403 (Akamai) | Owner browser read |
| shell.com (catalysts, scenarios) | Prerender JS shell; terms body client-side only | Owner browser read |
| sodir.no | Cloudflare challenge | Owner browser read |
| technipfmc.com | 403 (Cloudflare) | Owner browser read |
| wood-plc.com | Cloudflare challenge | Owner browser read |
| sciencedirect.com (Energy Reports) | 403 | Per-article check by owner |
| mopng.gov.in | Readable — but restrictive NIC copyright policy, NOT CC BY | Text reuse needs permission (downgraded from full-text-open, 2026-10-25) |

## Dead / moved sources (found while verifying, 2026-10-25)

| Catalog id | Finding |
| --- | --- |
| uq-energy | energy.uq.edu.au is NXDOMAIN — UQ Energy Initiative site retired, no redirect; record repointed to UQ legal page for provenance |
| mycite | mycite.my connection times out (two attempts) |
| myipo | iponlineext.myipo.gov.my returns Cloudflare error 522 (origin down) |
| aker-carbon-capture (SLB Capturi) | slbcapturi.com no longer resolves (NXDOMAIN); slb.com/capturi 404 — domain retired |
| garuda-indonesia | garuda.kemdikbud.go.id no longer resolves (NXDOMAIN) — domain moved |
| johnson-matthey | Business sold to Honeywell; old JM catalyst page redirects to Honeywell (whose terms ban copying). LCH technology pages still live on matthey.com and were read 2026-10-25 for card facts (bp H2Teesside, H2H Saltend) |
| iogp-jip33 | Catalog URL 404 — site moved to iogp-jip33.org |
| KEEI | Catalog URL /main.nsf/index_en.html dead — English site now at keei.re.kr/eng (record updated) |
| SINTEF Energy | /en/energy/ path 404 (site restructure); no terms page found anywhere on sintef.no |
| Pertamina | Terms page exists but has no terms body — footer © only; reuse_level summary-only |
| MoPNG (India) | Copyright policy read: permission-based, not CC BY — downgraded |

## Progress log

- 2026-10-25 (session 1): register created. Retrieved full documents for 4 gap-blocking sources (NETL Baseline Rev 4; DOE SAF Technical Pathways 2020; Tao 2017 HEFA TEA; Geleynse 2018 ATJ); read JM LCH pages for card facts; verified 9 of 12 unchecked sources and 26 of 51 manual-terms-check sources; confirmed all 15 free-registration and 19 paywalled gates (tables above); sector gap-hunters downloading (H2/GAS: 8 documents landed).
- 2026-10-25 (session 1, close): 24 corpus documents collected in total, 35 sources verified, all gates surveyed. MDPI harvested compliantly via OAI-PMH (850 unique abstracts, ~1.6% sample, `docs/research/mdpi-oai/`); full text stays manual-browser. Committed and pushed as `fe771ef` + `7999bc6`; hosted copy redeployed and verified live (versions 3cc4a6b4, then 845ee5b3 after the instance cycle: /api/stats 133 open documents / 9,859 chunks / 293 cards). nrel.gov (DNS) and pnnl.gov (WAF) added to the blocked table.
