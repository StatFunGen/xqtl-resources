# ROSMAP snRNA-seq Splicing (ISSAC-seq)

## Summary

Single-nucleus RNA-seq splicing quantitative trait loci from ROSMAP DLPFC tissue, using harmonized CUIMC and MIT single-nucleus data (ISSAC-seq protocol). Splicing was quantified at the single-cell level and aggregated to pseudobulk profiles per cell type.

## Dataset Information

- **Cohort**: ROSMAP (CUIMC + MIT harmonized, ISSAC-seq)
- **Brain region**: Dorsolateral prefrontal cortex (DLPFC)
- **Data type**: Single-nucleus RNA-seq (snRNA-seq), splicing quantification
- **Cell types**: Multiple brain cell types (excitatory neurons, inhibitory neurons, oligodendrocytes, astrocytes, microglia, OPCs, endothelial cells)
- **Platform**: ISSAC-seq (10x Genomics Chromium)

## Omics Data

### Splicing phenotype matrices

Splicing ratios (percent spliced in, PSI) computed from single-nucleus RNA-seq data, aggregated by cell type and individual. Available through Synapse.

## QTL Analysis
QTL analysis for this dataset is documented in [../qtl/ROSMAP_snuc_splicing_qtl.md](../qtl/ROSMAP_snuc_splicing_qtl.md).

Flagship paper analyses:
- Fine-mapping (SuSiE-RSS): [syn69670592](https://www.synapse.org/Synapse:syn69670592)
- TWAS weight models: [syn69670600](https://www.synapse.org/Synapse:syn69670600)
- Quantile TWAS (qTWAS) models: [syn69670611](https://www.synapse.org/Synapse:syn69670611)
- Multi-context colocalization (ColocBoost): [syn69670597](https://www.synapse.org/Synapse:syn69670597)
- AD GWAS–xQTL colocalization results: [syn69865816](https://www.synapse.org/Synapse:syn69865816)
- AD GWAS–xQTL colocalization models: [syn69670630](https://www.synapse.org/Synapse:syn69670630)
