# FunGen-AD Resources

## About FunGen-AD
The **[Alzheimer's Disease Sequencing Project Functional Genomics Consortium (FunGen-AD)](https://adsp-fgc.niagads.org/)** is a collaborative initiative aimed at understanding the molecular mechanisms underlying Alzheimer's disease through multi-omic and genetic screening approaches.

## Available Resources

### FunGen-xQTL
The FunGen-xQTL project provides comprehensive molecular quantitative trait loci (QTL) analyses across multiple molecular phenotypes, along with integrative analysis for neurodegenerative disorders particularly Alzheimer's disease. The data are on the AD Knowledge Portal and NIAGADS; the table above lists each folder and its access.

* **[xQTL Analysis and xQTL-GWAS Integration Results](xqtl_resource_description)** along with **[File Format Description](xqtl_resource_format)**
* **[Study Cohorts](xqtl-data/study_info/)** - Information about participating cohorts including ROSMAP, Knight ADRC, MSBB, MiGA, STARNET, and MetaBrain
* **[GWAS Summary Statistics](xqtl-data/gwas/)** - Alzheimer's disease GWAS data from major studies (Bellenguez 2022, Kunkle 2019, Wightman 2021, Jansen 2019; the 2026 update adds the Bellenguez main, no-biobank and no-proxy analyses) and integrated AD fine-mapping and colocalization analyses
* **[Molecular Phenotypes](xqtl-data/omics/)** - Multi-omic data including:
  - Gene expression (bulk RNA-seq: ROSMAP DLPFC/PCC/AC/microglia/monocyte, MSBB, Knight ADRC, MetaBrain, MiGA, STARNET)
  - Alternative splicing (bulk RNA-seq and single-nucleus with ISSAC method)
  - Proteomics including glycoproteomics (brain)
  - DNA methylation
  - Histone modification (H3K9ac ChIP-seq)
  - Chromatin accessibility (snATAC-seq)
  - Metabolomics (brain)
  - Single-nucleus RNA-seq (ROSMAP DLPFC: CUIMC1, MIT, and mega cohorts)
  - Genotype (WGS) and covariates
* **[xQTL Data](xqtl-data/qtl/)** - Molecular QTL associations organized by modality: [eQTL](xqtl-data/qtl/eQTL), [sQTL](xqtl-data/qtl/sQTL), [pQTL](xqtl-data/qtl/pQTL), [glycoQTL](xqtl-data/qtl/glycoQTL), [mQTL](xqtl-data/qtl/mQTL), [haQTL](xqtl-data/qtl/haQTL), [caQTL](xqtl-data/qtl/caQTL), [metQTL](xqtl-data/qtl/metQTL), plus ROSMAP transcriptomic pattern QTLs (tpQTL) and trans-xQTLs
* **[FGMB Atlas](fgmb_weights_database)** - FunGen-xQTL Multi-Brain Atlas: models that predict molecular traits from genotype across brain contexts, for regulome-wide association studies (RWAS), with AD Knowledge Portal accessions for the models, gene-level association results and causal fine-mapping outputs.
* **[scEEMS scores](sceems_scores)** - Machine learning predictions of causal eQTLs in six brain cell types, with the models and fine-mapping results that use them as priors
* **[AD Loci Integration Summary](https://www.synapse.org/Synapse:syn69865823)** - The 226-locus AD GWAS × xQTL summary (November 2026 release) on the AD Knowledge Portal ([syn69865823](https://www.synapse.org/Synapse:syn69865823)), also browsable in the interactive [xQTL-AD-loci-explorer](https://xqtl.niagads.org/AD-loci-explorer/)
* **[Reference Data](xqtl-data/reference_data/)** - ADSP-based LD reference panels (16,571 European ancestry samples), including an LD sketch panel, and other analytical resources

Software resources implementing the xQTL analysis are also available:

* **[xQTL Analysis Protocol](https://statfungen.github.io/xqtl-protocol)** - Standardized computational protocols for QTL mapping, fine-mapping, colocalization, and integrative analyses, with tutorials and an [xQTL Analysis Workflow Builder](https://statfungen.github.io/xqtl-protocol/xqtl_protocol_workflow_builder.html) that picks the modules and commands for your data
* **[xQTL Companion Statistical Methods Implementation](https://github.com/StatFunGen/pecotmr)** - Fine-mapping, enrichment, colocalization, TWAS, and Mendelian randomization tools
