---
type: qtl
modality: sQTL
short_title: ROSMAP single-nucleus
cohort: ROSMAP
context: "DLPFC, 7 cell types"
sample_size:
access: controlled
status:
synapse_ids: [syn69670592, syn69670600, syn69670611, syn69670597, syn69865816, syn69670630]
lead_analysts: [FunGen-xQTL Analysis Team]
last_verified:
---

# ROSMAP Single-Nucleus Alternative Splicing QTL (snSplicing)

Single-nucleus alternative splicing QTL analysis from CUIMC1 & MIT harmonized snRNA-seq / Multiome data across seven major cell types.

Please refer to [this document](../../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Contact

FunGen-xQTL Analysis Team

## Study Overview

- Study name: ROSMAP snRNA-seq alternative splicing QTL
- Study Description: Splicing quantitative trait loci (sQTL) derived from single-nucleus RNA-seq data using the CUIMC1 & MIT harmonized mega dataset (530 unique donors: CUIMC1 N=424, MIT N=298). Splice-site usage was quantified using the ISSAC pipeline, producing per-cell-type pseudo-bulk splicing phenotypes across 7 major cell types and up to 95 subcell types (67 retained with >3,000 cells).
- Dataset: CUIMC1 & MIT harmonized (mega)
- Cell types: Excitatory neurons (Exc), Inhibitory neurons (Inh), Astrocytes (Ast), Oligodendrocytes (Oli), OPCs (OPC), Microglia (Mic), Endothelial cells (End)

## Analysis Details



### Path(s) to fine-mapping with SuSiE RSS model

Fine-mapping model objects (SuSiE-RSS, `.rds`) are available in the [finemapping models folder (syn69670592)](https://www.synapse.org/Synapse:syn69670592).

### Path(s) to TWAS models

Pre-trained TWAS weight models for this context: [syn69670600](https://www.synapse.org/Synapse:syn69670600)

Quantile TWAS (qTWAS) models: [syn69670611](https://www.synapse.org/Synapse:syn69670611)

### Path(s) to colocalization with SuSiE-coloc / ColocBoost

Multi-context colocalization models (ColocBoost): [syn69670597](https://www.synapse.org/Synapse:syn69670597)

AD GWAS–xQTL colocalization results: [syn69865816](https://www.synapse.org/Synapse:syn69865816)

AD GWAS–xQTL colocalization models: [syn69670630](https://www.synapse.org/Synapse:syn69670630)
