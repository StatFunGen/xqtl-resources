# Protein QTL (pQTL) Resources

Protein quantitative trait loci (pQTL) identify genetic variants that influence protein abundance measured by mass spectrometry-based proteomics. This resource provides pQTL summary statistics, fine-mapping results, TWAS/qTWAS pre-trained models, and colocalization analyses across brain tissue, cerebrospinal fluid (CSF), and AD-relevant cohorts.

## Overview

pQTL mapping was performed using the [FunGen-xQTL pipeline](https://statfungen.github.io/xqtl-protocol/README.html). Protein abundance measurements from tandem mass tag (TMT) mass spectrometry underwent normalization, batch correction, and covariate adjustment prior to tensorQTL-based association testing. Fine-mapping was performed using SuSiE-RSS yielding posterior inclusion probabilities (PIPs) and credible sets.

## Available Datasets

### Brain Tissue

| Dataset | Cohort / Brain Region | Synapse |
|---------|-----------------------|---------|
| [ROSMAP DLPFC](ROSMAP_DLPFC_proteomics_qtl) | ROSMAP dorsolateral prefrontal cortex | [syn69670592](https://www.synapse.org/Synapse:syn69670592) |
| [MSBB](MSBB_proteomics_qtl) | Mount Sinai Brain Bank, 4 brain regions | — |
| [Knight ADRC brain](Knight_ADRC_brain_proteomics_qtl) | Knight ADRC brain (WashU) | — |

### Cerebrospinal Fluid (CSF)

| Dataset | Cohort | Synapse |
|---------|--------|---------|
| [Knight ADRC CSF](Knight_ADRC_CSF_proteomics_qtl) | Knight ADRC CSF proteomics (WashU) | — |
| [EFIGA CSF](EFIGA_CSF_proteomics_qtl) | EFIGA cohort CSF proteomics | — |

## Analyses Performed

### Single-Context Fine-Mapping

Fine-mapping using **SuSiE-RSS** per protein, providing:
- Posterior inclusion probabilities (PIPs)
- 95% credible sets
- Standardized effect sizes

### Multi-Gene Fine-Mapping

Multi-gene fine-mapping for pQTLs jointly models co-regulated proteins in a genomic window, resolving signals shared across proteins. Results available at [syn69670592](https://www.synapse.org/Synapse:syn69670592).

### Trans-pQTL Fine-Mapping

Genome-wide trans-pQTL analyses identify distant protein regulatory relationships. Trans-pQTL fine-mapping results for ROSMAP DLPFC are provided at [ROSMAP DLPFC](ROSMAP_DLPFC_proteomics_qtl).

### TWAS / qTWAS Models

Pre-trained pQTL-based TWAS models for protein-level AD association analyses:
- **TWAS weight models** ([syn69670600](https://www.synapse.org/Synapse:syn69670600)): ROSMAP DLPFC, MSBB, Knight ADRC brain
- **qTWAS models** ([syn69670611](https://www.synapse.org/Synapse:syn69670611)): quantile regression pQTL models
- **cTWAS inputs** ([syn70095142](https://www.synapse.org/Synapse:syn70095142)): formatted for causal TWAS

### Colocalization

**ColocBoost** multi-context colocalization and pairwise SuSiE-COLOC analyses identify shared pQTL signals across cohorts ([syn69670597](https://www.synapse.org/Synapse:syn69670597)). AD GWAS–pQTL colocalization results are at [syn69865816](https://www.synapse.org/Synapse:syn69865816) and [syn69670630](https://www.synapse.org/Synapse:syn69670630).

## Data Access

| Resource | Synapse ID |
|----------|------------|
| Fine-mapping models (pQTL) | [syn69670592](https://www.synapse.org/Synapse:syn69670592) |
| TWAS weight models (pQTL) | [syn69670600](https://www.synapse.org/Synapse:syn69670600) |
| qTWAS models (pQTL) | [syn69670611](https://www.synapse.org/Synapse:syn69670611) |
| cTWAS input files | [syn70095142](https://www.synapse.org/Synapse:syn70095142) |
| Colocalization models | [syn69670597](https://www.synapse.org/Synapse:syn69670597) |
| AD–pQTL colocalization results | [syn69865816](https://www.synapse.org/Synapse:syn69865816) |
| AD–pQTL colocalization models | [syn69670630](https://www.synapse.org/Synapse:syn69670630) |
