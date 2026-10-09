---
type: gwas
status:
synapse_ids: []
lead_analysts: []
last_verified:
---

# <Trait> GWAS Summary Data (<First author>)

One to two sentences: trait, study, publication (DOI and journal), ancestry, and genome build.

## Contact

Name(s) of the data owner or lead analyst.

## Access

- Public source: link to the original public release (e.g., GWAS Catalog accession), if any.
- Synapse: synapse IDs of the processed summary statistics and fine-mapping objects (see `synapse_ids` above).
- Access conditions: public, controlled (name the data access committee), or lab-internal.

Do not list cluster, HPC, or local file-system paths. Point to Synapse IDs or public URLs only.

## File Schema

- `column_name`: description (one line per column)

## Cohorts and sample size

Total cases and controls, and one line per contributing cohort. Report aggregate counts only; do not include participant-level or small-cell (n < 10) data.

## Analysis notebooks

1. GWAS summary statistics processing: link to the public notebook
2. Fine-mapping (SuSiE RSS): link to the public notebook

## Integration with xQTL

Synapse IDs of the colocalization, TWAS, and unified-loci summaries that use this GWAS.
