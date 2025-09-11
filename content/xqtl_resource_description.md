# FunGen-xQTL Resource Description

Molecular QTL (xQTL) and GWAS resources for Alzheimer's disease risk loci and genes.

## Overview

This resource provides molecular quantitative trait loci (xQTL) and genome-wide association study (GWAS) analysis results for Alzheimer's disease risk loci and genes. Beyond traditional xQTL mapping, we employ genome-wide single-trait and multi-trait fine-mapping, trans-QTL fine-mapping, colocalization, quantile regression QTLs, interaction QTLs, and machine learning-based prediction models to identify causal variants and their molecular mechanisms. Our analyses account for linkage disequilibrium between variants and jointly model across multiple molecular contexts, providing posterior inclusion probabilities (PIP), credible sets (CS), colocalization confidence sets (CoS), effect sizes, and machine learning-based functional annotations for the molecular impact of genetic variations. We also provide comprehensive fine-mapping, colocalization, and integration analyses including TWAS and Mendelian randomization for contemporary AD GWAS studies integrated with our xQTL resources.

This resource is part of the FunGen-xQTL project within the [FunGen-AD Consortium](https://adsp-fgc.niagads.org/research/), which systematically maps genetic variants influencing molecular phenotypes across Alzheimer's disease cohorts. By integrating data from ROSMAP, Knight ADRC, Mount Sinai Brain Bank, and other collaborating studies, FunGen-xQTL provides a comprehensive molecular QTL resource for aging human brains with immediate application to AD research.

The computational protocols generating these results are available at [xQTL Protocol Documentation](https://statfungen.github.io/xqtl-protocol/README.html). Most computations were performed on AWS cloud infrastructure using [MemVerge Memory Machine Cloud](https://www.mmcloud.io/) for automated spot instance management as a cost-effective way for large-scale genomic analyses. This page provides links to variant and gene-level summaries for xQTL and AD, pretrained statistical and machine learning models for use in integrative studies for other diseases, raw xQTL data, and reference datasets.

## Variant and Gene-Level Summaries

### Molecular QTL Fine-mapping and Colocalization

Our xQTL analyses span diverse brain regions and cell types, providing fine-mapped results for [expression QTLs (eQTL)](#single_context_eqtl), [splicing QTLs (sQTL)](#single_context_sqtl), [protein QTLs (pQTL)](#single_context_pqtl), [glycosylation QTLs (glycoQTL)](#single_context_glycoqtl), [methylation QTLs (mQTL)](#single_context_mqtl), [histone acetylation QTLs (haQTL)](#single_context_haqtl), and [chromatin accessibility QTLs (caQTL)](#single_context_caqtl) from single-context fine-mapping across multiple cohorts: ROS/MAP (Rush University, Columbia and MIT), Mount Sinai Brain Bank (MSBB), Knight ADRC (WashU), MiGA and STARNET. We provide [multi-context fine-mapping](#multi_context_finemapping) that integrates signals across brain regions for ROSMAP and MSBB cohorts, and [multi-gene fine-mapping](#multi_gene_finemapping) with separate analyses for [eQTLs](#multi_gene_eqtl) and [pQTLs](#multi_gene_pqtl) that jointly model multiple genes. Additionally, trans-QTL fine-mapping identifies distant regulatory relationships for [trans-eQTLs](#trans_eqtl), [trans-pQTLs](#trans_pqtl), [trans-glycoQTLs](#trans_gpqtl) and [metabolome QTLs](#trans_metabolome).

To understand relationships between molecular traits, we conducted colocalization analyses including [multi-context colocalization](#multi_context_colocalization) using [ColocBoost](https://www.medrxiv.org/content/10.1101/2025.04.17.25326042v1) across cohorts and [pairwise colocalization](#pairwise_colocalization) using SuSiE-COLOC to specifically examining [caQTL-eQTL](#caqtl_eqtl) relationships.

### Alzheimer's Disease GWAS Integration

#### AD Loci Fine-mapping and Colocalization

We provide [fine-mapped AD GWAS results](#ad_finemapping) from major studies including Bellenguez 2022, Jansen 2021, Wightman 2021, and Kunkle 2019. These undergo systematic [AD colocalization analysis](#ad_colocalization) to identify shared genetic signals across studies. We integrate AD GWAS with xQTL data through [AD-xQTL colocalization](#ad_xqtl_colocalization) across ROSMAP, MSBB, and Knight ADRC cohorts to identify molecular mechanisms underlying genetic risk. Additionally we performed pairwise colocalization analyses include [bulk mQTL-AD](#bulk_mqtl_haqtl_ad), bulk haQTL-AD, and [single-nucleus caQTL-AD](#caqtl_ad) relationships to leverage a [new fine-mapping approach we developed](https://www.biorxiv.org/content/10.1101/2025.08.17.670732v1) for mapping epigenetic and chromatin-level mechanisms of AD risk variants.

#### Gene-Level AD Analyses

Our gene-level analyses include [transcriptome-wide association studies (TWAS) and Mendelian randomization (MR)](#twas_mr) identifying genes whose regulated expression associates with AD risk. We complement this with [causal TWAS (cTWAS)](#ctwas) that accounts for gene expression correlation and LD structure, addressing LD-hitchhiking issues where non-causal genes appear significant due to correlation with true causal genes.

#### **Integrated AD Summary Tables**

For immediate use by researchers, we provide comprehensive summary tables:
- [AD loci annotated by xQTL summary table](#ad_loci_xqtl_table) - variant-level integration of AD GWAS loci with all xQTL evidence
- [AD genes with FunGen and xQTL annotations](#ad_genes_fungen_xqtl) - AD risk genes prioritization through fine-mapping and colocalization
- [AD genes with TWAS integration](#ad_genes_twas_xqtl) - AD risk genes prioritization that additionally incorporates TWAS and MR

## Predictive Models and Scores

### Single-Cell Expression Prediction

We provide [SCEEM (Single-Cell Expression Expectation Maximization) scores](#xqtl_sceem_scores) for predicting cell-type-specific eQTL effects in single-nucleus RNA-seq data. 

### Variant-to-Function Prediction

The [cv2F (causal variant to function) scores](#cv2f_scores) integrate xQTL data with functional annotations to predict AD risk at the variant level. [A machine learning framework](https://www.biorxiv.org/content/10.1101/2024.11.07.622307v2) is applied to combine multiple lines of molecular evidence, particularly our xQTL resource, to prioritize likely causal variants for GWAS.

## Pretrained Statistical Models

### QTL and GWAS Statistical Models

We provide complete statistical models as RDS files for researchers to conduct custom analyses or integrate with other complex traits and diseases. Fine-mapping models are available for [eQTL](#finemapping_models_eqtl), [pQTL](#finemapping_models_pqtl), [glycoQTL](#finemapping_models_glycoqtl), and [sQTL](#finemapping_models_sqtl). [Colocalization models](#colocalization_models) preserve the probabilistic framework for identifying shared genetic signals, allowing exploration of alternative colocalization thresholds and model assessment. TWAS models are provided for [eQTL](#twas_models_eqtl), [pQTL](#twas_models_pqtl), [glycoQTL](#twas_models_glycoqtl), and [sQTL](#twas_models_sqtl), along with qTWAS models for [eQTL](#qtwas_models_eqtl), [pQTL](#qtwas_models_pqtl), [glycoQTL](#qtwas_models_glycoqtl), and [sQTL](#qtwas_models_sqtl) that incorporate non-linear QTL effects.

### Alzheimer's Disease Analysis Models

AD-specific models include [AD fine-mapping results](#ad_fine_mapping_models) with Bayes factors, posterior probabilities and credible sets, and [AD colocalization models](#ad_colocalization_models) providing detailed statistical evidence of shared genetic architecture per locus. [AD-xQTL colocalization models](#ad_xqtl_colocalization_models) offer comprehensive colocalization statistics between AD risk and molecular traits. We also provide [cTWAS input files](#ad_ctwas_input) formatted for causal transcriptome-wide association studies in AD.

## Raw QTL Summary Statistics

### Linear Regression and Mixed Model Results

We provide [R-based linear model residuals](#r_lm_residual_sumstats) and tensorQTL outputs in two forms: [raw results for all variants](#tensorqtl_sumstats_raw) and [significant results after multiple testing correction](#tensorqtl_sumstats_significant) containing standard additive genetic effects. For splicing analysis, [generalized linear mixed model sQTL results](#xqtl_glmm) account for the count-based nature of splice junction data while controlling for related observations using meta-cell approaches in single-cell data.

### Non-linear Genetic Effects

[Quantile regression QTL results](#xqtl_qr) identify variants affecting expression variance and outliers, revealing heterogeneous genetic effects relevant to disease states. [QTL interaction analyses](#xqtl_interaction) test for genotype-by-sex, APOE4 genotype, and cell proportion interactions to capture context-dependent genetic effects.

## Reference Data and Resources

### Population-Specific LD References

We provide [ADSP-based LD reference data for European ancestry](#adsp_ld_reference_eur) populations, formatted in plink bim format with xz compression. These panels derive from the Alzheimer's Disease Sequencing Project Release 4, providing improved coverage of low-frequency variants. With larger sample sizes than 1000 Genomes reference panels, they demonstrate superior performance for fine-mapping in GWAS meta-analysis for AD and beyond.

### Functional Annotation Resources

Our LDSC reference data, computed from ADSP LD references rather than default 1000 Genomes panels, includes [LD scores](#ldsc_ld_scores) optimized for AD heritability estimation, [stratified LDSC annotations](#ldsc_sldsc_annotations) for functional enrichment across brain-specific elements, and [pre-processed GWAS summary statistics](#ldsc_gwas_munged). Additionally, [functional enrichment annotations](#functional_enrichment_annotations) in UCSC bed format encompass regulatory elements, cell-type-specific markers, and brain-specific annotations relevant to neurodegeneration.

### Protocols and Tutorials

Comprehensive [xQTL analysis protocols and tutorials](#xqtl_protocol_tutorial) provide instructions with example datasets, guiding users through QTL mapping, fine-mapping, colocalization, and integrative analyses.

## Data Format and Column Descriptions

All exported bed files follow standardized formats with consistent column definitions. See our [file and format description page](xqtl_resource_format) for detailed specifications.

## Citation and Usage

Please cite appropriate manuscripts and acknowledge consortium data generation efforts. Detailed citation information will be provided upon publication.

[ad_loci_xqtl_table]: 
[ad_genes_fungen_xqtl]:
[ad_genes_twas_xqtl]: 