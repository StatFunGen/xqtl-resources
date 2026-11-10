---
type: qtl
modality: haQTL
short_title: ROSMAP DLPFC H3K9ac
cohort: ROSMAP
context: DLPFC
sample_size: 596
access: controlled
status: staged
release:
synapse_ids: [syn69670592, syn69670597, syn69865816, syn69670630]
lead_analysts: [Xuanhe Chen]
last_verified:
methods:
  cis-QTL: done
---

# ROSMAP DLPFC H3K9ac QTL

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) h3k9ac QTL analysis using the FGC xQTL pipeline. 

Please refer to [this document](../../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Contact

Xuanhe Chen (xuanhechenxhc@163.com)

## Study Overview
 
- Study name : ROSMAP DLPFC H3K9ac QTL
- Study Description : Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) h3k9ac QTL analysis summary statistics using the FGC xQTL pipeline. 

Samples' phenotype information (sex, age, race etc.) can be found in ROSMAP metadata, see "Other information" section in [this document](../../study_info/ROSMAP.md)

## Analysis Status

TransQTL association: Need to be performed.

## Analysis Details

### Sample size tracking through the analysis workflow

| Step                                                  | Sample Size |
| ----------------------------------------------------- | ----------- |
| Raw data                                              | 669         |
| Sample 90214403 as been removed from 2022Feb08 ROSMAP | 668         |
| After overlapping with ROSMAP WGS                     | 607         |
| After overlapping with ROSMAP joint call              | 596         |

### QC and Normalization Details for Phenotype Data

Used h3k9ac readcount data directly without further QC. For QCs performed in Chip-seq and peak calling please refer to `descriptor/omics/histone_ChIPSeq/ROSMAP_DLPFC_ChIPSeq_H3K9ac.md`

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

## Links to QTL analysis notebooks

See notebooks in: 

- https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/haQTL

The notebooks in this folder contain the commands and data wrangling codes for analysis of the h3k9ac data in ROSMAP. (data wrangling exist because not all data are processed using the xqtl-pipeline from the beginning and need to be reformatted to fit one intermediate step of the pipeline).

### Association data preprocessing
#### Genotype data preprocessing
We conducted Whole Genome Sequencing (WGS) on 1160 DLPFC samples as part of the ROSMAP study. Post-sequencing, these samples were aligned to the GRCh38 reference genome, and the resulting genetic variants were meticulously cataloged, subsequently being saved in VCF (Variant Call Format) files. To ensure the integrity of our findings, we embarked on a rigorous quality control regimen. This involved the utilization of the GRCh38 reference genome complemented by the GENCODE 34 annotation. Our quality control also used the ERCC spike-in annotations. Specific parameters were meticulously applied: a read depth (--DP) of 1, an indel depth (--DP-indel) of 1, and a Genotype Quality (GQ) threshold exceeding 20. Furthermore, each site was mandated to have at least one sample surpassing the allele balance threshold, specifically set at >= 0.15 for Single Nucleotide Polymorphisms (SNPs) and >= 0.20 for insertion-deletion mutations (indels). This structured approach aimed to ensure a systematic and logical progression in our genomic analysis, reinforcing the academic rigor of our research. After the initial QC, the VCF files were merged using PLINK for downstream analysis. Subsequently, we applied further filters to exclude variants with more than 10% missing data and set a Hardy-Weinberg Equilibrium (HWE) cutoff of 1E-8. The generated genotype files will be subjected to subsequent Principal Component analysis (PCA) as part of the covariates, as well as utilized for QTL mapping. 

#### Principal component analysis for haQTL mapping (this would be the new pipeline)
For the generation of a covariate file for QTL mapping, we initiated the process with Principal Component analysis (PCA) applied to both genome and phenotype data, incorporating several pivotal steps. In the quality control stage, we utilized the KING to segregate samples into related and unrelated categories. PCA was then performed on the unrelated samples using the flashpcaR library, followed by outlier detection to identify pertinent genotype PCs. We retained those with a cumulative explained variance (PVE_cum) of 0.8 or higher and combined them with relevant metadata sexm, gender and post-mortem interval (pmi).
Subsequently, we calculated residuals on these merged covariates and embarked on hidden factor analysis to identify potential batch effects or artifacts in the phenotype data. The number of principal components to be included was determined through a comparison of their eigenvalues to the Marchenko-Pastur Distribution. The principal components identified as hidden factors were incorporated with genotype PCs and metadata into the final amalgamation, serving as the basis for subsequent QTL mapping analysis. 

phenotype preprocessing can be run in parallel but covariate preprocessing needsto be done last since it requires both phenotype data and PCs from PCA in genotype preprocessing.
- [phenotype_calling]() shows the commands used for phenotype calling.
- [genotype_preprocessing.ipynb](https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/haQTL/genotype_preprocessing.ipynb) shows the commands used for genotype processing and preparation steps.
  - Includes QC, PCA, and PCA result figures, for example [h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.h3k9ac.related.filtered.extracted.pca.projected.resid.PEER.diag.pdf](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/haQTL/figures/h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.h3k9ac.related.filtered.extracted.pca.projected.resid.PEER.diag.pdf) is the view of PCA result of the haQTL analysis.
- [phenotype_preprocessing.ipynb](https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/haQTL/phenotype_preprocessing.ipynb) shows the commands used for the phenotype data processing and preparation steps.
  - This notebook strated from some already cleaned data and convert them to bed format inputs taken by tensorQTL.
- [covariate_preprocessing.ipynb](https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/haQTL/covariates_preprocessing.ipynb) shows the commands used for the covariate data processing and preparation steps.
  - This includes PEER factor analysis steps and merging the PEER factors to covariates in raw data and PCA. 
  
### Association scan using TensorQTL and summary statistics standardization
For molecular cis-QTL mapping, we utilized quantified H3K9ac levels in BED format as phenotypes, principal components (PCs) obtained as previously described as covariates, and corresponding genotype data from the same dataset in PLINK format, as delineated in prior descriptions. 
We employed the TensorQTL pipeline to perform the association analysis, setting a minor allele count (MAC) cutoff of 5. This approach allowed us to generate phenotype-level summary statistics with empirical p-values, facilitating the calculation of genome-wide false discovery rates (FDR) through permutations. Additionally, summary statistics were obtained for all variant-phenotype pairs.
During this process, we strategically expanded the cis window to capture signals that were not confined to the coordinate level, but rather operated on the spatial level within a specific region. The cis window was meticulously defined as a region encompassing 1,000,000 base pairs, in addition to the topologically associated domain (TAD) and its boundary (TAB). This was executed with an understanding that variants located within this spatial domain could exert an impact on gene expression, thus associating with the corresponding gene. In instances where a gene was positioned within the confines of two generalized TABD boundaries, we systematically selected the outermost TABD boundary for incorporation into the cis window definition, ensuring a comprehensive and rigorous approach to our spatial genomic analysis.

### SuSiE univariate fine-mapping

- [univariate_fine_mapping.ipynb](https://github.com/StatFunGen/xqtl-protocol/blob/main/code/SoS/mnm_analysis/mnm_methods/mnm_regression.ipynb) contains the workflow of haQTL univariate fine-mapping.

## Dataset Details

- Number of cases : 
- Number of controls :
- Annotation information : 
- Genotype level imputation : 
- Imputation Panel : 

### Path(s) to genotype matrix 

**output of genotype_preprocessing.ipynb**

### Path(s) to omics-data matrix 

**output of phenotype_preprocessing.ipynb**

### Path(s) to covariate data matrix 

**output of covariate_preprocessing.ipynb**

### Path(s) to cis-QTL association testing

**output of cis_haqtl_association.ipynb**

- `/projects/histone-methylation/CU/h3k9_sumstats/`
### Path(s) to fine-mapping with SuSiE model 

**output of univariate_fine_mapping.ipynb**

### Path(s) to fine-mapping with fSuSiE / SuSiE RSS model

Fine-mapping model objects (fSuSiE/SuSiE-RSS, `.rds`) are available in the [fine-mapping models folder (syn69670592)](https://www.synapse.org/Synapse:syn69670592).

### Path(s) to colocalization

Pairwise colocalization models (SuSiE-coloc): [syn69670597](https://www.synapse.org/Synapse:syn69670597)

AD GWAS–xQTL colocalization results: [syn69865816](https://www.synapse.org/Synapse:syn69865816)

AD GWAS–xQTL colocalization models: [syn69670630](https://www.synapse.org/Synapse:syn69670630)
