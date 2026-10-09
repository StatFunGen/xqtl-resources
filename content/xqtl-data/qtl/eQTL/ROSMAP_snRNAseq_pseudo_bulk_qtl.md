---
type: qtl
modality: eQTL
short_title: ROSMAP snuc-eQTL
cohort: ROSMAP
context: "DLPFC, 7 cell types"
sample_size:
access: controlled
status:
release:
synapse_ids: [syn69670592, syn69670600, syn69670611, syn69670597, syn69865816, syn69670630]
lead_analysts: [Hao Sun, Masashi Fujita]
last_verified:
---

# ROSMAP snRNA-seq pseudo-bulk gene expression QTL

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) snRNA-seq from different cells in Dorsolateral Prefrontal Cortex (DLPFC). 

Please refer to [this document](../../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Contact

Hao Sun (eQTL), Masashi Fujita (eQTL), Haochen Sun (fine-mapping), Jiajun Tao (replication)

## Study Overview

- Sample information: `ROSMAP/ROSMAP_Pseudo_Bulk_sample_attributes.csv`.
- Lab protocol: `ROSMAP/ROSMAP_Pseudo_Bulk_lab_protocol.csv`.
- Computational protocol: `ROSMAP/ROSMAP_Pseudo_Bulk_computational_protocol.csv`.
- QTL summary statistics output: `####/####.qtl_results.csv`.
- Fine-mapping results individual level data model: `####/####.susie.csv`.
- Fine-mapping results summary statistics model: `####/####.susie_rss.csv`.

## Analysis Status

TransQTL association: Finished.

## Dataset Description

### Path(s) to genotype matrix

#### Using `MatrixQTL` pipeline (by Masashi)

1. genotype is an all-chromosome, all-samples vcf collection
2. The original `gz` vcf is `gzipped` but not `bgzipped`, thus cannot `tabix -p`
3. The vcf is not imputed.
- Dosage file. The number of ALT allele were counted per donor.

- SNP position file in GRCh38

- VCF file used to generate above files. This is a subset of ROSMAP WGS VCF.

- The original VCF files of ROS/MAP WGS is here (N = 1,196; GRCh37):

- A summary of quality control is here:

- Liftover of the above VCFs from GRCh37 to GRCh38.

- Sorted positions of SNPs, added rsID in dbSNP154, and renamed chromosomes (e.g. 1 to chr1).

- 424 donors extracted for snRNAseq and applied filtering of MAF, HWE, etc.



### Path(s) to covariate data matrix

#### Using `MatrixQTL` pipeline (by Masashi)

Here, I use astrocytes as an example. But all other cell types have the same folder structure.

Covariates of eQTL analysis are sex, age, PMI, study, total genes detected, top 3 genotype PCs, and up to 30 expression PCs. 


#### Using `TenorQTL` pipeline (by Hao)

### Path(s) to QTL results

#### Using `MatrixQTL` pipeline (by Masashi)


Take astrocytes as an example,


```r
df <- readRDS("matrix-eqtl.rds")$cis$eqtl
``` 

#### Using `TenorQTL` pipeline (by Hao)




### Association scan using TensorQTL and summary statistics standardization

- [TensorQTL.ipynb](https://github.com/cumc/xqtl-protocol/blob/main/code/association_scan/TensorQTL/TensorQTL.ipynb) provides the pipeline to generate TensorQTL cis association results for all QTLs. 
- [ROSMAP_DeJager_snuc_eQTL](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/cis_association/ROSMAP_DeJager_snuc_eQTL/command_generator.ipynb) provides information about the input files for TensorQTL cis association in the base_params variable in [generate_command_1].
- [ROSMAP_Kellis_eQTL](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/cis_association/ROSMAP_Kellis_eQTL/command_generator.ipynb) provides information about the input files for TensorQTL cis association in the base_params variable in [generate_command_1].
- [ROSMAP_mega_eQTL](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/cis_association/ROSMAP_mega_eQTL/command_generator.ipynb) provides information about the input files for TensorQTL cis association in the base_params variable in [generate_command_1].


### Path(s) to cis-QTL association testing

**output of TensorQTL.ipynb**

  
### Path(s) to fine-mapping with SuSiE RSS model

Fine-mapping model objects (SuSiE-RSS, `.rds`) are available in the [finemapping models folder (syn69670592)](https://www.synapse.org/Synapse:syn69670592).

### Path(s) to TWAS models

Pre-trained TWAS weight models for this context: [syn69670600](https://www.synapse.org/Synapse:syn69670600)

Quantile TWAS (qTWAS) models: [syn69670611](https://www.synapse.org/Synapse:syn69670611)

### Path(s) to colocalization with SuSiE-coloc / ColocBoost

Multi-context colocalization models (ColocBoost): [syn69670597](https://www.synapse.org/Synapse:syn69670597)

AD GWAS–xQTL colocalization results: [syn69865816](https://www.synapse.org/Synapse:syn69865816)

AD GWAS–xQTL colocalization models: [syn69670630](https://www.synapse.org/Synapse:syn69670630)

## Links to QTL analysis notebooks 
pseudo_bulk_eQTL_DeJager:
[Preprocess_bundle](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pseudo_bulk_eQTL_DeJager/Preprocess_bundle.ipynb) provides commands to preprocess genotype, phenotype and covariate data all at once.
[Phenotype_preprocessing](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pseudo_bulk_eQTL_DeJager/ALL/phenotype_preprocessing.ipynb) shows the commands used for the phenotype data processing and preparation steps for all cell types. Cell-specific phenotype preprocessing are listed [here in different folders](https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/pseudo_bulk_eQTL_DeJager).


pseudo_bulk_eQTL_Kellis:
[Preprocess_bundle](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pseudo_bulk_eQTL_Kellis/Preprocess_bundle.ipynb) provides commands to preprocess genotype, phenotype and covariate data all at once.
[Genotype_pca](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pseudo_bulk_eQTL_Kellis/genotype_pca.ipynb) provides steps for PCA analysis for genotype data.
[Phenotype_preprocessing](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pseudo_bulk_eQTL_Kellis/phenotype_preprocessing.ipynb) shows the commands used for the phenotype data processing and preparation steps.
[Covariates_preprocessing](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pseudo_bulk_eQTL_Kellis/covariates_preprocessing.ipynb) shows the commands used for the covariate data processing and preparation steps.


pseudo_bulk_eQTL_mega:
[Genotype_pca](https://github.com/rl3328/xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pseudo_bulk_eQTL_mega/genotype_pca.ipynb) provides steps for PCA analysis for genotype data.
[Phenotype_preprocessing](https://github.com/rl3328/xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pseudo_bulk_eQTL_mega/phenotype_preprocessing.ipynb) shows the commands used for the phenotype data processing and preparation steps.
[Covariates_preprocessing](https://github.com/rl3328/xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pseudo_bulk_eQTL_mega/covariates_preprocessing.ipynb) shows the commands used for the covariate data processing and preparation steps.
