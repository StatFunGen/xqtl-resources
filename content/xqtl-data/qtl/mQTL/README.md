# Methylation QTL (mQTL) Resources

Methylation quantitative trait loci (mQTL) identify genetic variants that influence DNA methylation levels at CpG sites. DNA methylation is a stable epigenetic mark that regulates gene expression and is implicated in aging and neurodegeneration. This resource provides mQTL summary statistics, fine-mapping results, and colocalization analyses across brain tissues from multiple AD cohorts.

## Overview

mQTL mapping was performed on EPIC or 450K array methylation data from brain tissue, using the [FunGen-xQTL pipeline](https://statfungen.github.io/xqtl-protocol/README.html). Beta-values were M-value transformed, batch corrected, and adjusted for cell-type proportions and principal components before tensorQTL-based association testing. Fine-mapping was performed using SuSiE-RSS (or fSuSiE for multi-context). Pairwise colocalization with AD GWAS fine-mapping uses a novel epigenetic fine-mapping approach developed for this resource.

## Available Datasets

### Brain Tissue

| Dataset | Cohort / Brain Region | Synapse |
|---------|-----------------------|---------|
| [ROSMAP DLPFC](../ROSMAP_DLPFC_methylation_qtl) | ROSMAP dorsolateral prefrontal cortex | [syn69670592](https://www.synapse.org/Synapse:syn69670592) |
| [MSBB](../MSBB_brain_methylation_qtl) | Mount Sinai Brain Bank, 4 brain regions | — |
| [Knight ADRC](../Knight_ADRC_brain_methylation_qtl) | Knight ADRC brain (WashU) | — |

## Analyses Performed

### Single-Context Fine-Mapping

Fine-mapping using **SuSiE-RSS** per CpG site, providing:
- Posterior inclusion probabilities (PIPs)
- 95% credible sets
- Effect sizes on methylation M-values

### Multi-Context Fine-Mapping

For ROSMAP and MSBB multi-region mQTL, **fSuSiE** integrates methylation signals across brain regions. Multi-context fine-mapping results are at [syn69670592](https://www.synapse.org/Synapse:syn69670592).

### AD GWAS Colocalization

Bulk mQTL–AD GWAS pairwise colocalization uses a [novel fine-mapping approach for epigenetic data](https://www.biorxiv.org/content/10.1101/2025.08.17.670732v1) to identify methylation-level mechanisms of AD risk variants. Results available at [syn69865816](https://www.synapse.org/Synapse:syn69865816) and [syn69670630](https://www.synapse.org/Synapse:syn69670630).

### Multi-Context Colocalization

**ColocBoost** multi-context colocalization across mQTL datasets and cohorts is available at [syn69670597](https://www.synapse.org/Synapse:syn69670597).

## Data Access

| Resource | Synapse ID |
|----------|------------|
| Fine-mapping models (mQTL) | [syn69670592](https://www.synapse.org/Synapse:syn69670592) |
| Colocalization models | [syn69670597](https://www.synapse.org/Synapse:syn69670597) |
| AD–mQTL colocalization results | [syn69865816](https://www.synapse.org/Synapse:syn69865816) |
| AD–mQTL colocalization models | [syn69670630](https://www.synapse.org/Synapse:syn69670630) |
