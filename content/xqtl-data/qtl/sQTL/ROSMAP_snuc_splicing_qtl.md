# ROSMAP Single-Nucleus Alternative Splicing QTL (snSplicing)

Single-nucleus alternative splicing QTL analysis from CUIMC & MIT harmonized snRNA-seq / Multiome data across six cell types.

Please refer to [this document](../../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Contact

FunGen-xQTL Analysis Team

## Study Overview

- Study name: ROSMAP snRNA-seq alternative splicing QTL
- Study Description: Splicing quantitative trait loci (sQTL) derived from single-nucleus RNA-seq data using the CUIMC & MIT harmonized mega dataset. Splice-site usage was quantified using the ISSAC-seq pipeline, producing per-cell-type pseudo-bulk splicing phenotypes for six cell types.
- Dataset: CUIMC & MIT harmonized (mega)
- Cell types: Microglia (Mic), Astrocytes (Ast), Oligodendrocytes (Oli), OPCs (OPC), Excitatory neurons (Exc), Inhibitory neurons (Inh)

## Analysis Details

### Path(s) to cis-QTL association testing

- `s3://statfungen/ftp_fgc_xqtl/analysis_result/cis_association/ROSMAP/sQTL/snuc_mega/`

### Path(s) to fine-mapping with SuSiE RSS model

Fine-mapping model objects (SuSiE-RSS, `.rds`) are available in the [finemapping models folder (syn69670592)](https://www.synapse.org/Synapse:syn69670592).

### Path(s) to TWAS models

Pre-trained TWAS weight models for this context: [syn69670600](https://www.synapse.org/Synapse:syn69670600)

Quantile TWAS (qTWAS) models: [syn69670611](https://www.synapse.org/Synapse:syn69670611)

### Path(s) to colocalization with SuSiE-coloc / ColocBoost

Multi-context colocalization models (ColocBoost): [syn69670597](https://www.synapse.org/Synapse:syn69670597)

AD GWAS–xQTL colocalization results: [syn69865816](https://www.synapse.org/Synapse:syn69865816)

AD GWAS–xQTL colocalization models: [syn69670630](https://www.synapse.org/Synapse:syn69670630)
