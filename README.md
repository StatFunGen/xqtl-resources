# xqtl-resources
### FunGen-xQTL resources navigation

This repository contains a collection of resources related to xQTL, Alzheimer's Disease (AD) loci, fine-mapping, colocalization, TWAS/Mendelian randomization, models, raw data, reference files, and companion analyses. The structure follows folders, subfolders, and file types organized by method and data modality to facilitate downstream analysis and integration.

---

## Repository Content Overview

| Folder / Subfolder                        | File Types           | Description / Notes                                                                                              | Contact Person                      |
|------------------------------------------|---------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------|
| `/` (root)                              | README.md              | This README summarizing repo contents and links to external data on GitHub/NIAGADS                                | Gao Wang                          |
| `/variant_gene_summary`                  | —        | Summary of variants, loci, and genes annotated by xQTL                                                           | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;├─ `/xQTL_loci_summary`         | —         | Summary of xQTL loci                                                                                              | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `/xQTL_finemapping`       | UCSC bed.gz         | Fine-mapping results, structured by method and modality                                                          | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ `/xQTL_colocalization`    | UCSC bed.gz         | Colocalization results, structured by method and modality                                                        | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;├─ `/AD_loci_summary`           | —         | Summary of Alzheimer's Disease (AD) loci                                                                         | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `/AD_finemapping`          | UCSC bed.gz         | AD fine-mapping results, structured by method and modality                                                       | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `/AD_colocalization`      | UCSC bed.gz         | AD colocalization results, structured by method and modality                                                     | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ `/AD_xQTL_colocalization`  | UCSC bed.gz         | AD-xQTL integrated colocalization results                                                                        | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp; ├─ `/AD_TWAS_MR`                           | UCSC bed.gz         | TWAS, cTWAS, and Mendelian Randomization summary outputs (large combined files)                                  | Ru Feng (with input from Chunming Liu) |
| &nbsp;&nbsp;&nbsp;&nbsp; ├─ `/AD_xQTL_integration`                  | XLSX, TSV for AD_xQTL_loci and AD_xQTL_genes           | Summarized tables annotating AD loci by xQTL analyses (fine-mapping, colocalization, TWAS, MR)                   | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp; ├─ `/xQTL_SCEEM_scores`                    | UCSC bed.gz         | ML-based xQTL PIP prediction scores on FTP server                                                                              | Chirag Lakhani                   |
| `/xQTL_GWAS_models`                     | —                 | Pretrained statistical and ML models for data integration                                                         | —                   |
| &nbsp;&nbsp;&nbsp;&nbsp;├─ `/xQTL_finemapping_models`   | RDS                 | Fine-mapping models                                                                                                | Ru Feng                         |
| &nbsp;&nbsp;&nbsp;&nbsp;├─ `/xQTL_regional_sumstats`    | RDS                 | Companion summary statistics for fine-mapping models                                                              | Ru Feng                         |
| &nbsp;&nbsp;&nbsp;&nbsp;├─ `/xQTL_colocalization_models`| RDS                 | Colocalization models                                                                                              | Xuewei Cao                     |
| &nbsp;&nbsp;&nbsp;&nbsp;├─ `/xQTL_TWAS_models`          | RDS                 | TWAS models                                             | Ru Feng (with inputs/clarifications by Anqi Wang & Chunming Liu)|
| &nbsp;&nbsp;&nbsp;&nbsp;├─ `/xQTL_qTWAS_models`         | RDS                 | Quantile TWAS models on HPC                                                                                        | Anjing Liu                    |
| &nbsp;&nbsp;&nbsp;&nbsp;├─ `/AD_GWAS_finemapping_models`| RDS                 | AD GWAS summary stats based fine-mapping models                                                                                   | Ruixi Li                       |
| &nbsp;&nbsp;&nbsp;&nbsp;└─ `/AD_cTWAS_input`            | RDS                 | AD cTWAS input data                                                                                               | Chunming Liu                  |
| `/xQTL_data` (raw pre-release area)     | —        | Raw xQTL data prior to NIAGADS harmonization; restricted access                                                  | — |
| &nbsp;&nbsp;&nbsp;&nbsp;├─ `/xQTL_LR`                 | UCSC bed.gz (tensorQTL)        | Linear regression model data on FTP server                                                                                     | Anjing Liu                    |
| &nbsp;&nbsp;&nbsp;&nbsp;├─ `/xQTL_QR`                 | UCSC bed.gz (tesorQTL)        | Quantile regression model data on FTP server                                                                                   | Anjing Liu                    |
| &nbsp;&nbsp;&nbsp;&nbsp;├─ `/xQTL_interaction`         | UCSC bed.gz (tensorQTL)        | Interaction analysis data on HPC and cloud                                                                                         | Anjing Liu                    |
| &nbsp;&nbsp;&nbsp;&nbsp;└─ `/xQTL_GLMM`                | UCSC bed.gz (ISSAC)        | Generalized linear mixed model based xQTL calling                                                                 | Yuntian Zhang, Boxiang Liu    |
| `/reference_files`                      |  —              | Companion analysis supporting files                                                       |  —                 |
| &nbsp;&nbsp;&nbsp;&nbsp;├─ `/ADSP_LD_reference_data` | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `/EUR` | xz (bim format) with meta data    | ADSP LD reference data (on Synapse)                                                                                   | Gao Wang                      |
| &nbsp;&nbsp;&nbsp;&nbsp;├─ `/LDSC_reference_data` | —                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `/LD_scores` | Misc. file     | LD reference data on HPC                                                                                   | Anjing Liu                      |Miscellaneous       | LD scores, S-LDSC annotations, munged GWAS data   
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `/sldsc_annoatations` | Misc. file    | LD reference data on HPC                                                                                   | Anjing Liu                      |Miscellaneous       | LD scores, S-LDSC annotations, munged GWAS data  
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `/GWAS_munged` | Misc. file     | LD reference data on HPC                                                                                   | Ruixi Li                      |Miscellaneous       | LD scores, S-LDSC annotations, munged GWAS data                                                                | Anjing Liu (except GWAS munged), Ruixi Li (GWAS munged) |
| &nbsp;&nbsp;&nbsp;&nbsp;├─ `/functional_enrichment_annotations`| UCSC bed.gz       | Functional enrichment annotation files on HPC                                                                           | Anjing Liu                    |
| &nbsp;&nbsp;&nbsp;&nbsp;└─ `/xQTL_protocol_tutorial`   | Misc. file             | Toy example and protocol tutorial data compatible with FunGen-xQTL pipeline                                     | Frank Grenn                   |

---

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

