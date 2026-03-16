# Metabolome QTL (metaQTL) Resources

Metabolome quantitative trait loci (metaQTL) identify genetic variants that influence metabolite levels measured by mass spectrometry-based metabolomics. Metabolomics provides a direct readout of cellular biochemical activity and can reveal disease-relevant metabolic pathways linked to genetic variation. This resource provides metaQTL summary statistics, fine-mapping results, and colocalization analyses across brain tissue, cerebrospinal fluid (CSF), and plasma from AD-relevant cohorts.

## Overview

metaQTL mapping was performed using the [FunGen-xQTL pipeline](https://statfungen.github.io/xqtl-protocol/README.html). Metabolite abundances from untargeted or targeted mass spectrometry underwent log-transformation, batch correction, and covariate adjustment before tensorQTL-based association testing. Fine-mapping was performed using SuSiE-RSS yielding posterior inclusion probabilities (PIPs) and credible sets.

## Available Datasets

### Brain Tissue

| Dataset | Cohort / Brain Region | Synapse |
|---------|-----------------------|---------|
| [ROSMAP DLPFC](../ROSMAP_DLPFC_metabolomics_qtl) | ROSMAP dorsolateral prefrontal cortex | [syn69670592](https://www.synapse.org/Synapse:syn69670592) |
| [Knight ADRC brain](../Knight_ADRC_brain_metabolomics_qtl) | Knight ADRC brain (WashU) | — |

### Cerebrospinal Fluid (CSF)

| Dataset | Cohort | Synapse |
|---------|--------|---------|
| [Knight ADRC CSF](../Knight_ADRC_CSF_metabolomics_qtl) | Knight ADRC CSF (WashU) | — |

### Plasma

| Dataset | Cohort | Synapse |
|---------|--------|---------|
| [EFIGA plasma](../EFIGA_plasma_metabolomics_qtl) | EFIGA cohort plasma metabolomics | — |
| [WHICAP plasma (pilot)](../WHICAP_plasma_metabolomics_qtl) | Washington Heights–Inwood Columbia Aging Project pilot | — |

## Analyses Performed

### Single-Context Fine-Mapping

Fine-mapping using **SuSiE-RSS** per metabolite, providing:
- Posterior inclusion probabilities (PIPs)
- 95% credible sets
- Effect sizes on metabolite abundance

### Trans-metaQTL Fine-Mapping

Genome-wide trans-metaQTL analyses identify distant genetic influences on metabolite levels. Trans-metaQTL results for ROSMAP DLPFC are provided at [ROSMAP DLPFC](../ROSMAP_DLPFC_metabolomics_qtl).

### Colocalization

**ColocBoost** multi-context colocalization identifies shared metabolite QTL signals across cohorts and tissues ([syn69670597](https://www.synapse.org/Synapse:syn69670597)). AD GWAS–metaQTL colocalization results are at [syn69865816](https://www.synapse.org/Synapse:syn69865816) and [syn69670630](https://www.synapse.org/Synapse:syn69670630).

## Data Access

| Resource | Synapse ID |
|----------|------------|
| Fine-mapping models (metaQTL) | [syn69670592](https://www.synapse.org/Synapse:syn69670592) |
| Colocalization models | [syn69670597](https://www.synapse.org/Synapse:syn69670597) |
| AD–metaQTL colocalization results | [syn69865816](https://www.synapse.org/Synapse:syn69865816) |
| AD–metaQTL colocalization models | [syn69670630](https://www.synapse.org/Synapse:syn69670630) |
