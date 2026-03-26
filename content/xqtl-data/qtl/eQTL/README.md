# Expression QTL (eQTL) Resources

Expression quantitative trait loci (eQTL) identify genetic variants that influence gene expression levels measured by bulk or single-cell RNA sequencing. This resource provides eQTL summary statistics, fine-mapping results, TWAS/qTWAS pre-trained models, and colocalization analyses across multiple brain regions, peripheral tissues, and AD-relevant cohorts.

## Overview

eQTL mapping was performed using the [FunGen-xQTL pipeline](https://statfungen.github.io/xqtl-protocol/README.html) across diverse human brain regions and cell types. All datasets underwent harmonized genotype QC, expression normalization, and covariate adjustment. Fine-mapping was performed using SuSiE-RSS to generate posterior inclusion probabilities (PIPs), credible sets (CS), and effect sizes. TWAS weight models and quantile TWAS (qTWAS) models are provided for key datasets.

## Available Datasets

### Brain Tissue — ROSMAP Cohort

| Dataset | Brain Region / Cell Type | Synapse |
|---------|--------------------------|---------|
| [ROSMAP DLPFC](ROSMAP_DLPFC_expression_qtl) | Dorsolateral prefrontal cortex (bulk RNA-seq) | [syn69670592](https://www.synapse.org/Synapse:syn69670592) |
| [ROSMAP PCC](ROSMAP_PCC_expression_qtl) | Posterior cingulate cortex (bulk RNA-seq) | — |
| [ROSMAP AC](ROSMAP_AC_expression_qtl) | Anterior cingulate cortex (bulk RNA-seq) | — |
| [ROSMAP microglia](ROSMAP_microglia_expression_qtl) | Microglia (bulk RNA-seq) | — |
| [ROSMAP monocyte](ROSMAP_monocyte_expression_qtl) | Peripheral blood monocytes | — |
| [ROSMAP snRNA-seq pseudo-bulk](ROSMAP_snRNAseq_pseudo_bulk_qtl) | Single-nucleus RNA-seq, 7 major cell types (CUIMC + MIT) | — |

### Brain Tissue — Other Cohorts

| Dataset | Cohort / Brain Region | Synapse |
|---------|-----------------------|---------|
| [MSBB](MSBB_brain_expression_qtl) | Mount Sinai Brain Bank, 4 brain regions | — |
| [MiGA](MiGA_brain_expression_qtl) | Microglia in Genomics and Aging (multi-brain region) | — |
| [MetaBrain](MetaBrain_brain_expression_qtl) | MetaBrain consortium (multi-brain region) | — |
| [Knight ADRC](Knight_ADRC_brain_expression_qtl) | Knight ADRC brain (WashU) | — |

### Blood / Peripheral Tissue

| Dataset | Cohort / Tissue | Synapse |
|---------|-----------------|---------|
| [MAGENTA African American](MAGENTA_AA_blood_expression_qtl) | MAGENTA cohort, African American whole blood | — |
| [MAGENTA Non-Hispanic White](MAGENTA_NHW_blood_expression_qtl) | MAGENTA cohort, Non-Hispanic White whole blood | — |
| [STARNET macrophage](STARNET_macrophage_qtl) | STARNET macrophage gene expression | — |

## Analyses Performed

### Single-Context Fine-Mapping

Fine-mapping using **SuSiE-RSS** is performed per dataset and per molecular phenotype, yielding:
- Posterior inclusion probabilities (PIPs)
- 95% credible sets (CS)
- Standardized effect sizes (beta) and standard errors

### Multi-Context Fine-Mapping

For ROSMAP (DLPFC, PCC, AC) and MSBB cohorts, **mvSuSiE** (multivariate SuSiE with MASH prior) integrates signals across multiple brain regions jointly to improve power and resolution. Multi-context results are deposited in [syn69670592](https://www.synapse.org/Synapse:syn69670592).

### Multi-Gene Fine-Mapping

Separate multi-gene fine-mapping analyses for eQTLs jointly model nearby genes to resolve signals with shared genetic variants. Results available at [syn69670592](https://www.synapse.org/Synapse:syn69670592).

### Trans-eQTL Fine-Mapping

Genome-wide trans-eQTL analyses identify distant regulatory relationships (>5 Mb or inter-chromosomal). Trans-eQTL fine-mapping results for ROSMAP DLPFC are provided at [ROSMAP DLPFC](ROSMAP_DLPFC_expression_qtl).

### TWAS / qTWAS Models

Pre-trained transcriptome-wide association study (TWAS) models are available for integrating eQTL weights with AD GWAS summary statistics:
- **TWAS weight models** ([syn69670600](https://www.synapse.org/Synapse:syn69670600)): ROSMAP DLPFC, PCC, AC; MSBB; Knight ADRC
- **qTWAS models** ([syn69670611](https://www.synapse.org/Synapse:syn69670611)): quantile regression models capturing non-linear eQTL effects
- **cTWAS inputs** ([syn70095142](https://www.synapse.org/Synapse:syn70095142)): formatted for causal TWAS accounting for LD structure

### Colocalization

Multi-context colocalization using **ColocBoost** across cohorts and brain regions identifies shared genetic signals between eQTLs and other molecular traits ([syn69670597](https://www.synapse.org/Synapse:syn69670597)). AD GWAS–eQTL colocalization results are available at [syn69865816](https://www.synapse.org/Synapse:syn69865816) and [syn69670630](https://www.synapse.org/Synapse:syn69670630).

### Single-Cell eQTL Prediction (scEEMs)

The **scEEMs** model predicts cell-type-specific eQTL effects using a CatBoost binary classifier trained on 4,839 genomic features (TSS distance, ABC scores, baseline annotations, cell-type-specific annotations, deep learning variant effect predictions, and gene features) with leave-one-chromosome-out cross-validation. Models trained on ROSMAP snRNA-seq pseudo-bulk data are described in [ROSMAP snRNA-seq pseudo-bulk](ROSMAP_snRNAseq_pseudo_bulk_qtl).

## Data Access

All fine-mapping models and TWAS weights are hosted on [Synapse](https://www.synapse.org/). Access requires a Synapse account and acceptance of the appropriate data use agreement.

| Resource | Synapse ID |
|----------|------------|
| Fine-mapping models (eQTL) | [syn69670592](https://www.synapse.org/Synapse:syn69670592) |
| TWAS weight models | [syn69670600](https://www.synapse.org/Synapse:syn69670600) |
| qTWAS models | [syn69670611](https://www.synapse.org/Synapse:syn69670611) |
| cTWAS input files | [syn70095142](https://www.synapse.org/Synapse:syn70095142) |
| Colocalization models | [syn69670597](https://www.synapse.org/Synapse:syn69670597) |
| AD–eQTL colocalization results | [syn69865816](https://www.synapse.org/Synapse:syn69865816) |
| AD–eQTL colocalization models | [syn69670630](https://www.synapse.org/Synapse:syn69670630) |
