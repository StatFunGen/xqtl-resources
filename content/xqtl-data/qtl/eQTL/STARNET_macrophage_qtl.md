---
type: qtl
modality: eQTL
short_title: STARNET macrophage
cohort: STARNET
context: macrophage
access: controlled
status: staged
release:
synapse_ids: [syn69670592, syn69670600, syn69670611, syn69670597, syn69865816, syn69670630]
lead_analysts: [Travyse Edwards]
last_verified:
sample_size: 471
methods:
  SuSiE: done
  TWAS: done
---

# STARNET macrophage gene expression QTL

STARNET is an RNA expression study of various disease-relevant tissues obtained from living patients with cardiovascular disease (CVD). The inclusion criterion for patients was eligibility for coronary artery by-pass graft (CABG) surgery.
Please refer to [this document](../../study_info/STARNET.md) for an overview of the STARNET project.
## Contact

- Contact Name: Travyse Edwards
- Contact Email: travyse.edwards@icahn.mssm.edu
- Contact Affiliation: Icahn School of Medicine at Mount Sinai
- Contact Role: Travyse performed QC & QTL analysis

## Study Overview

- Study name : STARNET Macrophage eQTL
- Study Description : Stockholm-Tartu Atherosclerosis Reverse Network Engineering Task (STARNET) macrophage eQTL analysis summary statistics generated using the FGC xQTL pipeline.

## Analysis Details

### Sample Size Tracking Through Analysis Workflow

|Step |Sample Size|
|-----|-----------|
|Raw Expression Data|480|
|QC'd Expression Data|479|
|After overlapping with STARNET genotype data|471|

### Quality Control and Normalization Details for Phenotype Data

For quality control performed for the macrophage gene expression dataset, please refer to [this markdown document](https://github.com/Travyse/brain-xqtl-analysis/blob/main/data/descriptor/omics/expression/STARNET_macrophage.md).

### Genotype Parameters

|Parameter |Value|
|----------|-----|
|Minimum Minor Allele Freq|0.01|
|Maximum Minor Allele Freq|0.99|
|Kinship Coefficient for Related Individuals|0.0625|
|Maximum Missingness Per Variant|0.1|
|Maximum Missingness Per Sample|0.1|
|Hardy-Weinberg Equilibrium Filter|1e-15|

### Covariate Parameters

PCA Analysis:

|Parameter |Value|
|----------|-----|
|Minor Allele Freq for PCA|0.01|
|LD Pruning: Window|0.1|
|LD Pruning: Shift|0.1|
|LD Pruning: Window|0.1|
|Number of PCs|13|

PEER Analysis:

|Parameter |Value|
|----------|-----|
|Max Iterations|1000|
|Prior Parameter: `Alpha_a`|0.001|
|Prior Parameter: `Alpha_b`|0.1|
|Prior Parameter: `Eps_a`|0.1|
|Prior Parameter: `Eps_b`|10.0|
|Tolerance Parameter: `tol`|0.001|
|Tolerance Parameter: `var_tol`|1e-5|
|Convergence Mode| "fast"|

Final Covariates: Sex, Age, PCs (13), PEER Factors (60)

PCA Method for Latent Factor Identification (Using Marchenko-Pastur Method):

TBD

### TensorQTL Parameters

|Parameter |Value|
|----------|-----|
|Cis Window|1,000,000|
|Minor Allele Count Cutoff|0|
|Minor Allele Freq Cutoff|0|

## Links to QTL analysis notebooks

Currently rearranging this section and below

The notebooks in this folder, 

https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Marcora_MSSM/STARNET

contain the commands and some of the results visualizations produced by the pipeline when analyzing the STARNET macrophage RNA-seq expression data.

- `STARNET_Analysis_Complete.ipynb` provides information about the imputation of genotype, summary from other preprocessing steps, and a look into the cisQTL association scan.
- `genotype_preprocessing.ipynb` shows the commands used for genotype processing and preparation steps.
  - Mostly contains the commands used to run the pipeline, but includes some pre-pipeline data wrangling.
  - This includes QC, PCA, and GRM steps
- `phenotype_preprocessing.ipynb` shows the commands used for the phenotype data processing and preparation steps.
  - As above, it mostly contains the commands used to run the pipeline, but includes some pre-pipeline data wrangling.
  - This includes quantification steps, QC, annotation, and residual expression steps
- `covariate_preprocessing.ipynb` shows the commands used for the covariate data processing and preparation steps.
  - This includes factor analysis steps
- `association_scan_cis.ipynb` provides information about the TensorQTL cis association scan.

Wang lab: 
- [TensorQTL.ipynb](https://github.com/cumc/xqtl-protocol/blob/main/code/association_scan/TensorQTL/TensorQTL.ipynb) provides the pipeline to generate TensorQTL cis association results for all QTLs. 
- [STARNET_eQTL](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/cis_association/STARNET_eQTL/command_generator.ipynb) provides information about the input files for TensorQTL cis association in the base_params variable in [generate_command_1].

## Dataset Details

- Number of cases :
- Number of controls :
- Annotation information :
- Genotype level imputation :
- Imputation Panel :

### Path(s) to fine-mapping with SuSiE RSS model

Fine-mapping model objects (SuSiE-RSS, `.rds`) are available in the [finemapping models folder (syn69670592)](https://www.synapse.org/Synapse:syn69670592).

### Path(s) to TWAS models

Pre-trained TWAS weight models for this context: [syn69670600](https://www.synapse.org/Synapse:syn69670600)

Quantile TWAS (qTWAS) models: [syn69670611](https://www.synapse.org/Synapse:syn69670611)

### Path(s) to colocalization with SuSiE-coloc / ColocBoost

Multi-context colocalization models (ColocBoost): [syn69670597](https://www.synapse.org/Synapse:syn69670597)

AD GWAS–xQTL colocalization results: [syn69865816](https://www.synapse.org/Synapse:syn69865816)

AD GWAS–xQTL colocalization models: [syn69670630](https://www.synapse.org/Synapse:syn69670630)
