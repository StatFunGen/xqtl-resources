# Glycoproteomics QTL (gpQTL) Resources

Glycoproteomics quantitative trait loci (gpQTL) identify genetic variants that influence protein glycosylation levels. Glycosylation is a key post-translational modification affecting protein folding, stability, and function, and is particularly relevant to neurodegeneration and amyloid processing in Alzheimer's disease. This resource provides gpQTL summary statistics, fine-mapping results, TWAS/qTWAS pre-trained models, and trans-gpQTL analyses.

## Overview

gpQTL mapping was performed on glycopeptide-level mass spectrometry data from brain tissue, using the [FunGen-xQTL pipeline](https://statfungen.github.io/xqtl-protocol/README.html). Glycopeptide abundances were normalized and regressed on covariates before tensorQTL-based association testing. Fine-mapping was performed using SuSiE-RSS. This represents one of the first large-scale brain gpQTL resources integrated with AD genetics.

## Available Datasets

### Brain Tissue

| Dataset | Cohort / Brain Region | Synapse |
|---------|-----------------------|---------|
| [ROSMAP DLPFC](../ROSMAP_DLPFC_glycoproteomics_qtl) | ROSMAP dorsolateral prefrontal cortex | [syn69670592](https://www.synapse.org/Synapse:syn69670592) |

## Analyses Performed

### Single-Context Fine-Mapping

Fine-mapping using **SuSiE-RSS** per glycopeptide, yielding:
- Posterior inclusion probabilities (PIPs)
- 95% credible sets
- Effect sizes on glycosylation levels

### Multi-Gene Fine-Mapping

Multi-gene fine-mapping for gpQTLs jointly models co-regulated glycoproteins to resolve shared signals. Results available at [syn69670592](https://www.synapse.org/Synapse:syn69670592).

### Trans-gpQTL Fine-Mapping

Genome-wide trans-gpQTL analyses identify distant genetic influences on glycosylation patterns. Trans-gpQTL fine-mapping results for ROSMAP DLPFC are provided at [ROSMAP DLPFC](../ROSMAP_DLPFC_glycoproteomics_qtl).

### TWAS / qTWAS Models

Pre-trained gpQTL-based TWAS models:
- **TWAS weight models** ([syn69670600](https://www.synapse.org/Synapse:syn69670600)): ROSMAP DLPFC
- **qTWAS models** ([syn69670611](https://www.synapse.org/Synapse:syn69670611)): quantile regression gpQTL models
- **cTWAS inputs** ([syn70095142](https://www.synapse.org/Synapse:syn70095142)): causal TWAS formatted inputs

### Colocalization

AD GWAS–gpQTL colocalization analyses identify glycosylation-level mechanisms of AD risk variants. Results at [syn69865816](https://www.synapse.org/Synapse:syn69865816) and [syn69670630](https://www.synapse.org/Synapse:syn69670630).

## Data Access

| Resource | Synapse ID |
|----------|------------|
| Fine-mapping models (gpQTL) | [syn69670592](https://www.synapse.org/Synapse:syn69670592) |
| TWAS weight models (gpQTL) | [syn69670600](https://www.synapse.org/Synapse:syn69670600) |
| qTWAS models (gpQTL) | [syn69670611](https://www.synapse.org/Synapse:syn69670611) |
| cTWAS input files | [syn70095142](https://www.synapse.org/Synapse:syn70095142) |
| AD–gpQTL colocalization results | [syn69865816](https://www.synapse.org/Synapse:syn69865816) |
| AD–gpQTL colocalization models | [syn69670630](https://www.synapse.org/Synapse:syn69670630) |
