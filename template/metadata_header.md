# Dataset page metadata header

Every dataset page under `content/xqtl-data/{gwas,omics,qtl,study_info,reference_data}` can start with a YAML header between two `---` lines. The catalog generator (`scripts/toc.py`) and the checker (`scripts/audit_catalog.py`) read it. `scripts/hugo_generator.py` removes it from the page text and passes its public fields to the site layouts in `site/`, which use them for the summary card, the catalog, the menu and the analysis coverage grid. The `internal` field is dropped and never reaches the site. Pages without a header keep working and the catalog falls back to the first sentence of the page.

The header sits next to the NIAGADS fields described in the other templates in this folder. It does not replace them.

```yaml
---
type: omics                # study | gwas | omics | qtl | reference
modality: expression       # omics and qtl pages. Use the modality folder name, for example expression, splicing, eQTL, sQTL
short_title: MiGA microglia # optional, label in the menu and in "Related datasets"
cohort: MiGA               # study, omics and qtl pages
context: microglia         # optional, tissue or cell type
sample_size: 255           # optional, number of samples
access: controlled         # optional, open | controlled | requested | pending
status: released           # released | staged | planned | deprecated
release: 2026-10           # required for released and deprecated
synapse_ids: [syn69670592] # public Synapse IDs only. May be empty for staged or planned pages
lead_analysts: [Travyse Edwards]
last_verified: 2026-10-07  # required for released pages. May be blank during the migration
replaced_by:               # required for deprecated pages. Path of the replacing page
methods:                   # optional, qtl pages. Analyses run on this dataset, shown on the page and in the coverage grid
  cis-QTL: done            # done | running | not_run | awaiting | decide. Leave out methods that do not apply
  SuSiE: done
internal:                  # optional. Not shown on the site. Staging IDs go here. Never file-system paths: the field is still visible in the repository
  staging_ids: []
---
```

| Field | Required | Allowed values |
|---|---|---|
| `type` | always | `study`, `gwas`, `omics`, `qtl`, `reference` |
| `modality` | omics and qtl | modality folder name |
| `cohort` | study, omics, qtl | one cohort name |
| `context` | optional | tissue or cell type |
| `sample_size` | optional | number of samples |
| `access` | optional | `open`, `controlled`, `requested`, `pending` |
| `status` | always | `released`, `staged`, `planned`, `deprecated` |
| `release` | released, deprecated | year and month, for example `2026-10` |
| `synapse_ids` | released | list of public Synapse IDs, may be empty for staged or planned pages |
| `lead_analysts` | always | list of names |
| `last_verified` | released | date of the last Synapse check, may be blank during the migration |
| `replaced_by` | deprecated | path of the replacing page |
| `short_title` | optional | short label for menus, for example `ROSMAP DLPFC` |
| `methods` | optional | map of method to `done`, `running`, `not_run`, `awaiting` or `decide`. Methods: cis-QTL, SuSiE, fSuSiE, ColocBoost, TWAS, cTWAS, MR, LF2, scEEMS |
| `internal` | optional | excluded from the build |

Values marked `# TODO: verify (design placeholder)` came from the site redesign mockup, not from the analysts. Replace them with checked values and remove the comment; `scripts/audit_catalog.py` lists them as placeholders until then.
