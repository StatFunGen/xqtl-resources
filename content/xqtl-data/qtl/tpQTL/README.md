# Transcriptomic pattern QTL (tpQTL) Resources

Transcriptomic pattern QTL (tpQTL) are variants associated with patterns of RNA-seq read coverage within a gene. Torino models coverage across each gene jointly to define the pattern traits. tpQTL come from the same RNA-seq data as eQTL and sQTL, so the FunGen-xQTL paper counts them under its eight molecular modalities.

## Available Datasets

| Dataset | Cohort / Brain Region | AD Knowledge Portal |
|---------|-----------------------|---------|
| [ROSMAP DLPFC, PCC, AC](ROSMAP_tpQTL) | ROSMAP bulk brain, three regions | [syn77650756](https://www.synapse.org/Synapse:syn77650756) |

## Analyses Performed

- Single-context fine-mapping with SuSiE and cis export, for the K3 and K5 Torino runs
- ColocBoost colocalization models (K5)
- TWAS weights (K3 and K5)
- Colocalization with AD GWAS (Bellenguez 2022)
