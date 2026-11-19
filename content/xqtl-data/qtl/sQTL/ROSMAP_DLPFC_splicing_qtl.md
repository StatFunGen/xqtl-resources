---
type: qtl
modality: sQTL
short_title: ROSMAP DLPFC
cohort: ROSMAP
context: DLPFC
sample_size: 839
access: controlled
niagads: NG00184
status: staged
release:
synapse_ids: [syn69670592, syn69670600, syn69670597, syn69865816, syn69670630]
lead_analysts: [Shrishtee Kandoi, Xuanhe Chen]
last_verified:
---

# ROSMAP DLPFC alternative splicing QTL

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) DLPFC alternative splicing. 

Please refer to [this document](../../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Contact

Shrishtee Kandoi and Xuanhe Chen

## Study Overview
 
- Study name : ROSMAP DLPFC sQTL
- Study Description : Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) sQTL analysis summary statistics using the FGC xQTL pipeline. 

Samples' phenotype information (sex, age, race etc.) can be found in ROSMAP metadata, see "Other information" section in [this document](../../study_info/ROSMAP.md)

## Analysis Status

TransQTL association: Need to be performed.

## Analysis Details

### Sample size tracking through the analysis workflow

|Step |Sample Size|
|-----|-----------|
|Raw data|1141|
|After overlapping with ROSMAP WGS|839|

### QC and Normalization Details for Phenotype Data

In the case of leafcutter data, any features with over 40% missing values across samples were removed. The remaining missing values were replaced with the mean of existing values, and introns with less than 0.005 variation were eliminated. A scaled normalization was performed on each intron cluster (representing a row of leafcutter data), followed by Quantile-Quantile Normalization on each sample (representing a column of leafcutter data). In contrast, psichomics phenotype data underwent a different imputation approach; zero-imputation was performed to retain "no event detected" information, and only scaled normalization was applied to each event (row).

### Genotype parameters

- Kinship coefficient for related individuals: 0.0625
- Minor allele count cutoff for single variant analysis: 5
- Variant level missingness threshold: 0.1
- Sample level missingness threshold: 0.1
- HWE filter: 1e-06

### Covariate parameters

PCA analysis:
- MAF for PCA: 0.01
- LD pruning via PLINK for PCA analysis: window 50, shift 10, r2 0.1
- Tolerance of missingness in covariates: 0.3
- number of pc that captured more than 70% PVE were kept

PEER analysis (Default values from PEER software):
- The number of max iteration: 1000
- Prior parameter Alpha_a: 0.001
- Prior parameter Alpha_b: 0.1
- Prior parameter Eps_a: 0.1
- Prior parameter Eps_b: 10.0
- Tolerance  parameter tol: 0.001
- Tolerance parameter var_tol: 0.00001
- minimum variance explained criteria to drop factors while training r2_tol: False
- Convergence mode: "fast"

Final covariates: Sex, Age at death, PMI, PCs(13), PEER factors(60)

### TensorQTL association scan parameters

- cis window for the up and downstream radius to analyze around the region of interest, in units of bp: 1000000
- Minor allele count cutoff: 5
- Minor allele frequency cutoff: 5/(2N), where N is the number of samples in the analysis. The pipeline computes N from the covariate file, so the cutoff differs between datasets.

## Links to QTL analysis notebooks for LeafCutter2

See notebooks in: 

- https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/sQTL/DLPFC

The notebooks in this folder contain the commands and data wrangling codes for analysis of the eQTL and sQTL data in ROSMAP. (data wrangling exist because not all data are processed using the xqtl-pipeline from the beginning and need to be reformatted to fit one intermediate step of the pipeline). Since the sQTL phenotype pre-processing used eQTL STAR alignment output, some of the early stage code are shared.

### Association data preprocessing

- [LeafCutter2_QC](https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/sQTL/DLPFC/1.2_dlpfc_leafcutter2_results_QC.ipynb) shows the commands used for quality control of the LeafCutter2 results.

- [genotype_preprocessing.ipynb](https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/haQTL/genotype_preprocessing.ipynb) shows the commands used for genotype processing and preparation steps.all QTLs in one cohort have the same genotype_preprocessing procedure.

- [phenotype_preprocessing.ipynb](https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/sQTL/DLPFC/1_dlpfc_phenotype_preprocessing.ipynb) shows the commands used for the phenotype data processing and preparation steps.

- [covariate_preprocessing.ipynb](https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/sQTL/DLPFC/3_dlpfc_covariate_preprocessing.ipynb) shows the commands used for the covariate data processing and preparation steps.

  
### Association scan using TensorQTL and summary statistics standardization

- [TensorQTL.ipynb](https://github.com/StatFunGen/xqtl-protocol/blob/main/code/SoS/association_scan/TensorQTL/TensorQTL.ipynb) provides the pipeline to generate TensorQTL cis association results for all QTLs. 
- [ROSMAP_sQTL_LeafCutter2_commands](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/cis_association/ROSMAP_sQTL_LeafCutter2/command_generator.ipynb) provides information about the input files for AC/DLPFC/PCC TensorQTL cis association in the base_params variable in [generate_command_1].

### SuSiE univariate fine-mapping

- [fine_mapping.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Zhang_BU/ROSMAP_DLPFC/sQTL/fine_mapping.ipynb) contains the workflow of sQTL univariate fine-mapping using filtered psichomics data.

## Dataset Details

- Number of cases : 
- Number of controls :
- Annotation information : 
- Genotype level imputation : 
- Imputation Panel : 

### Path(s) to genotype matrix 

**output of genotype_qc.ipynb**

### Path(s) to omics-data matrix 

**output of phenotype_preprocessing_sqtl.ipynb**

leafCutter:

psichomics:

### Path(s) to covariate data matrix 

**output of covariate_preprocessing.ipynb**

leafCutter:

   

psichomics:

### Path(s) to QTL results 

**output of association_scan_sQTL.ipynb**

leafCutter:

   
psichomics:

psichomics (grouped by each gene - event_type pair):

### Path(s) to fine-mapping with SuSiE model 

**output of fine_mapping.ipynb**

The results are separated in psi_A3SS, psi_A5SS, psi_AFE, psi_ALE, psi_MXE, psi_SE sub directories according to their event type. Due to the massive amount of files for splicing data they are not listed here.

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