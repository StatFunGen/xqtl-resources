# MetaBrain Brain Gene Expression QTL

MetaBrain multi-region bulk RNA-seq gene expression data used for validation of eQTL signals in the FunGen-xQTL flagship study.

## Contact

FunGen-xQTL Analysis Team

## Study Overview

- Study name: MetaBrain brain expression eQTL
- Study Description: Large-scale brain eQTL meta-analysis across five brain regions used as a validation and replication resource. All five MetaBrain contexts were used to replicate xQTL signals identified in the ROSMAP, MSBB, and MiGA cohorts.
- Brain regions: Cerebellum, Cortex, Basal ganglia, Spinal cord, Hippocampus
- Reference: Schipper et al. 2021, *Nature Neuroscience*. doi:10.1038/s41593-021-00976-7

## Analysis Details

MetaBrain summary statistics were obtained from the [MetaBrain resource](https://www.metabrain.nl/) and used as an independent eQTL replication dataset in the FunGen-xQTL flagship analysis. Fine-mapping and colocalization were performed in parallel with the primary FunGen-xQTL datasets.

## Links to QTL analysis notebooks

See MetaBrain processing notebooks in:
- https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/MetaBrain

### Path(s) to summary statistics

- MetaBrain portal: https://www.metabrain.nl/

### Path(s) to fine-mapping with SuSiE RSS model

Fine-mapping model objects (SuSiE-RSS, `.rds`) are available in the [finemapping models folder (syn69670592)](https://www.synapse.org/Synapse:syn69670592).

### Path(s) to TWAS models

Pre-trained TWAS weight models for this context: [syn69670600](https://www.synapse.org/Synapse:syn69670600)

Quantile TWAS (qTWAS) models: [syn69670611](https://www.synapse.org/Synapse:syn69670611)

### Path(s) to colocalization with SuSiE-coloc / ColocBoost

Multi-context colocalization models (ColocBoost): [syn69670597](https://www.synapse.org/Synapse:syn69670597)

AD GWAS–xQTL colocalization results: [syn69865816](https://www.synapse.org/Synapse:syn69865816)

AD GWAS–xQTL colocalization models: [syn69670630](https://www.synapse.org/Synapse:syn69670630)
