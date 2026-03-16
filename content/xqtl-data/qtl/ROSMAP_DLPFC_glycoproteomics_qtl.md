# ROSMAP DLPFC protein expression QTL

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) DLPFC protein expression. 

Please refer to [this document](../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Contact



## Study Overview
 
- Study name : ROSMAP Glyco_proteomics QTL
- Study Description : Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) proteomics QTL analysis summary statistics using the FGC xQTL pipeline. 

Samples' phenotype information (sex, age, race etc.) can be found in ROSMAP metadata, see "Other information" section in [this document](../study_info/ROSMAP.md)

## Analysis Status

TransQTL association: 

## Links to QTL analysis notebooks

See notebooks in: 

- https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/KnightADRC/mQTL

The notebooks in this folder contain the commands and data wrangling codes for analysis of the methylation data in KnightADRC. (data wrangling exist because not all data are processed using the xqtl-pipeline from the beginning and need to be reformatted to fit one intermediate step of the pipeline).

### Association data preprocessing
#### Genotype data preprocessing

#### Principal component analysis for eQTL mapping

#### Phenotype data preprocessing

#### Covariate data preprocessing

### Association scan using TensorQTL and summary statistics standardization

- [TensorQTL.ipynb](https://github.com/cumc/xqtl-protocol/blob/main/code/association_scan/TensorQTL/TensorQTL.ipynb) provides the pipeline to generate TensorQTL cis association results for all QTLs. 
- [ROSMAP_gpQTL](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/cis_association/ROSMAP_gpQTL/command_generator.ipynb) provides information about the input files for adjusted/unadjusted glycoproteomics TensorQTL cis association in the base_params variable in [generate_command_1].

### Path(s) to cis-QTL association testing

**output of TensorQTL.ipynb**

- `s3://statfungen/ftp_fgc_xqtl/analysis_result/cis_association/ROSMAP/pQTL/gpQTL/`

### Path(s) to fine-mapping with SuSiE RSS model

Fine-mapping model objects (SuSiE-RSS, `.rds`) are available in the [finemapping models folder (syn69670592)](https://www.synapse.org/Synapse:syn69670592).

### Path(s) to TWAS models

Pre-trained TWAS weight models for this context: [syn69670600](https://www.synapse.org/Synapse:syn69670600)

Quantile TWAS (qTWAS) models: [syn69670611](https://www.synapse.org/Synapse:syn69670611)

### Path(s) to colocalization with SuSiE-coloc / ColocBoost

Multi-context colocalization models (ColocBoost): [syn69670597](https://www.synapse.org/Synapse:syn69670597)

AD GWAS–xQTL colocalization results: [syn69865816](https://www.synapse.org/Synapse:syn69865816)

AD GWAS–xQTL colocalization models: [syn69670630](https://www.synapse.org/Synapse:syn69670630)