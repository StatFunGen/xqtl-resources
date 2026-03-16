# MSBB brain alternative splicing QTL

## Contact

Minghui Wang

## Links to QTL analysis notebooks

See notebooks in: 

- https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/MSBB/sQTL

The notebooks in this folder contain the commands and data wrangling codes for analysis of the expression data in MSBB. (data wrangling exist because not all data are processed using the xqtl-pipeline from the beginning and need to be reformatted to fit one intermediate step of the pipeline).

### Association data preprocessing
#### Genotype data preprocessing

#### Principal component analysis for eQTL mapping

#### Phenotype data preprocessing

#### Covariate data preprocessing
  
### Association scan using TensorQTL and summary statistics standardization




### Path(s) to cis-QTL association testing

**output of TensorQTL.ipynb**

- `s3://statfungen/ftp_fgc_xqtl/analysis_result/cis_association/MSBB/sQTL/`

### Path(s) to fine-mapping with SuSiE RSS model

Fine-mapping model objects (SuSiE-RSS, `.rds`) are available in the [finemapping models folder (syn69670592)](https://www.synapse.org/Synapse:syn69670592).

### Path(s) to TWAS models

Pre-trained TWAS weight models for this context: [syn69670600](https://www.synapse.org/Synapse:syn69670600)

Quantile TWAS (qTWAS) models: [syn69670611](https://www.synapse.org/Synapse:syn69670611)

### Path(s) to colocalization with SuSiE-coloc / ColocBoost

Multi-context colocalization models (ColocBoost): [syn69670597](https://www.synapse.org/Synapse:syn69670597)

AD GWAS–xQTL colocalization results: [syn69865816](https://www.synapse.org/Synapse:syn69865816)

AD GWAS–xQTL colocalization models: [syn69670630](https://www.synapse.org/Synapse:syn69670630)
