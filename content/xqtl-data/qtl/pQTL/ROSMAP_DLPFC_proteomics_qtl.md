---
type: qtl
modality: pQTL
short_title: ROSMAP DLPFC
cohort: ROSMAP
context: DLPFC
sample_size: 416
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
  cTWAS: done
---

# ROSMAP DLPFC protein expression QTL

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) DLPFC protein expression. 

Please refer to [this document](../../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Contact

Zining Qi(zq2209@cumc.columbia.edu)

## Study Overview
 
- Study name : ROSMAP DLPFC proteomics QTL
- Study Description : Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) proteomics QTL analysis summary statistics using the FGC xQTL pipeline. 

Samples' phenotype information (sex, age, race etc.) can be found in ROSMAP metadata, see "Other information" section in [this document](../../study_info/ROSMAP.md)

## Analysis Status

TransQTL association: Finished.

## Links to QTL analysis notebooks

See notebooks in: 

- https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/pQTL

The notebooks in this folder contain the commands and data wrangling codes for analysis of the proteomics data in ROSMAP. (data wrangling exist because not all data are processed using the xqtl-pipeline from the beginning and need to be reformatted to fit one intermediate step of the pipeline).

### Association data preprocessing

phenotype preprocessing can be run in parallel but covariate preprocessing need to be done last since it requires both phenotype data and PCs from PCA in genotype preprocessing.

- [genotype_preprocessing.ipynb](https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/pQTL/genotype_preprocessing.ipynb) shows the commands used for genotype processing and preparation steps, including QC and formatting for genotype data.
- [genotype_pca.ipynb](https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/pQTL/genotype_pca.ipynb) shows the commands used for computing genotype PC for population structure inference.
- [phenotype_preprocessing.ipynb](https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/pQTL/phenotype_preprocessing.ipynb) shows the commands used for the phenotype data formatting steps. QC is not included (should be performed already elsewhere).
- [covariate_preprocessing.ipynb](https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/pQTL/covariates_preprocessing.ipynb) shows the commands used for the covariate data processing and preparation steps, including icomputing molecular phenotype PCA for hidden factor analysis and merging all covariates together.
  
### Association scan using TensorQTL and summary statistics standardization

- [cis_association.ipynb](https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/pQTL/cis_association.ipynb) provides information and result of cis-QTL analysis.
- [trans_association.ipynb](https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/pQTL/trans_association.ipynb) provides information and result of AD genes trans-QTL analysis.

## Analysis Details

### Sample size tracking through the analysis workflow

|Step |Sample Size|
|-----|-----------|
|Raw data|596|
|After overlapping with ROSMAP WGS|512|
|After overlapping with ROSMAP joint call|416|

### QC and Normalization Details for Phenotype Data

Used proteomics data directly without further QC. For QCs performed on data please refer to `descriptor/omics/proteomics/proteomics/ROSMAP_DLPFC_proteomics.md`

### Genotype parameters

- Kinship coefficient for related individuals: 0.0625
- Minor allele count cutoff for single variant analysis: 0
- Variant level missingness threshold: 0.1
- Sample level missingness threshold: 0.1
- HWE cutoof: 1E-08

### Covariate parameters

PCA analysis:
- Minor allele count cutoff for PCA: 5
- LD pruning via PLINK for PCA analysis: window 50, shift 10, r2 0.1
- Tolerance of missingness in covariates: 0.3
- number of pc that captured more than 70% PVE were kept

Hidden Factor analysis - PCA
- Use Marchenko-Pastur limit to choose PCs

Final covariates: Sex, Age at death, PMI, PCs(12), hidden factors(41)

### TensorQTL association scan parameters

- [Extened TADB windows](https://github.com/cumc/fungen-xqtl-analysis/blob/main/resource/extended_cis_before_winsorize.tsv) for cis analysis.
- Trans window for the up and downstream radius to analyze around the region of interest, in units of bp: 1000000
- Minor allele count cutoff: 5
- Minor allele frequency cutoff: 5/(2N), where N is the number of samples in the analysis. The pipeline computes N from the covariate file, so the cutoff differs between datasets.

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

