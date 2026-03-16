# Chromatin Accessibility QTL (caQTL) Resources

Chromatin accessibility quantitative trait loci (caQTL) identify genetic variants that influence open chromatin regions measured by ATAC-seq or snATAC-seq. Open chromatin marks active regulatory elements (promoters, enhancers, insulators) and caQTLs can reveal the functional impact of non-coding genetic variants on gene regulation. This resource provides single-nucleus caQTL summary statistics, fine-mapping results, and colocalization analyses in AD-relevant brain cell types.

## Overview

caQTL mapping was performed on single-nucleus ATAC-seq (snATAC-seq) data from brain tissue using the [FunGen-xQTL pipeline](https://statfungen.github.io/xqtl-protocol/README.html). Peak-level chromatin accessibility was quantified per cell type, normalized, and adjusted for covariates before tensorQTL-based association testing. Fine-mapping was performed using SuSiE-RSS or fSuSiE. Pairwise colocalization with AD GWAS uses a [novel epigenetic fine-mapping approach](https://www.biorxiv.org/content/10.1101/2025.08.17.670732v1) to identify chromatin-level regulatory mechanisms of AD risk variants at cell-type resolution.

## Available Datasets

### Brain Tissue — Single-Nucleus

| Dataset | Cohort / Brain Region | Cell Types | Synapse |
|---------|-----------------------|------------|---------|
| [ROSMAP snuc](../ROSMAP_snuc_caQTL_qtl) | ROSMAP multi-region snATAC-seq | Multiple brain cell types | [syn69670592](https://www.synapse.org/Synapse:syn69670592) |

## Analyses Performed

### Single-Context Fine-Mapping

Fine-mapping using **SuSiE-RSS** per ATAC-seq peak and cell type, providing:
- Posterior inclusion probabilities (PIPs)
- 95% credible sets
- Effect sizes on chromatin accessibility

### caQTL–eQTL Pairwise Colocalization

Pairwise **SuSiE-COLOC** analyses examine the relationship between chromatin accessibility QTLs and expression QTLs to identify regulatory variants acting through open chromatin. Results are available at [syn69670597](https://www.synapse.org/Synapse:syn69670597).

### AD GWAS Colocalization

Single-nucleus caQTL–AD GWAS pairwise colocalization uses the epigenetic fine-mapping approach to identify cell-type-specific chromatin accessibility mechanisms of AD genetic risk. Results available at [syn69865816](https://www.synapse.org/Synapse:syn69865816) and [syn69670630](https://www.synapse.org/Synapse:syn69670630).

### Multi-Context Colocalization

**ColocBoost** multi-context colocalization across caQTL cell types and eQTL datasets is available at [syn69670597](https://www.synapse.org/Synapse:syn69670597).

## Data Access

| Resource | Synapse ID |
|----------|------------|
| Fine-mapping models (caQTL) | [syn69670592](https://www.synapse.org/Synapse:syn69670592) |
| Colocalization models (caQTL–eQTL) | [syn69670597](https://www.synapse.org/Synapse:syn69670597) |
| AD–caQTL colocalization results | [syn69865816](https://www.synapse.org/Synapse:syn69865816) |
| AD–caQTL colocalization models | [syn69670630](https://www.synapse.org/Synapse:syn69670630) |
