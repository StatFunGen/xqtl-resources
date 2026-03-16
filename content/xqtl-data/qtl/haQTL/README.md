# Histone Acetylation QTL (haQTL) Resources

Histone acetylation quantitative trait loci (haQTL) identify genetic variants that influence levels of H3K9 acetylation, an active histone mark associated with promoter and enhancer activity. This resource provides haQTL summary statistics, fine-mapping results, and colocalization analyses linking active regulatory elements to genetic variation in Alzheimer's disease brain tissue.

## Overview

haQTL mapping was performed on H3K9ac ChIP-seq data from brain tissue using the [FunGen-xQTL pipeline](https://statfungen.github.io/xqtl-protocol/README.html). Peak-level H3K9ac read counts were normalized and adjusted for covariates before tensorQTL-based association testing. Fine-mapping was performed using SuSiE-RSS. Pairwise colocalization with AD GWAS fine-mapping uses a [novel epigenetic fine-mapping approach](https://www.biorxiv.org/content/10.1101/2025.08.17.670732v1) developed to map chromatin-level mechanisms of AD risk variants.

## Available Datasets

### Brain Tissue

| Dataset | Cohort / Brain Region | Assay | Synapse |
|---------|-----------------------|-------|---------|
| [ROSMAP DLPFC](../ROSMAP_DLPFC_ChIPSeq_H3K9ac_qtl) | ROSMAP dorsolateral prefrontal cortex | H3K9ac ChIP-seq | [syn69670592](https://www.synapse.org/Synapse:syn69670592) |

## Analyses Performed

### Single-Context Fine-Mapping

Fine-mapping using **SuSiE-RSS** per H3K9ac peak, providing:
- Posterior inclusion probabilities (PIPs)
- 95% credible sets
- Effect sizes on H3K9ac signal

### AD GWAS Colocalization

Bulk haQTL–AD GWAS pairwise colocalization uses the epigenetic fine-mapping approach to identify histone acetylation-level mechanisms of AD genetic risk. Results available at [syn69865816](https://www.synapse.org/Synapse:syn69865816) and [syn69670630](https://www.synapse.org/Synapse:syn69670630).

### Multi-Context Colocalization

**ColocBoost** colocalization identifying shared signals between haQTL and other molecular QTL datasets is available at [syn69670597](https://www.synapse.org/Synapse:syn69670597).

## Data Access

| Resource | Synapse ID |
|----------|------------|
| Fine-mapping models (haQTL) | [syn69670592](https://www.synapse.org/Synapse:syn69670592) |
| Colocalization models | [syn69670597](https://www.synapse.org/Synapse:syn69670597) |
| AD–haQTL colocalization results | [syn69865816](https://www.synapse.org/Synapse:syn69865816) |
| AD–haQTL colocalization models | [syn69670630](https://www.synapse.org/Synapse:syn69670630) |
