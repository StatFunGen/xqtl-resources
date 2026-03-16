# ROSMAP AC gene expression

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) AC gene expression. 

Please refer to [this document](../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Contact 

Frank Grenn

## Data Descriptions

**Verifying current avaliable location for the dataset now**

Samples were extracted using Qiagen's miRNeasy mini kit (cat. no. 217004) and the RNase free DNase Set (cat. no. 79254), and quantified by Nanodrop and quality was evaluated by Agilent Bioanalyzer.

| Brain      | Description |
| -----------| ----------- |
| Batch 1    | 638         |
| Batch 2    | 252 (117 for PolyA selection & 135 for rRNA depletion)        |
| Batch 3    | 251         |
| Total      | 1141        |

**Notes regarding sample naming:** Sequencing samples that were sequenced more than once include the sequencing batch number as the last 2 digits of the id. For example, sample 123_456789_02 is sample "123_456789", from batch 2. The sample IDs are otherwise randomly-assigned identifiers. Some samples were re-sequenced due to poor quality or low output, they may have "redo" in the sample identifier.


## eQTL analysis performed by Gao Wang's Lab and Xiaoling Zhang's lab

### Analyst

Shrishtee Kandoi, Hao Sun

### Analysis Description

Brain multi-region RNA-seq data was proccessed with the xQTL-pipeline, for analysis detial please check records here: [eQTL](https://github.com/cumc/brain-xqtl-analysis/tree/main/analysis/Zhang_BU/ROSMAP_DLPFC/eQTL) [eQTL_susie_result_analysis
](https://github.com/cumc/brain-xqtl-analysis/tree/main/analysis/Wang_Columbia/eqtl)

- Genotype used in this analysis on BU cluster: `/restricted/projectnb/casa/skandoi/ROSMAP_DLPFC/genotype_partition/ROSMAP_NIA_WGS.leftnorm.filtered.filtered.plink_files_list.txt`

- Covariates used in this analysis on BU cluster: `/restricted/projectnb/casa/skandoi/ROSMAP_DLPFC/reference_data/ROSMAP_xqtl_covariates_sex_death_pmi_study.tsv`

### Results

- Output summary statistics are uploaded to the FTP server: `/ftp_fgc_xqtl/projects/rna-seq/BU/ROSMAP_DLPFC/eQTL/association_scan`

## sQTL analysis performed by Gao Wang's Lab and Xiaoling Zhang's lab

### Analyst

Shrishtee Kandoi, Xuanhe Chen

### Analysis Description

Brain multi-region RNA-seq data was proccessed with the xQTL-pipeline, for analysis detial please check records here: [sQTL](https://github.com/cumc/brain-xqtl-analysis/tree/main/analysis/Zhang_BU/ROSMAP_DLPFC/sQTL)

- Genotype used in this analysis on BU cluster: `/restricted/projectnb/casa/skandoi/ROSMAP_DLPFC/genotype_partition/ROSMAP_NIA_WGS.leftnorm.filtered.filtered.plink_files_list.txt`

- Covariates used in this analysis on BU cluster: `/restricted/projectnb/casa/skandoi/ROSMAP_DLPFC/reference_data/ROSMAP_xqtl_covariates_sex_death_pmi_study.tsv`

### Results

In this analysis we performed two methods: leafcutter and psichomics.

#### leafcutter

- Output summary statistics are uploaded to the FTP server: `/ftp_fgc_xqtl/projects/rna-seq/BU/ROSMAP_DLPFC/sQTL/association_scan/`

#### psichomics

- data generation using psichomics still in progress

## Study Metadata

- **PI**: David A. Bennett (Rush University Medical Center, Chicago, IL, USA)
- **Grant numbers**: U01AG046152, R01AG048015, U01AG061356, R01AG15819, U01AG061359
- **Publication**: PMID: 30084846
- **Genetics publication**: PMID: 40407102
- **Acknowledgement**: Study data were generated from postmortem brain tissue provided by the Religious Orders Study and Rush Memory and Aging Project (ROSMAP) cohort at Rush Alzheimer's Disease Center, Rush University Medical Center, Chicago.
- **Omics data**: [syn3388564](https://www.synapse.org/Synapse:syn3388564)
- **Genetics data**: [ng00067](https://dss.niagads.org/datasets/ng00067/)
## QTL Analysis
QTL analysis for this dataset is documented in [../qtl/ROSMAP_AC_expression_qtl.md](../qtl/ROSMAP_AC_expression_qtl.md).

Flagship paper analyses:
- Fine-mapping (SuSiE-RSS): [syn69670592](https://www.synapse.org/Synapse:syn69670592)
- TWAS weight models: [syn69670600](https://www.synapse.org/Synapse:syn69670600)
- Quantile TWAS (qTWAS) models: [syn69670611](https://www.synapse.org/Synapse:syn69670611)
- Multi-context colocalization (ColocBoost): [syn69670597](https://www.synapse.org/Synapse:syn69670597)
- AD GWAS–xQTL colocalization results: [syn69865816](https://www.synapse.org/Synapse:syn69865816)
- AD GWAS–xQTL colocalization models: [syn69670630](https://www.synapse.org/Synapse:syn69670630)
