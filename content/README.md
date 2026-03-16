# FunGen-AD Resources

## About FunGen-AD
The **[Alzheimer's Disease Sequencing Project Functional Genomics Consortium (FunGen-AD)](https://adsp-fgc.niagads.org/)** is a collaborative initiative aimed at understanding the molecular mechanisms underlying Alzheimer's disease through multi-omic and genetic screening approaches.

## Available Resources

### FunGen-xQTL
The FunGen-xQTL project provides comprehensive molecular quantitative trait loci (QTL) analyses across multiple molecular phenotypes, along with integrative analysis for neurodegenerative disorders particularly Alzheimer's disease. All datasets are hosted on Synapse at the [FunGen-xQTL project page (syn72381203)](https://www.synapse.org/Synapse:syn72381203).

* **[xQTL Analysis and xQTL-GWAS Integration Results](xqtl_resource_description)** along with **[File Format Description](xqtl_resource_format)**
* **[Study Cohorts](xqtl-data/study_info/)** - Information about participating cohorts including ROSMAP, Knight ADRC, MSBB, MiGA, MAGENTA, STARNET, EFIGA, WHICAP, and MetaBrain
* **[GWAS Summary Statistics](xqtl-data/gwas/)** - Alzheimer's disease GWAS data from major studies (Bellenguez 2022, Kunkle 2019, Wightman 2021, Jansen 2021) and integrated AD fine-mapping and colocalization analyses
* **[Molecular Phenotypes](xqtl-data/omics/)** - Multi-omic data including:
  - Gene expression (bulk RNA-seq: ROSMAP DLPFC/PCC/AC/microglia/monocyte, MSBB, Knight ADRC, MetaBrain, MiGA, MAGENTA, STARNET)
  - Alternative splicing (bulk RNA-seq and single-nucleus with ISSAC method)
  - Proteomics including glycoproteomics (brain and CSF)
  - DNA methylation
  - Histone modification (H3K9ac ChIP-seq)
  - Chromatin accessibility (snATAC-seq)
  - Metabolomics (brain, CSF, and plasma)
  - Single-nucleus RNA-seq (ROSMAP DLPFC: CUIMC, MIT, and mega cohorts)
  - Genotype (WGS) and covariates
* **[xQTL Data](xqtl-data/qtl/)** - Molecular QTL associations organized by modality: [eQTL](xqtl-data/qtl/eQTL), [sQTL](xqtl-data/qtl/sQTL), [pQTL](xqtl-data/qtl/pQTL), [gpQTL](xqtl-data/qtl/gpQTL), [mQTL](xqtl-data/qtl/mQTL), [haQTL](xqtl-data/qtl/haQTL), [caQTL](xqtl-data/qtl/caQTL), [metaQTL](xqtl-data/qtl/metaQTL)
* **[Reference Data](xqtl-data/reference_data/)** - ADSP-based LD reference panels (16,905 European ancestry samples) and other analytical resources

Software resources implementing the xQTL analysis are also available:

* **[xQTL Analysis Protocol](https://statfungen.github.io/xqtl-protocol)** - Standardized computational protocols for QTL mapping, fine-mapping, colocalization, and integrative analyses
* **[xQTL Companion Statistical Methods Implementation](https://github.com/StatFunGen/pecotmr)** - Fine-mapping, enrichment, colocalization, TWAS, and Mendelian randomization tools

## Data Access
All datasets are available through controlled access via:
- [Synapse Platform](https://www.synapse.org/Synapse:syn72381203) (primary repository — FunGen-xQTL project syn72381203)
- [NIAGADS](https://www.niagads.org/) (genomics data)

---
*This resource is actively maintained by the FunGen-AD Analysis Working Group and reflects data generated through March 2026*
