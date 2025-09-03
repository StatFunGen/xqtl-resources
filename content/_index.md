+++
date = '2025-08-29T11:43:09-04:00'
draft = false
title = 'FunGen xQTL Resources'
+++

# Welcome

# xqtl-resources
### FunGen-xQTL resources navigation

This repository contains a collection of resources related to xQTL, Alzheimer's Disease (AD) loci, fine-mapping, colocalization, TWAS/Mendelian randomization, models, raw data, reference files, and companion analyses. The structure follows folders, subfolders, and file types organized by method and data modality to facilitate downstream analysis and integration.

---

## Repository Content Overview

| Folder / Subfolder                                      | File Types                   | Description / Notes                                                                                                  | Contact Person                      |
|--------------------------------------------------------|------------------------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| `/` (root)                                            | README.md                    | This README summarizing repo contents and links to external data on GitHub/NIAGADS                                    | Gao Wang                          |
| `/variant_gene_summary`                               | —                            | Summary of variants, loci, and genes annotated by xQTL                                                               | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;├─ `/xQTL_loci_summary`         | —                            | Summary of xQTL loci                                                                                                  | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `/xQTL_finemapping`         | UCSC bed.gz                  | Fine-mapping results, structured into contexts and modalities                                                        | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `/single_context_finemapping`    | UCSC bed.gz                  | Per-QTL-type directory containing eQTL, pQTL, sQTL, mQTL, haQTL, caQTL etc. BED files of exported top loci          | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `/multi_context_finemapping`     | UCSC bed.gz                  | Multi-context fine-mapping results (e.g., MSBB, ROSMAP)                                                               | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `/multi_gene_finemapping`        | UCSC bed.gz                  | Per-QTL-type BED files of top loci aggregated across multiple genes                                                   | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ `/trans_finemapping`              | UCSC bed.gz                  | Trans fine-mapping BED files, per QTL type and dataset                                                               | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ `/xQTL_colocalization`         | UCSC bed.gz                  | Colocalization results, structured by multi- and pairwise-context                                                     | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `/multi_context_colocalization`   | UCSC bed.gz                  | Multi-context colocalization results                                                                                  | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ `/pairwise_colocalization`            | UCSC bed.gz / TSV / Misc     | Pairwise colocalization results and related files (bulk mQTL haQTL AD etc.)                                          | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;├─ `/AD_loci_summary`            | —                            | Summary of Alzheimer's Disease (AD) loci                                                                              | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `/AD_finemapping`            | UCSC bed.gz                  | AD GWAS/meta-analysis fine-mapping exported top loci BED files                                                       | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `/AD_colocalization`         | UCSC bed.gz                  | AD GWAS/meta-analysis colocalization exported BED files                                                              | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `/AD_xQTL_colocalization`    | UCSC bed.gz                  | Integrated AD-xQTL colocalization results                                                                             | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `/AD_gene_level`             | —                            | AD gene-level results, including TWAS and cTWAS results                                                            | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `/TWAS_MR`                | UCSC bed.gz                  | TWAS, cTWAS, Mendelian Randomization summary outputs (large combined files)                                           | Ru Feng (with input from Chunming Liu) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ `/cTWAS`                  | UCSC bed.gz                  | AD cTWAS results                                                                                                      | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;├─ `/AD_xQTL_integration_summary`  | XLSX, TSV                    | Summary tables for AD loci annotated by xQTL analyses (fine-mapping, colocalization, TWAS, MR)                       | —                                 |
| `/xQTL_SCEEM_scores`                                  | UCSC bed.gz                  | ML-based xQTL PIP prediction scores on FTP server                                                                   | Chirag Lakhani                   |
| `/xQTL_GWAS_models`                                  | —                            | Pretrained statistical and ML models for data integration                                                           | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;├─ `/xQTL_models`                     | —                            | xQTL models organized by type                                                                                        | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `/finemapping_models`       | RDS                         | Fine-mapping models by QTL type (eQTL, pQTL, glycoQTL, sQTL)                                                        | Ru Feng (main contact)             |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `/colocalization_models`     | RDS                         | Colocalization models                                                                                                | Xuewei Cao                      |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `/TWAS_models`             | RDS                         | TWAS models                                                                                                         | Ru Feng et al.                   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ `/qTWAS_models`             | RDS                         | Quantile TWAS models                                                                                                | Anjing Liu                      |
| &nbsp;&nbsp;&nbsp;&nbsp;├─ `/AD_GWAS_models`                 | RDS                         | AD GWAS fine-mapping and colocalization models                                                                     | Ruixi Li                       |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `/AD_colocalization`                 | RDS                         | AD GWAS colocalization models                                                                     | Ruixi Li                       |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─  `/AD_finemapping`                 | RDS                         | AD GWAS fine-mapping models                                                                     | Ruixi Li                       |
| &nbsp;&nbsp;&nbsp;&nbsp;├─ `/AD_xQTL_integration`            | RDS                         | AD xQTL integration models                                                                                          | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `/AD_xQTL_colocalization_models` | RDS                         | AD xQTL colocalization models                                                                                      | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ `/AD_cTWAS_input`             | RDS                         | AD cTWAS input data                                                                                                  | Chunming Liu                    |
| `/xQTL_data` (raw pre-release area)                   | —                            | Raw xQTL data prior to NIAGADS harmonization; restricted access                                                    | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;├─ `/xQTL_LR`                       | UCSC bed.gz (tensorQTL)      | Linear regression model data and residual sumstats                                                                 | Anjing Liu                      |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `/R_lm_residual_sumstats` | RDS                         | Residual summary statistics for linear models                                   | Anjing Liu                  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ `/tensorQTL_sumstats`    | UCSC bed.gz                  | Summary statistics from tensorQTL                                               | —                           |
| &nbsp;&nbsp;&nbsp;&nbsp;├─ `/xQTL_QR`                       | UCSC bed.gz (tensorQTL)      | Quantile regression model data                                                                                     | Anjing Liu                      |
| &nbsp;&nbsp;&nbsp;&nbsp;├─ `/xQTL_interaction`              | UCSC bed.gz (tensorQTL)      | Interaction analysis data on HPC and cloud                                                                          | Anjing Liu                      |
| &nbsp;&nbsp;&nbsp;&nbsp;└─ `/xQTL_GLMM`                     | UCSC bed.gz (ISSAC)          | Generalized linear mixed model based xQTL calling                                                                  | Yuntian Zhang, Boxiang Liu      |
| `/reference_files`                                    | —                            | Companion analysis supporting files                                                                                 | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;├─ `/ADSP_LD_reference_data`        | —                            | ADSP LD reference data (on Synapse)                                                                                 | Gao Wang                      |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ `/EUR`                   | xz (bim format) with meta data | European population LD reference data                                                                         | Gao Wang                      |
| &nbsp;&nbsp;&nbsp;&nbsp;├─ `/LDSC_reference_data`           | —                            | LDSC reference files including LD scores and annotations                                                           | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `/LD_scores`             | Miscellaneous               | LD scores data on HPC                                                                                                | Anjing Liu                    |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `/sldsc_annotations`     | Miscellaneous               | S-LDSC annotation files on HPC                                                                                       | Anjing Liu                    |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `/GWAS_munged`            | Miscellaneous               | Munged GWAS summary statistics                                                                                      | Ruixi Li                     |
| &nbsp;&nbsp;&nbsp;&nbsp;├─ `/functional_enrichment_annotations` | UCSC bed.gz                  | Functional enrichment annotation files on HPC                                                                       | Anjing Liu                    |
| &nbsp;&nbsp;&nbsp;&nbsp;└─ `/xQTL_protocol_tutorial`        | Miscellaneous               | Toy example and protocol tutorial data compatible with FunGen-xQTL pipeline                                       | Frank Grenn                   |


## Contacts Summary

| Contact Person      | Area of Responsibility                                             |
|---------------------|-------------------------------------------------------------------|
| Gao Wang            | General coordination, README, ADSP LD reference data              |
| Ru Feng             | TWAS/MR outputs, fine-mapping, summary stats, TWAS models         |
| Chunming Liu        | TWAS/MR and cTWAS inputs and model clarifications                 |
| Chirag Lakhani      | ML-based prediction scores                                        |
| Xuewei Cao          | Colocalization models                                            |
| Anqi Wang           | TWAS models input support                                        |
| Anjing Liu          | Quantile TWAS models, raw xQTL data, tensorQTL files, reference data (except GWAS munged) |
| Ruixi Li            | AD GWAS fine-mapping models, GWAS munged data                    |
| Yuntian Zhang       | GLMM-based xQTL calling data                                      |
| Boxiang Liu         | GLMM-based xQTL calling data                                      |
| Frank Grenn         | Protocol tutorial and example data                               |

---

## Additional Notes

- Some data, especially raw or pre-release files, require approval for access. Please contact the relevant person for access requests.  
- Folder organization mirrors the structure of cloud storage and HPC deployment for ease of usage.  
- For detailed info on datasets and file conventions, please refer to linked READMEs or contact the respective persons.  
- For extended xQTL data descriptions, see: [cumc/xqtl-data README](https://github.com/cumc/xqtl-data/blob/main/release_data/README.md)

---

