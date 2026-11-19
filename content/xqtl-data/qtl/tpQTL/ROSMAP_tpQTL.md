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

The Torino paper used 1,193 RNA-seq samples from 729 ROSMAP participants across the three regions. Not every sample has a matching genotype, so the tpQTL mapping uses fewer participants per region.

| Region | RNA-seq samples (Torino paper) | Genotype-matched participants | Female | Male |
|--------|-------------:|-------------:|-------:|-----:|
| Dorsolateral prefrontal cortex (DLPFC) | 118 | 91 | 62 | 29 |
| Posterior cingulate cortex (PCC) | 444 | 370 | 228 | 142 |
| Anterior caudate nucleus (AC) | 631 | 537 | 352 | 185 |

Genotype-matched counts come from the FunGen-xQTL sample table.

## How the tpQTL were mapped

Torino was run twice on 12,297 protein-coding genes, once with three patterns per gene (K3) and once with five (K5). tpQTL were mapped separately in each region with TensorQTL, using cis windows from the FunGen-xQTL TAD boundaries (at least 1 Mb around each gene). Covariates were sex, age at death, post-mortem interval, 15 genotype principal components and hidden factors estimated from the pattern data. The paper reports 45 genes whose tpQTL colocalize with AD risk variants, including KNOP1 (intron retention) and CISD1 (alternative polyadenylation).

## Analyses

The Synapse folders hold two Torino runs, K3 and K5. Both have fine-mapping, cis export and TWAS weights; the ColocBoost model folder has K5 only. Colocalization with AD GWAS (Bellenguez 2022) is in the AD GWAS and xQTL colocalization folder listed above for both runs: K5 as colocalization tables and K3 as a ColocBoost output. The AD Loci Explorer counts tpQTL colocalization as xQTL support for AD loci.
