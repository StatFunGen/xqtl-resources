# FunGen-xQTL Resource Description

Molecular QTL (xQTL) and GWAS resources for Alzheimer's disease risk loci and genes.

## Overview

This resource provides molecular quantitative trait loci (xQTL) and genome-wide association study (GWAS) analysis results for Alzheimer's disease risk loci and genes. Beyond traditional xQTL mapping, we employ genome-wide single-trait and multi-trait fine-mapping, trans-QTL fine-mapping, colocalization, quantile regression QTLs, interaction QTLs, and machine learning-based prediction models to identify causal variants and their molecular mechanisms. Our analyses account for linkage disequilibrium between variants and jointly model across multiple molecular contexts, providing posterior inclusion probabilities (PIP), credible sets (CS), colocalization confidence sets (CoS), effect sizes, and machine learning-based functional annotations for the molecular impact of genetic variations. We also provide comprehensive fine-mapping, colocalization, and integration analyses including TWAS and Mendelian randomization for contemporary AD GWAS studies integrated with our xQTL resources.

This resource is part of the FunGen-xQTL project within the [FunGen-AD Consortium](https://adsp-fgc.niagads.org/research/), which systematically maps genetic variants influencing molecular phenotypes across Alzheimer's disease cohorts. By integrating data from ROSMAP, Knight ADRC, Mount Sinai Brain Bank, and other collaborating studies, FunGen-xQTL provides a comprehensive molecular QTL resource for aging human brains with immediate application to AD research. All data are hosted on Synapse: [variant & gene summaries](https://www.synapse.org/Synapse:syn69865684) ([syn69865684](https://www.synapse.org/Synapse:syn69865684)), [xQTL models](https://www.synapse.org/Synapse:syn69670588) ([syn69670588](https://www.synapse.org/Synapse:syn69670588)), [raw QTL data](https://www.synapse.org/Synapse:syn69670632) ([syn69670632](https://www.synapse.org/Synapse:syn69670632)), [reference files](https://www.synapse.org/Synapse:syn69670634) ([syn69670634](https://www.synapse.org/Synapse:syn69670634)).

The computational protocols generating these results are available at [xQTL Protocol Documentation](https://statfungen.github.io/xqtl-protocol/README.html). Most computations were performed on AWS cloud infrastructure using [MemVerge Memory Machine Cloud](https://www.mmcloud.io/) for automated spot instance management as a cost-effective way for large-scale genomic analyses. This page provides links to variant and gene-level summaries for xQTL and AD, pretrained statistical and machine learning models for use in integrative studies for other diseases, raw xQTL data, and reference datasets.

## Variant and Gene-Level Summaries

### Molecular QTL Fine-mapping and Colocalization

Our xQTL analyses span diverse brain regions and cell types across multiple cohorts, providing fine-mapped results for the following modalities:

- **[Expression QTLs (eQTL)](xqtl-data/qtl/eQTL):** [ROSMAP DLPFC](xqtl-data/qtl/eQTL/ROSMAP_DLPFC_expression_qtl), [ROSMAP PCC](xqtl-data/qtl/eQTL/ROSMAP_PCC_expression_qtl), [ROSMAP AC](xqtl-data/qtl/eQTL/ROSMAP_AC_expression_qtl), [ROSMAP microglia](xqtl-data/qtl/eQTL/ROSMAP_microglia_expression_qtl), [ROSMAP monocyte](xqtl-data/qtl/eQTL/ROSMAP_monocyte_expression_qtl), [ROSMAP snRNA-seq pseudo-bulk](xqtl-data/qtl/eQTL/ROSMAP_snRNAseq_pseudo_bulk_qtl), [MSBB](xqtl-data/qtl/eQTL/MSBB_brain_expression_qtl), [MiGA](xqtl-data/qtl/eQTL/MiGA_brain_expression_qtl), [MetaBrain](xqtl-data/qtl/eQTL/MetaBrain_brain_expression_qtl), [Knight ADRC](xqtl-data/qtl/eQTL/Knight_ADRC_brain_expression_qtl), [STARNET](xqtl-data/qtl/eQTL/STARNET_macrophage_qtl)

- **[Splicing QTLs (sQTL)](xqtl-data/qtl/sQTL):** [ROSMAP DLPFC](xqtl-data/qtl/sQTL/ROSMAP_DLPFC_splicing_qtl), [ROSMAP PCC](xqtl-data/qtl/sQTL/ROSMAP_PCC_splicing_qtl), [ROSMAP AC](xqtl-data/qtl/sQTL/ROSMAP_AC_splicing_qtl), [ROSMAP snuc](xqtl-data/qtl/sQTL/ROSMAP_snuc_splicing_qtl), [MSBB](xqtl-data/qtl/sQTL/MSBB_brain_splicing_qtl), [Knight ADRC](xqtl-data/qtl/sQTL/Knight_ADRC_brain_splicing_qtl)

- **[Protein QTLs (pQTL)](xqtl-data/qtl/pQTL):** [ROSMAP DLPFC](xqtl-data/qtl/pQTL/ROSMAP_DLPFC_proteomics_qtl), [MSBB](xqtl-data/qtl/pQTL/MSBB_proteomics_qtl), [Knight ADRC brain](xqtl-data/qtl/pQTL/Knight_ADRC_brain_proteomics_qtl)

- **[Glycosylation QTLs (gpQTL)](xqtl-data/qtl/gpQTL):** [ROSMAP DLPFC](xqtl-data/qtl/gpQTL/ROSMAP_DLPFC_glycoproteomics_qtl)

- **[Methylation QTLs (mQTL)](xqtl-data/qtl/mQTL):** [ROSMAP DLPFC](xqtl-data/qtl/mQTL/ROSMAP_DLPFC_methylation_qtl), [MSBB](xqtl-data/qtl/mQTL/MSBB_brain_methylation_qtl), [Knight ADRC](xqtl-data/qtl/mQTL/Knight_ADRC_brain_methylation_qtl)

- **[Histone acetylation QTLs (haQTL)](xqtl-data/qtl/haQTL):** [ROSMAP DLPFC](xqtl-data/qtl/haQTL/ROSMAP_DLPFC_ChIPSeq_H3K9ac_qtl)

- **[Chromatin accessibility QTLs (caQTL)](xqtl-data/qtl/caQTL):** [ROSMAP snuc](xqtl-data/qtl/caQTL/ROSMAP_snuc_caQTL_qtl)

- **[Metabolome QTLs (metQTL)](xqtl-data/qtl/metQTL):** [ROSMAP DLPFC](xqtl-data/qtl/metQTL/ROSMAP_DLPFC_metabolomics_qtl), [Knight ADRC brain](xqtl-data/qtl/metQTL/Knight_ADRC_brain_metabolomics_qtl)

We provide [multi-context fine-mapping](https://www.synapse.org/Synapse:syn69865754) that integrates signals across brain regions for ROSMAP and MSBB cohorts, and [multi-gene fine-mapping](https://www.synapse.org/Synapse:syn69865757) with separate analyses for eQTLs and pQTLs that jointly model multiple genes. Additionally, [trans-QTL fine-mapping](https://www.synapse.org/Synapse:syn69865773) identifies distant regulatory relationships for trans-eQTLs ([ROSMAP DLPFC](xqtl-data/qtl/eQTL/ROSMAP_DLPFC_expression_qtl)), trans-pQTLs ([ROSMAP DLPFC](xqtl-data/qtl/pQTL/ROSMAP_DLPFC_proteomics_qtl)), trans-gpQTLs ([ROSMAP DLPFC](xqtl-data/qtl/gpQTL/ROSMAP_DLPFC_glycoproteomics_qtl)), and metabolome QTLs ([ROSMAP DLPFC](xqtl-data/qtl/metQTL/ROSMAP_DLPFC_metabolomics_qtl)). Transcriptomic pattern QTLs (tpQTL), derived from ROSMAP splicing factor analyses, are included in the fine-mapping, colocalization and TWAS resources.

To understand relationships between molecular traits, we conducted colocalization analyses including [multi-context colocalization](https://www.synapse.org/Synapse:syn69865796) using [ColocBoost](https://www.medrxiv.org/content/10.1101/2025.04.17.25326042v1) across cohorts ([syn69865796](https://www.synapse.org/Synapse:syn69865796); models: [syn69670597](https://www.synapse.org/Synapse:syn69670597)) and [pairwise colocalization](https://www.synapse.org/Synapse:syn69865800) using SuSiE-COLOC to specifically examine [caQTL-eQTL](https://www.synapse.org/Synapse:syn69865800) relationships. ColocBoost colocalization among ROSMAP trans-xQTL (transmap) signals is provided separately as [trans colocalization](https://www.synapse.org/Synapse:syn77579916) ([syn77579916](https://www.synapse.org/Synapse:syn77579916)).

### Alzheimer's Disease GWAS Integration

#### AD Loci Fine-mapping and Colocalization

We provide [fine-mapped AD GWAS results](xqtl-data/gwas/AD_GWAS) from major studies including Bellenguez 2022, Jansen 2019, Wightman 2021, and Kunkle 2019 ([syn69670625](https://www.synapse.org/Synapse:syn69670625)); the 2026 update adds the Bellenguez main, no-biobank and no-proxy analyses, with per-study top loci in [syn69865805](https://www.synapse.org/Synapse:syn69865805). These undergo systematic [AD colocalization analysis](xqtl-data/gwas/AD_GWAS) to identify shared genetic signals across studies ([syn69865814](https://www.synapse.org/Synapse:syn69865814)). We integrate AD GWAS with xQTL data through [AD-xQTL colocalization](xqtl-data/gwas/AD_GWAS) across ROSMAP, MSBB, Knight ADRC and MiGA cohorts, including ROSMAP trans-xQTL (transmap) and tpQTL colocalization, to identify molecular mechanisms underlying genetic risk ([syn69865816](https://www.synapse.org/Synapse:syn69865816), [syn69670630](https://www.synapse.org/Synapse:syn69670630)). Additionally, we performed pairwise colocalization analyses include [bulk mQTL-AD](https://www.synapse.org/Synapse:syn69865816), bulk haQTL-AD, and [single-nucleus caQTL-AD](https://www.synapse.org/Synapse:syn69865816) relationships to leverage a [new fine-mapping approach we developed](https://www.biorxiv.org/content/10.1101/2025.08.17.670732v1) for mapping epigenetic and chromatin-level mechanisms of AD risk variants.

#### Gene-Level AD Analyses

Our gene-level analyses include [transcriptome-wide association studies (TWAS) and Mendelian randomization (MR)](https://www.synapse.org/Synapse:syn69670600) identifying genes whose regulated expression associates with AD risk (exported results: [syn69865821](https://www.synapse.org/Synapse:syn69865821); per-context association results: [syn74908416](https://www.synapse.org/Synapse:syn74908416)), using pre-trained TWAS weight models ([syn69670600](https://www.synapse.org/Synapse:syn69670600)) and quantile TWAS (qTWAS) models ([syn69670611](https://www.synapse.org/Synapse:syn69670611)). We complement this with [causal TWAS (cTWAS)](https://www.synapse.org/Synapse:syn74908389) ([syn74908389](https://www.synapse.org/Synapse:syn74908389); exported results: [syn69865822](https://www.synapse.org/Synapse:syn69865822)) that accounts for gene expression correlation and LD structure, addressing LD-hitchhiking issues where non-causal genes appear significant due to correlation with true causal genes.

#### **Integrated AD Summary Tables**

For immediate use by researchers, we provide comprehensive summary tables in the [AD × xQTL integration summary folder](https://www.synapse.org/Synapse:syn69865823) ([syn69865823](https://www.synapse.org/Synapse:syn69865823)). The current release (October 2026) covers 195 AD loci:
- **AD loci annotated by xQTL summary workbook** (`unified_AD_loci_xQTL_summary_20261002.xlsx`) - variant-level integration of AD GWAS loci with all xQTL evidence
- **Unified AD loci** (`AD_loci_unified_cs95orColocs.csv`) and the **variant-level table** (`AD_loci_unified_cs95orColocs_Pval1e5_variant_level.csv`)
- **xQTL overlap table** (`xQTL_all_methods_overlap_with_AD_loci_unified_cs95orColocs_Pval1e5.csv.gz`) - every xQTL method and context overlapping each AD locus
- [AD genes with FunGen and xQTL annotations](https://www.synapse.org/Synapse:syn70095142) - AD risk gene prioritization through fine-mapping and colocalization (March 2025)
- [AD genes with TWAS integration](https://www.synapse.org/Synapse:syn70095143) - AD risk gene prioritization that additionally incorporates TWAS and MR (March 2025)

The same release can be browsed interactively in the [xQTL-AD-loci-explorer](https://wanggroup.org/xQTL-AD-loci-explorer/).

## Predictive Models and Scores

### Single-Cell Expression Prediction

We provide [SCEEM (Single-Cell Expression Expectation Maximization) scores](xqtl-data/qtl/eQTL/ROSMAP_snRNAseq_pseudo_bulk_qtl) for predicting cell-type-specific eQTL effects in single-nucleus RNA-seq data, with trained models and predictions for six major brain cell types ([syn69670587](https://www.synapse.org/Synapse:syn69670587)). 

### Variant-to-Function Prediction

The [cv2F (causal variant to function) scores](https://www.biorxiv.org/content/10.1101/2024.11.07.622307v2) integrate xQTL data with functional annotations to predict AD risk at the variant level. [A machine learning framework](https://www.biorxiv.org/content/10.1101/2024.11.07.622307v2) is applied to combine multiple lines of molecular evidence, particularly our xQTL resource, to prioritize likely causal variants for GWAS.

## Pretrained Statistical Models

### QTL and GWAS Statistical Models

We provide complete statistical models as RDS files for researchers to conduct custom analyses or integrate with other complex traits and diseases. Fine-mapping models ([syn69670592](https://www.synapse.org/Synapse:syn69670592)) are available for:

- **eQTL:** [ROSMAP DLPFC](xqtl-data/qtl/eQTL/ROSMAP_DLPFC_expression_qtl), [ROSMAP PCC](xqtl-data/qtl/eQTL/ROSMAP_PCC_expression_qtl), [ROSMAP AC](xqtl-data/qtl/eQTL/ROSMAP_AC_expression_qtl), [ROSMAP microglia](xqtl-data/qtl/eQTL/ROSMAP_microglia_expression_qtl), [ROSMAP monocyte](xqtl-data/qtl/eQTL/ROSMAP_monocyte_expression_qtl), [MSBB](xqtl-data/qtl/eQTL/MSBB_brain_expression_qtl), [Knight ADRC](xqtl-data/qtl/eQTL/Knight_ADRC_brain_expression_qtl), [MiGA](xqtl-data/qtl/eQTL/MiGA_brain_expression_qtl), [MetaBrain](xqtl-data/qtl/eQTL/MetaBrain_brain_expression_qtl)
- **sQTL:** [ROSMAP DLPFC](xqtl-data/qtl/sQTL/ROSMAP_DLPFC_splicing_qtl), [ROSMAP PCC](xqtl-data/qtl/sQTL/ROSMAP_PCC_splicing_qtl), [ROSMAP AC](xqtl-data/qtl/sQTL/ROSMAP_AC_splicing_qtl), [ROSMAP snuc](xqtl-data/qtl/sQTL/ROSMAP_snuc_splicing_qtl), [MSBB](xqtl-data/qtl/sQTL/MSBB_brain_splicing_qtl), [Knight ADRC](xqtl-data/qtl/sQTL/Knight_ADRC_brain_splicing_qtl)
- **pQTL:** [ROSMAP DLPFC](xqtl-data/qtl/pQTL/ROSMAP_DLPFC_proteomics_qtl), [MSBB](xqtl-data/qtl/pQTL/MSBB_proteomics_qtl), [Knight ADRC brain](xqtl-data/qtl/pQTL/Knight_ADRC_brain_proteomics_qtl)
- **gpQTL:** [ROSMAP DLPFC](xqtl-data/qtl/gpQTL/ROSMAP_DLPFC_glycoproteomics_qtl)
- **mQTL:** [ROSMAP DLPFC](xqtl-data/qtl/mQTL/ROSMAP_DLPFC_methylation_qtl), [MSBB](xqtl-data/qtl/mQTL/MSBB_brain_methylation_qtl), [Knight ADRC](xqtl-data/qtl/mQTL/Knight_ADRC_brain_methylation_qtl)
- **haQTL:** [ROSMAP DLPFC](xqtl-data/qtl/haQTL/ROSMAP_DLPFC_ChIPSeq_H3K9ac_qtl)
- **caQTL:** [ROSMAP snuc](xqtl-data/qtl/caQTL/ROSMAP_snuc_caQTL_qtl)

[Colocalization models](https://www.synapse.org/Synapse:syn69670597) preserve the probabilistic framework for identifying shared genetic signals, allowing exploration of alternative colocalization thresholds and model assessment ([syn69670597](https://www.synapse.org/Synapse:syn69670597)). TWAS weight models ([syn69670600](https://www.synapse.org/Synapse:syn69670600)) and qTWAS models ([syn69670611](https://www.synapse.org/Synapse:syn69670611)) are provided for eQTL ([ROSMAP DLPFC](xqtl-data/qtl/eQTL/ROSMAP_DLPFC_expression_qtl), [ROSMAP PCC](xqtl-data/qtl/eQTL/ROSMAP_PCC_expression_qtl), [ROSMAP AC](xqtl-data/qtl/eQTL/ROSMAP_AC_expression_qtl), [MSBB](xqtl-data/qtl/eQTL/MSBB_brain_expression_qtl), [Knight ADRC](xqtl-data/qtl/eQTL/Knight_ADRC_brain_expression_qtl)), pQTL ([ROSMAP DLPFC](xqtl-data/qtl/pQTL/ROSMAP_DLPFC_proteomics_qtl), [MSBB](xqtl-data/qtl/pQTL/MSBB_proteomics_qtl), [Knight ADRC](xqtl-data/qtl/pQTL/Knight_ADRC_brain_proteomics_qtl)), gpQTL ([ROSMAP DLPFC](xqtl-data/qtl/gpQTL/ROSMAP_DLPFC_glycoproteomics_qtl)), and sQTL ([ROSMAP DLPFC](xqtl-data/qtl/sQTL/ROSMAP_DLPFC_splicing_qtl), [ROSMAP PCC](xqtl-data/qtl/sQTL/ROSMAP_PCC_splicing_qtl), [ROSMAP AC](xqtl-data/qtl/sQTL/ROSMAP_AC_splicing_qtl), [MSBB](xqtl-data/qtl/sQTL/MSBB_brain_splicing_qtl), [Knight ADRC](xqtl-data/qtl/sQTL/Knight_ADRC_brain_splicing_qtl)), incorporating non-linear QTL effects.

### Alzheimer's Disease Analysis Models

AD-specific models include [AD fine-mapping results](https://www.synapse.org/Synapse:syn69670625) with Bayes factors, posterior probabilities and credible sets ([syn69670625](https://www.synapse.org/Synapse:syn69670625)), and [AD colocalization results](https://www.synapse.org/Synapse:syn69865814) providing statistical evidence of shared genetic architecture per locus ([syn69865814](https://www.synapse.org/Synapse:syn69865814)). [AD-xQTL colocalization models](https://www.synapse.org/Synapse:syn69865816) offer comprehensive colocalization statistics between AD risk and molecular traits ([syn69865816](https://www.synapse.org/Synapse:syn69865816), [syn69670630](https://www.synapse.org/Synapse:syn69670630)). We also provide [cTWAS inputs and results](https://www.synapse.org/Synapse:syn74908389) (single-group and multi-group cTWAS) for causal transcriptome-wide association studies in AD ([syn74908389](https://www.synapse.org/Synapse:syn74908389)).

## Raw QTL Summary Statistics

### Linear Regression and Mixed Model Results

We provide [R-based linear model residuals](xqtl-data/qtl/) and tensorQTL outputs in two forms: [raw results for all variants](xqtl-data/qtl/) and [significant results after multiple testing correction](xqtl-data/qtl/) containing standard additive genetic effects. For splicing analysis, [generalized linear mixed model sQTL results](https://www.synapse.org/Synapse:syn69670647) account for the count-based nature of splice junction data while controlling for related observations using meta-cell approaches in single-cell data.

### Non-linear Genetic Effects

[Quantile regression QTL results](xqtl-data/qtl/) identify variants affecting expression variance and outliers, revealing heterogeneous genetic effects relevant to disease states. [QTL interaction analyses](xqtl-data/qtl/) test for genotype-by-sex, APOE4 genotype, and cell proportion interactions to capture context-dependent genetic effects.

## Reference Data and Resources

### Population-Specific LD References

We provide [ADSP-based LD reference data for European ancestry](xqtl-data/reference_data/ld_reference) populations, formatted in plink bim format with xz compression ([syn69670651](https://www.synapse.org/Synapse:syn69670651), [syn69670652](https://www.synapse.org/Synapse:syn69670652)). These panels derive from the Alzheimer's Disease Sequencing Project whole genome sequencing data (16,905 European ancestry samples), providing improved coverage of low-frequency variants. With larger sample sizes than 1000 Genomes reference panels, they demonstrate superior performance for fine-mapping in GWAS meta-analysis for AD and beyond. Pre-computed in-sample LD matrices for 1,361 LD blocks are in [syn75082259](https://www.synapse.org/Synapse:syn75082259). We also provide an [LD sketch panel](https://www.synapse.org/Synapse:syn75082260) (plink2 format, [syn75082260](https://www.synapse.org/Synapse:syn75082260)): the ADSP genotypes are multiplied by a random matrix, so LD between variants is preserved while rows no longer correspond to individual participants.

### Functional Annotation Resources

Our [LDSC reference data](https://www.synapse.org/Synapse:syn69670653), computed from ADSP LD references rather than default 1000 Genomes panels, includes [LD scores](xqtl-data/reference_data/) optimized for AD heritability estimation, [stratified LDSC annotations](xqtl-data/reference_data/) for functional enrichment across brain-specific elements, and [pre-processed GWAS summary statistics](xqtl-data/reference_data/). Stratified LDSC baseline-LD v2.2 reference files (1000 Genomes EUR and ADSP-overlap versions) are in [syn75157484](https://www.synapse.org/Synapse:syn75157484). Additionally, [functional enrichment annotations](xqtl-data/reference_data/) in UCSC bed format encompass regulatory elements, cell-type-specific markers, and brain-specific annotations relevant to neurodegeneration.

### Protocols and Tutorials

Tutorials now live in the [xQTL protocol repository](https://github.com/StatFunGen/xqtl-protocol) and its [documentation site](https://statfungen.github.io/xqtl-protocol/README.html), with example datasets for QTL mapping, fine-mapping, colocalization, and integrative analyses. Start with the [xQTL Analysis Workflow Builder](https://statfungen.github.io/xqtl-protocol/xqtl_protocol_workflow_builder.html): it asks what you measured and what you want to find out, then shows the modules to run and the commands for each. [Environment Setup](https://statfungen.github.io/xqtl-protocol/xqtl-protocol-demo) covers installation.

## Data Format and Column Descriptions

All exported bed files follow standardized formats with consistent column definitions. See our [file and format description page](xqtl_resource_format) for detailed specifications.


## Synapse Data Access

All FunGen-xQTL flagship paper datasets are hosted on [Synapse](https://www.synapse.org/). The table below summarizes the primary resource folders.

| Resource | Description | Synapse ID |
|----------|-------------|------------|
| **Variant & gene summary results** | AD loci, xQTL loci, fine-mapping and colocalization summaries | [syn69865684](https://www.synapse.org/Synapse:syn69865684) |
| **xQTL GWAS models** | All statistical models: fine-mapping, TWAS, colocalization, AD integration | [syn69670588](https://www.synapse.org/Synapse:syn69670588) |
| **Raw xQTL data** | Raw QTL summary statistics (linear regression, quantile regression, interaction) | [syn69670632](https://www.synapse.org/Synapse:syn69670632) |
| **Reference files** | ADSP LD reference, LDSC scores, functional enrichment annotations | [syn69670634](https://www.synapse.org/Synapse:syn69670634) |
| Fine-mapping models | SuSiE-RSS / fSuSiE model objects (.rds) for all xQTL datasets | [syn69670592](https://www.synapse.org/Synapse:syn69670592) |
| Multi-context fine-mapping | Multi-context fine-mapping summaries (ROSMAP, MSBB) | [syn69865754](https://www.synapse.org/Synapse:syn69865754) |
| Multi-gene fine-mapping | Multi-gene fine-mapping summaries (eQTL, pQTL) | [syn69865757](https://www.synapse.org/Synapse:syn69865757) |
| Trans fine-mapping | Trans-xQTL fine-mapping summaries | [syn69865773](https://www.synapse.org/Synapse:syn69865773) |
| xQTL colocalization summaries | Multi-context, trans and pairwise colocalization summaries | [syn69865795](https://www.synapse.org/Synapse:syn69865795) |
| scEEMS scores | Single-cell eQTL effect models and predictions | [syn69670587](https://www.synapse.org/Synapse:syn69670587) |
| Single-nucleus sQTL (ISSAC GLMM) | Cell-type and subtype sQTL summary statistics | [syn69670647](https://www.synapse.org/Synapse:syn69670647) |
| Colocalization models | ColocBoost multi-context + SuSiE-coloc pairwise models | [syn69670597](https://www.synapse.org/Synapse:syn69670597) |
| TWAS weight models | Pre-trained TWAS weight models (eQTL, sQTL, pQTL, gpQTL) | [syn69670600](https://www.synapse.org/Synapse:syn69670600) |
| qTWAS models | Quantile TWAS weight models | [syn69670611](https://www.synapse.org/Synapse:syn69670611) |
| AD GWAS fine-mapping | SuSiE-RSS fine-mapping results for AD GWAS | [syn69670625](https://www.synapse.org/Synapse:syn69670625) |
| AD GWAS colocalization results | Cross-GWAS ColocBoost colocalization summary | [syn69865814](https://www.synapse.org/Synapse:syn69865814) |
| AD GWAS fine-mapping top loci | Per-study AD GWAS top loci (incl. 2026 Bellenguez updates) | [syn69865805](https://www.synapse.org/Synapse:syn69865805) |
| AD–xQTL colocalization results | AD GWAS × xQTL colocalization summary statistics | [syn69865816](https://www.synapse.org/Synapse:syn69865816) |
| AD–xQTL colocalization models | AD GWAS × xQTL colocalization model objects | [syn69670630](https://www.synapse.org/Synapse:syn69670630) |
| cTWAS inputs and results | Causal TWAS inputs, single-group and multi-group results for AD | [syn74908389](https://www.synapse.org/Synapse:syn74908389) |
| cTWAS exported results | Exported cTWAS summary (bed) | [syn69865822](https://www.synapse.org/Synapse:syn69865822) |
| TWAS / MR exported results | Exported TWAS and Mendelian randomization summaries (bed) | [syn69865821](https://www.synapse.org/Synapse:syn69865821) |
| AD TWAS association | Per-context AD TWAS association results | [syn74908416](https://www.synapse.org/Synapse:syn74908416) |
| **AD × xQTL integration summary** | 195-locus AD loci × xQTL workbook, variant-level and overlap tables, AD gene lists | [syn69865823](https://www.synapse.org/Synapse:syn69865823) |
| ADSP LD reference (genotypes) | 16,905 European ancestry WGS samples, plink format | [syn69670651](https://www.synapse.org/Synapse:syn69670651) |
| ADSP LD reference (LD matrices) | Pre-computed in-sample LD matrices for fine-mapping | [syn75082259](https://www.synapse.org/Synapse:syn75082259) |
| ADSP LD sketch | Privacy-preserving LD sketch panel (plink2) | [syn75082260](https://www.synapse.org/Synapse:syn75082260) |
| sLDSC reference data | Stratified LDSC baseline-LD v2.2 reference files | [syn75157484](https://www.synapse.org/Synapse:syn75157484) |

## Citation and Usage

Please cite appropriate manuscripts and acknowledge consortium data generation efforts. Detailed citation information will be provided upon publication.

[ad_loci_xqtl_table]: https://github.com/StatFunGen/xqtl-resources/blob/main/data/genes/unified_AD_loci_xQTL_summary.xlsx
[ad_genes_fungen_xqtl]: https://github.com/StatFunGen/xqtl-resources/blob/main/data/genes/AD_genes_FunGen_AD_GVC_xQTL_20250325.tsv
[ad_genes_twas_xqtl]: https://github.com/StatFunGen/xqtl-resources/blob/main/data/genes/AD_genes_FunGen_AD_twas_GVC_xQTL_20250325.tsv
