# ROSMAP Single-Nucleus Chromatin Accessibility QTL (caQTL)

Single-nucleus ATAC-seq chromatin accessibility QTL analysis from ROSMAP donors, covering MIT snATAC-seq and CUIMC & MIT harmonized Multiome ATAC data.

Please refer to [this document](../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Contact

FunGen-xQTL Analysis Team

## Study Overview

- Study name: ROSMAP snATAC-seq caQTL
- Study Description: Chromatin accessibility quantitative trait loci (caQTL) using pseudo-bulk ATAC-seq profiles per cell type. Two datasets are included: (1) MIT snATAC-seq (Mic, Ast, Oli, OPC, Exc, Inh) and (2) CUIMC & MIT harmonized Multiome ATAC (Mic, Ast, Oli, OPC, Exc, Inh). A response caQTL (r-caQTL) analysis was also performed to identify variants affecting chromatin remodeling in context of co-measured gene expression.
- Cell types: Microglia (Mic), Astrocytes (Ast), Oligodendrocytes (Oli), OPCs (OPC), Excitatory neurons (Exc), Inhibitory neurons (Inh)
- Assay: 10x Genomics snATAC-seq and Multiome ATAC

## Analysis Details

### Path(s) to cis-QTL association testing

- `s3://statfungen/ftp_fgc_xqtl/analysis_result/cis_association/ROSMAP/caQTL/`

### Path(s) to fine-mapping with fSuSiE / SuSiE RSS model

Fine-mapping model objects (fSuSiE/SuSiE-RSS, `.rds`) are available in the [finemapping models folder (syn69670592)](https://www.synapse.org/Synapse:syn69670592).

### Path(s) to colocalization

Pairwise colocalization models (SuSiE-coloc): [syn69670597](https://www.synapse.org/Synapse:syn69670597)

AD GWAS–xQTL colocalization results: [syn69865816](https://www.synapse.org/Synapse:syn69865816)

AD GWAS–xQTL colocalization models: [syn69670630](https://www.synapse.org/Synapse:syn69670630)
