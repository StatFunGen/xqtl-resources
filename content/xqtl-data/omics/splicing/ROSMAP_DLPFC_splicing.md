# ROSMAP DLPFC alternative splicing

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) DLPFC alternative splicing. 

Please refer to [this document](../../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Contact 

Xuanhe Chen; Shrishtee Kandoi

- Contact Email : xuanhechenxhc@163.com;
- Contact Affiliation : Columbia University; Boston University
- Contact Role : Xuanhe Chen performed sQTL analysis via psichomics package, and SuSiE uni-variate fine-mapping analysis using psichomics sQTL data, Shrishtee Kandoi performed sQTL analysis via leafCutter package.


## Study Overview

- PI : David A. Bennett (Rush University Medical Center, Chicago, IL, USA)
- Grant number : U01AG046152, R01AG048015, U01AG061356, R01AG15819, U01AG061359
- Publication : PMID: 30084846
- Genetics Publication : PMID: 40407102
- Acknowledgement : Study data were generated from postmortem brain tissue provided by the Religious Orders Study and Rush Memory and Aging Project (ROSMAP) cohort at Rush Alzheimer’s Disease Center, Rush University Medical Center, Chicago.
- Study name : splicing phenotype processing using ROSMAP DLPFC RNAseq Bulk Brain
- Study Description : From STAR alignment output of ROSMAP DLPFC RNAseq Bulk Brain data (sample size 1141), we used leafCutter package to find intron usage ratio data for intron clusters and psichomics package to find percent spliced in (PSI) values for different alternative splicing events. All phenotype processing was done using the ADSP FGC xQTL pipeline and the output format is prepared for sQTL analysis.
- Disease : Alzheimer’s Disease
- Data Citation : Omics data: [syn3388564](https://www.synapse.org/Synapse:syn3388564); Genetics data: [ng00067](https://dss.niagads.org/datasets/ng00067/)
- Additional study information : 

## Dataset Details

### Raw data

Samples were extracted using Qiagen's miRNeasy mini kit (cat. no. 217004) and the RNase free DNase Set (cat. no. 79254), and quantified by Nanodrop and quality was evaluated by Agilent Bioanalyzer.

ROSMAP DLPFC Gene Expression (RNA seq - bulk brain): 

- https://www.synapse.org/#!Synapse:syn3388564

| Brain   | Description                                            |
| ------- | ------------------------------------------------------ |
| Batch 1 | 638                                                    |
| Batch 2 | 252 (117 for PolyA selection & 135 for rRNA depletion) |
| Batch 3 | 251                                                    |
| Total   | 1141                                                   |

**NOTE: These data was once downloaded to BU cluster for QTL analysis phenotype preprocessing and then deleted to release storage.**

### Molecular phenotype matrices

Data Processing:

The raw data were aligned using the STAR-WASP pipeline, which utilizes the reference file available at ftp: `/ftp_fgc_xqtl/ref-data/ROSMAP_rnaseq/ref/GRCh38_full_analysis_set_plus_decoy_hla.noALT_noHLA_noDecoy_ERCC.fasta.chrom.size` and `/ftp_fgc_xqtl/ref-data/ROSMAP_rnaseq/ref/ZOD14598_AD_GRM_WGS_2021-04-29_all.recalibrated_variants.leftnorm.filtered.AF.WASP.vcf.gz` The alignment results was processed via ADSP FGC xQTL pipeline, splicing QTL module, using two packages, leafCutter and psichomics. Within the 1141 samples, 95310 intron clusters were found by leafCutter and 176917 different alternative splicing event were found by psichomics.

For leafCutter, the recipe of chromosome seperated phenotype matrices can be found at BU cluster: `/restricted/projectnb/casa/skandoi/ROSMAP_DLPFC/PDP_leafcutter/leafcutter_bam_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.processed_phenotype.per_chrom.recipe`. The recipe and matrices can be found on FTP server: `/ftp_fgc_xqtl/projects/rna-seq/BU/ROSMAP_DLPFC/sQTL/phenotype_preprocessing/`

The phenotype matrices are processed bed format files, with chr, start, end, ID and sample IDs as column names, each row represents one intron cluster and the values are intron usage ratio (for details please check [leafCutter publication](https://www.nature.com/articles/s41588-017-0004-9) ). The ID of leafcutter phenotype will be like [chromosome]:[intron_start]:[intron_end]:clu_[cluster No.]_[strandness]:[gene mapped for this intron cluster], for example: chr14:19062466:19064583:clu_26162_+:ENSG00000225210

For psichomics, the recipe of chromosome seperated phenotype matrices can be found at CU cluster: `/mnt/mfs/hgrcgrid/homes/xc2610/psichomics_rerun2/pheno/ROSMAP_psichomics_bed_recipe.txt`.

The phenotype matrices are processed bed format files, with chr, start, end, ID and sample IDs as column names, each row represents one alternative splicing event and the values are percent spliced in value (for details please check [psichomics publication](https://www.biorxiv.org/content/10.1101/261180v2.full) ). The ID of psichomics phenotype will be like [Alternative splicing event type]_[chromosome]_[strandness]_[splicing locations depend on event type]_[gene mapped for this splicing event], for example: SE_10_+_135559_179994_180128_209889_ENSG00000015171

## Links to omics data analysis notebooks

### splicing phenotype pre-processing

The splicing related phenotype data were generated via the following workflow: [splicing_phenotype_preprocessing](https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/ROSMAP_DLPFC/sQTL/phenotype_preprocessing_sQTL.ipynb)

### Exploratory analysis

1. [Data_Information.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Zhang_BU/ROSMAP_DLPFC/Data_Information.ipynb) provides data description and sample overlap checking between ROSMAP DLPFC RNAseq Bulk Brain and ROSMAP WGS.

## QTL Analysis
QTL analysis for this dataset is documented in [../../qtl/sQTL/ROSMAP_DLPFC_splicing_qtl.md](../../qtl/sQTL/ROSMAP_DLPFC_splicing_qtl.md).

Flagship paper analyses:
- Fine-mapping (SuSiE-RSS): [syn69670592](https://www.synapse.org/Synapse:syn69670592)
- TWAS weight models: [syn69670600](https://www.synapse.org/Synapse:syn69670600)
- Quantile TWAS (qTWAS) models: [syn69670611](https://www.synapse.org/Synapse:syn69670611)
- Multi-context colocalization (ColocBoost): [syn69670597](https://www.synapse.org/Synapse:syn69670597)
- AD GWAS–xQTL colocalization results: [syn69865816](https://www.synapse.org/Synapse:syn69865816)
- AD GWAS–xQTL colocalization models: [syn69670630](https://www.synapse.org/Synapse:syn69670630)
