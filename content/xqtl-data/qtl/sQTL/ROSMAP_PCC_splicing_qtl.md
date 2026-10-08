# ROSMAP PCC alternative splicing QTL

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) PCC alternative splicing. 

Please refer to [this document](../../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Contact 

Frank Grenn

## Study Overview

**In progress**

- Sample information: `####/####_sample_attributes.csv`.
- Lab protocol: `####/####_lab_protocol.csv`.
- Computational protocol: `####/####_computational_protocol.csv`.
- QTL summary statistics output: `####/####.qtl_results.csv`.
- Fine-mapping results individual level data model: `####/####.susie.csv`.
- Fine-mapping results summary statistics model: `####/####.susie_rss.csv`.
- Colocalization with AD GWAS: `####/####.susie_coloc.csv`.

## Analysis Status

TransQTL association: Need to be performed.

## Dataset Details

### Path(s) to genotype matrix




### Path(s) to omics-data matrix


```
$ ls -lh batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.txt
-rw-r--r-- 1 fgrennjr casa 3.1G Mar  6 14:06 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.txt
```

### Path(s) to covariate data matrix


### Path(s) to QTL results

```
$ ls -lh | head
total 27G
-rw-r--r-- 1 fgrennjr casa 374M Mar 24 11:42 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.per_chrom_leafcutter.pcc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.1.cis_qtl_pairs.1.parquet
-rw-r--r-- 1 fgrennjr casa  285 Mar 24 22:12 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.per_chrom_leafcutter.pcc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.1.cis_qtl_pairs.1.parquet.stderr
-rw-r--r-- 1 fgrennjr casa 138K Mar 24 22:12 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.per_chrom_leafcutter.pcc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.1.cis_qtl_pairs.1.parquet.stdout
-rw-r--r-- 1 fgrennjr casa 433K Mar 24 22:12 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.per_chrom_leafcutter.pcc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.1.emprical.cis_sumstats.txt
-rw-r--r-- 1 fgrennjr casa 2.2G Mar 24 11:44 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.per_chrom_leafcutter.pcc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.1.norminal.cis_long_table.txt
-rw-r--r-- 1 fgrennjr casa 180M Mar 24 11:28 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.per_chrom_leafcutter.pcc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.10.cis_qtl_pairs.10.parquet
-rw-r--r-- 1 fgrennjr casa  285 Mar 24 16:48 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.per_chrom_leafcutter.pcc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.10.cis_qtl_pairs.10.parquet.stderr
-rw-r--r-- 1 fgrennjr casa  58K Mar 24 16:48 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.per_chrom_leafcutter.pcc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.10.cis_qtl_pairs.10.parquet.stdout
-rw-r--r-- 1 fgrennjr casa 187K Mar 24 16:48 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.per_chrom_leafcutter.pcc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.10.emprical.cis_sumstats.txt
```


## Links to QTL analysis notebooks for LeafCutter2

See notebooks in: 

- https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/sQTL/PCC

The notebooks in this folder contain the commands and data wrangling codes for analysis of the eQTL and sQTL data in ROSMAP. (data wrangling exist because not all data are processed using the xqtl-pipeline from the beginning and need to be reformatted to fit one intermediate step of the pipeline). Since the sQTL phenotype pre-processing used eQTL STAR alignment output, some of the early stage code are shared.

### Association data preprocessing

- [LeafCutter2_QC](https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/sQTL/PCC/1.2_pcc_leafcutter2_results_QC.ipynb) shows the commands used for quality control of the LeafCutter2 results.

- [genotype_preprocessing.ipynb](https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/haQTL/genotype_preprocessing.ipynb) shows the commands used for genotype processing and preparation steps.all QTLs in one cohort have the same genotype_preprocessing procedure.

- [phenotype_preprocessing.ipynb](https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/sQTL/PCC/1_pcc_phenotype_preprocessing.ipynb) shows the commands used for the phenotype data processing and preparation steps.

- [covariate_preprocessing.ipynb](https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/sQTL/PCC/3_pcc_covariate_preprocessing.ipynb) shows the commands used for the covariate data processing and preparation steps.

  
### Association scan using TensorQTL and summary statistics standardization

- [TensorQTL.ipynb](https://github.com/cumc/xqtl-protocol/blob/main/code/association_scan/TensorQTL/TensorQTL.ipynb) provides the pipeline to generate TensorQTL cis association results for all QTLs. 
- [ROSMAP_sQTL_LeafCutter2_commands](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/cis_association/ROSMAP_sQTL_LeafCutter2/command_generator.ipynb) provides information about the input files for AC/DLPFC/PCC TensorQTL cis association in the base_params variable in [generate_command_1].

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