---
type: qtl
modality: eQTL
short_title: ROSMAP PCC
cohort: ROSMAP
context: PCC
sample_size:
access: controlled
status: staged
release:
synapse_ids: [syn69670592, syn69670600, syn69670611, syn69670597, syn69865816, syn69670630]
lead_analysts: [Frank Grenn]
last_verified:
---

# ROSMAP PCC Expression QTL

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










### Path(s) to QTL results


```
$ ls -lh | head
total 35G
-rw-r--r-- 1 fgrennjr casa  529M Mar 17 16:02 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.per_chrom_pcc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.1.cis_qtl_pairs.1.parquet
-rw-r--r-- 1 fgrennjr casa   285 Mar 17 17:06 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.per_chrom_pcc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.1.cis_qtl_pairs.1.parquet.stderr
-rw-r--r-- 1 fgrennjr casa  173K Mar 17 17:06 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.per_chrom_pcc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.1.cis_qtl_pairs.1.parquet.stdout
-rw-r--r-- 1 fgrennjr casa  555K Mar 17 17:06 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.per_chrom_pcc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.1.emprical.cis_sumstats.txt
-rw-r--r-- 1 fgrennjr casa  2.6G Mar 17 16:04 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.per_chrom_pcc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.1.norminal.cis_long_table.txt
-rw-r--r-- 1 fgrennjr casa  253M Mar 17 16:00 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.per_chrom_pcc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.10.cis_qtl_pairs.10.parquet
-rw-r--r-- 1 fgrennjr casa   285 Mar 17 16:31 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.per_chrom_pcc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.10.cis_qtl_pairs.10.parquet.stderr
-rw-r--r-- 1 fgrennjr casa   72K Mar 17 16:31 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.per_chrom_pcc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.10.cis_qtl_pairs.10.parquet.stdout
-rw-r--r-- 1 fgrennjr casa  234K Mar 17 16:31 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.per_chrom_pcc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.10.emprical.cis_sumstats.txt
```

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

Analysis notebook generation in progress and will be uploaded to [https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Zhang_BU/PCC_AC](https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Zhang_BU/PCC_AC). Steps will be similar to what is found in [https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Zhang_BU/ROSMAP_DLPFC](https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Zhang_BU/ROSMAP_DLPFC).

Wang lab: 
- [TensorQTL.ipynb](https://github.com/cumc/xqtl-protocol/blob/main/code/association_scan/TensorQTL/TensorQTL.ipynb) provides the pipeline to generate TensorQTL cis association results for all QTLs. 
- [ROSMAP_DeJager_bulk_eQTL](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/cis_association/ROSMAP_DeJager_bulk_eQTL/command_generator.ipynb)provides information about the input files for AC/DLPFC/PCC TensorQTL cis association in the base_params variable in [generate_command_1].