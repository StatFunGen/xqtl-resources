# Splicing QTL (sQTL) Resources

Splicing quantitative trait loci (sQTL) identify genetic variants that influence RNA alternative splicing patterns, measured as intron excision ratios or splice junction usage. This resource provides sQTL summary statistics, fine-mapping results, TWAS/qTWAS pre-trained models, and colocalization analyses across brain tissues, blood, and AD-relevant cohorts.

## Overview

sQTL mapping was performed using the [FunGen-xQTL pipeline](https://statfungen.github.io/xqtl-protocol/README.html). For bulk tissue, splice junction quantification uses LeafCutter-style intron excision ratios followed by tensorQTL mapping. For single-nucleus data, the **ISSAC** (Integrative Single-cell Splicing Analysis for Context) method quantifies splice site usage via UMI-collapsed junction counts using **junctools**, followed by binomial GLMM sQTL mapping with metacell aggregation. Fine-mapping was performed using SuSiE-RSS yielding PIPs and credible sets.

## Available Datasets

### Brain Tissue — ROSMAP Cohort

| Dataset | Brain Region / Cell Type | Method | Synapse |
|---------|--------------------------|--------|---------|
| [ROSMAP DLPFC](../ROSMAP_DLPFC_splicing_qtl) | Dorsolateral prefrontal cortex (bulk) | LeafCutter + tensorQTL | [syn69670592](https://www.synapse.org/Synapse:syn69670592) |
| [ROSMAP PCC](../ROSMAP_PCC_splicing_qtl) | Posterior cingulate cortex (bulk) | LeafCutter + tensorQTL | — |
| [ROSMAP AC](../ROSMAP_AC_splicing_qtl) | Anterior cingulate cortex (bulk) | LeafCutter + tensorQTL | — |
| [ROSMAP snuc (ISSAC)](../ROSMAP_snuc_splicing_qtl) | Single-nucleus (7 major + 95 subcell types) | ISSAC binomial GLMM | — |

### Brain Tissue — Other Cohorts

| Dataset | Cohort / Brain Region | Synapse |
|---------|-----------------------|---------|
| [MSBB](../MSBB_brain_splicing_qtl) | Mount Sinai Brain Bank, 4 brain regions | — |
| [Knight ADRC](../Knight_ADRC_brain_splicing_qtl) | Knight ADRC brain (WashU) | — |

### Blood / Peripheral Tissue

| Dataset | Cohort / Tissue | Synapse |
|---------|-----------------|---------|
| [MAGENTA African American](../MAGENTA_AA_blood_splicing_qtl) | MAGENTA cohort, African American whole blood | — |
| [MAGENTA Non-Hispanic White](../MAGENTA_NHW_blood_splicing_qtl) | MAGENTA cohort, Non-Hispanic White whole blood | — |

## Analyses Performed

### Single-Context Fine-Mapping

Fine-mapping using **SuSiE-RSS** is applied per splicing phenotype (intron cluster or splice site), providing:
- Posterior inclusion probabilities (PIPs)
- 95% credible sets
- Effect sizes on splice junction usage

### ISSAC — Single-Nucleus sQTL Method

For ROSMAP snuc data, **ISSAC** implements:
- **Metacell aggregation**: 23,143 major-cell-type and 87,936 subcell-type metacells from 3,177,748 nuclei (530 donors: CUIMC 424 + MIT 298)
- **Splice site usage quantification** with junctools (UMI-level collapsed)
- **Binomial GLMM** sQTL mapping with PCG/REML for random effects
- **Context-dependent sQTL** analyses: AD-biased (FDR < 0.01), sex-biased (FDR < 0.05), and cell-state-dependent

### Multi-Context Fine-Mapping

For ROSMAP multi-region bulk sQTL, **fSuSiE** integrates splicing signals across DLPFC, PCC, and AC jointly. Multi-context fine-mapping results are at [syn69670592](https://www.synapse.org/Synapse:syn69670592).

### TWAS / qTWAS Models

Pre-trained sQTL-based TWAS models for splicing-level AD association analyses:
- **TWAS weight models** ([syn69670600](https://www.synapse.org/Synapse:syn69670600)): ROSMAP DLPFC, PCC, AC; MSBB; Knight ADRC
- **qTWAS models** ([syn69670611](https://www.synapse.org/Synapse:syn69670611)): quantile regression sQTL models

### Colocalization

**ColocBoost** multi-context colocalization identifies shared splicing QTL signals across brain regions and cohorts ([syn69670597](https://www.synapse.org/Synapse:syn69670597)). AD GWAS–sQTL colocalization results are available at [syn69865816](https://www.synapse.org/Synapse:syn69865816) and [syn69670630](https://www.synapse.org/Synapse:syn69670630).

## Data Access

| Resource | Synapse ID |
|----------|------------|
| Fine-mapping models (sQTL) | [syn69670592](https://www.synapse.org/Synapse:syn69670592) |
| TWAS weight models (sQTL) | [syn69670600](https://www.synapse.org/Synapse:syn69670600) |
| qTWAS models (sQTL) | [syn69670611](https://www.synapse.org/Synapse:syn69670611) |
| Colocalization models | [syn69670597](https://www.synapse.org/Synapse:syn69670597) |
| AD–sQTL colocalization results | [syn69865816](https://www.synapse.org/Synapse:syn69865816) |
| AD–sQTL colocalization models | [syn69670630](https://www.synapse.org/Synapse:syn69670630) |
