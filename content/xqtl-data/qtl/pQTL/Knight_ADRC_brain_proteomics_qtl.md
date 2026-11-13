---
type: qtl
modality: pQTL
short_title: Knight ADRC brain
cohort: Knight-ADRC
context: parietal cortex
sample_size: 412
access: controlled
niagads: NG00184
status: staged
release:
synapse_ids: [syn69670592, syn69670600, syn69670597, syn69865816, syn69670630]
lead_analysts: [Zining Qi]
last_verified:
methods:
  cis-QTL: done
  SuSiE: done
  TWAS: done
---

# Knight ADRC brain proteomics QTL
Charles F. And Joanne Knight Alzheimer's Disease Research Center (Knight-ADRC)

Please refer to [this document](https://github.com/cumc/xqtl-data/blob/main/descriptor/study_info/KnightADRC.md) for an overview of the Knight project.

## Contact
Zining Qi(zq2209@cumc.columbia.edu)

## Study Overview
 
- Study name : Knight ADRC brain proteomics QTL
- Study Description : Charles F. And Joanne Knight Alzheimer's Disease Research Center (Knight-ADRC) brain proteomics QTL analysis summary statistics using the FGC xQTL pipeline. 

Samples' phenotype information (sex, age, race etc.) can be found in Knight metadata, see "Other information" section in [this document](https://github.com/cumc/xqtl-data/blob/main/descriptor/study_info/KnightADRC.md)

## Analysis Status
TransQTL association: Need to be updated with new covariate files.

## Analysis Details

### Sample size tracking through the analysis workflow

|Step |Sample Size|
|-----|-----------|
|Raw data|442|
|After overlapping with Knight covariates|418|
|After overlapping with Knight genotype|412|

### QC and Normalization Details for Phenotype Data

For QCs performed on data please refer to `descriptor/omics/proteomics/proteomics/Knight_ADRC_brain_proteomics.md`

### Genotype parameters

- Kinship coefficient for related individuals: 0.0625
- Minor allele count cutoff for single variant analysis: 5
- Variant level missingness threshold: 0.1
- Sample level missingness threshold: 0.1

### Covariate parameters

PCA analysis:
- MAF for PCA: 0.05
- LD pruning via PLINK for PCA analysis: window 50, shift 10, r2 0.1
- Tolerance of missingness in covariates: 0.3
- number of pc that captured more than 70% PVE were kept

Hidden Factor analysis - PCA
- Use Marchenko-Pastur limit to choose PCs

Final covariates: Sex, Age at death, PMI, PCs(12), hidden factors(18)

### TensorQTL association scan parameters

- cis/trans window for the up and downstream radius to analyze around the region of interest, in units of bp: 1000000
- Minor allele count cutoff: 5
- Minor allele frequency cutoff: 5/(2N), where N is the number of samples in the analysis. The pipeline computes N from the covariate file, so the cutoff differs between datasets.

## Links to QTL analysis notebooks

See notebooks in: 

- https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Wang_Columbia/knight/pqtl

The notebooks in this folder contain the commands and data wrangling codes for analysis of the proteomics data in ROSMAP. (data wrangling exist because not all data are processed using the xqtl-pipeline from the begnning and need to be reformated to fit one intermediate step of the pipeline).

### Association data preprocessing

phenotype preprocessing can be run in parallel but covariate preprocessing need to be done last since it requires both phenotype data and PCs from PCA in genotype preprocessing.

- [genotype_preprocessing.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/knight/pqtl/genotype_preprocessing.ipynb) shows the commands used for genotype processing and preparation steps.
  - Includes QC, PCA, and PCA result figures.
- [phenotype_preprocessing.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/knight/pqtl/phenotype_preprocessing.ipynb) shows the commands used for the phenotype data processing and preparation steps.
  - This notebook strated from some already cleaned data and covert them to bed format inputs taken by tensorQTL.
- [covariate_preprocessing.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/knight/pqtl/covariates_preprocessing.ipynb) shows the commands used for the covariate data processing and preparation steps.
  - This includes PCA hidden factor analysis steps and merging the PCA hidden factors to covariates and PCA. 
  
### Association scan using TensorQTL and summary statistics standardization

- [cis_pqtl_association.ipynb](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/KnightADRC/pqtl/cis_pqtl_association.ipynb) provides information and result of cis-QTL analysis.
- [trans_pqtl_association.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/knight/pqtl/trans_pqtl_association.ipynb) provides information and result of AD genes trans-QTL analysis.

## Dataset Description

### Path(s) to QTL results

- FTP: 

### Path(s) to cis-QTL association testing

**output of TensorQTL.ipynb**

  
### Path(s) to fine-mapping with SuSiE RSS model

Fine-mapping model objects (SuSiE-RSS, `.rds`) are available in the [fine-mapping models folder (syn69670592)](https://www.synapse.org/Synapse:syn69670592).

### Path(s) to TWAS models

Pre-trained TWAS weight models for this context: [syn69670600](https://www.synapse.org/Synapse:syn69670600)

Quantile TWAS (qTWAS) models: not available yet

### Path(s) to colocalization with SuSiE-coloc / ColocBoost

Multi-context colocalization models (ColocBoost): [syn69670597](https://www.synapse.org/Synapse:syn69670597)

AD GWAS–xQTL colocalization results: [syn69865816](https://www.synapse.org/Synapse:syn69865816)

AD GWAS–xQTL colocalization models: [syn69670630](https://www.synapse.org/Synapse:syn69670630)

