---
type: qtl
modality: tpQTL
short_title: ROSMAP DLPFC, PCC, AC
cohort: ROSMAP
context: DLPFC, PCC, AC
sample_size:
sample_note: 91 to 537 by region
access: controlled
status: staged
release:
synapse_ids: [syn77650756, syn77652326, syn77827202, syn69865816]
lead_analysts: []
last_verified:
methods:
  SuSiE: done
  TWAS: done
---

# ROSMAP transcriptomic pattern QTL

Transcriptomic pattern QTL (tpQTL) are variants associated with patterns of RNA-seq read coverage within a gene. Torino models coverage across each gene jointly and defines the pattern traits; tpQTL mapping then tests these traits in ROSMAP bulk brain RNA-seq from three regions.

Please refer to [this document](../../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Samples

Genotype-matched participants per region, from the FunGen-xQTL sample table.

| Region | Participants | Female | Male |
|--------|-------------:|-------:|-----:|
| Dorsolateral prefrontal cortex (DLPFC) | 91 | 62 | 29 |
| Posterior cingulate cortex (PCC) | 370 | 228 | 142 |
| Anterior caudate nucleus (AC) | 537 | 352 | 185 |

## Analyses

The Synapse folders hold two Torino runs, K3 and K5. Both have fine-mapping, cis export and TWAS weights; the ColocBoost model folder has K5 only. Colocalization with AD GWAS (Bellenguez 2022) is in the AD GWAS and xQTL colocalization folder listed above for both runs: K5 as colocalization tables and K3 as a ColocBoost output. The AD Loci Explorer counts tpQTL colocalization as xQTL support for AD loci.
