# FunGen-AD Resources

## About FunGen-AD

The [Alzheimer's Disease Sequencing Project Functional Genomics Consortium (FunGen-AD)](https://adsp-fgc.niagads.org/) studies the molecular mechanisms of Alzheimer's disease (AD) through multi-omic and genetic approaches.

## Available Resources

### FunGen-xQTL

FunGen-xQTL maps molecular quantitative trait loci (QTL) across multiple molecular phenotypes and integrates them with GWAS of neurodegenerative disease, with AD as the model disease. All datasets are hosted on Synapse, in four folders: [variant and gene summaries](https://www.synapse.org/Synapse:syn69865684) (syn69865684), [xQTL models](https://www.synapse.org/Synapse:syn69670588) (syn69670588), [raw QTL data](https://www.synapse.org/Synapse:syn69670632) (syn69670632), and [reference files](https://www.synapse.org/Synapse:syn69670634) (syn69670634).

* **[xQTL analysis and xQTL-GWAS integration results](xqtl_resource_description)** and the **[file format description](xqtl_resource_format)**.
* **[Study cohorts](xqtl-data/study_info/)** describe the participating cohorts ROSMAP, Knight ADRC, MSBB, MiGA, STARNET, and MetaBrain.
* **[GWAS summary statistics](xqtl-data/gwas/)** cover the major AD GWAS (Bellenguez 2022, Kunkle 2019, Wightman 2021, Jansen 2019). The 2026 update adds the Bellenguez main, no-biobank and no-proxy analyses. Integrated AD fine-mapping and colocalization results are listed on the same page.
* **[Molecular phenotypes](xqtl-data/omics/)** include the following.
  - Gene expression from bulk RNA-seq (ROSMAP DLPFC, PCC, AC, microglia and monocyte; MSBB; Knight ADRC; MetaBrain; MiGA; STARNET).
  - Alternative splicing from bulk RNA-seq and from single-nucleus data (ISSAC method).
  - Proteomics and glycoproteomics of brain.
  - DNA methylation.
  - Histone modification (H3K9ac ChIP-seq).
  - Chromatin accessibility (snATAC-seq).
  - Metabolomics of brain.
  - Single-nucleus RNA-seq (ROSMAP DLPFC, in the CUIMC, MIT and mega cohorts).
  - Whole-genome sequencing genotypes and covariates.
* **[xQTL data](xqtl-data/qtl/)** are molecular QTL associations organized by modality, namely [eQTL](xqtl-data/qtl/eQTL), [sQTL](xqtl-data/qtl/sQTL), [pQTL](xqtl-data/qtl/pQTL), [glycoQTL](xqtl-data/qtl/glycoQTL), [mQTL](xqtl-data/qtl/mQTL), [haQTL](xqtl-data/qtl/haQTL), [caQTL](xqtl-data/qtl/caQTL) and [metQTL](xqtl-data/qtl/metQTL). They also include ROSMAP transcriptomic pattern QTL (tpQTL) and trans-xQTL.
* **[FGMB Atlas](fgmb_weights_database)** provides multi-context regulome-wide association study (RWAS) prediction models, with Synapse accessions for the models, gene-level association results and causal fine-mapping outputs.
* **AD loci integration summary** gives the 195-locus AD GWAS and xQTL summary from the October 2026 release on Synapse ([syn69865823](https://www.synapse.org/Synapse:syn69865823)). The same data can be browsed in the interactive [xQTL-AD-loci-explorer](https://wanggroup.org/xQTL-AD-loci-explorer/).
* **[Reference data](xqtl-data/reference_data/)** include ADSP-based LD reference panels (16,905 European ancestry samples), an LD sketch panel, and other analytical resources.

Two software resources implement the xQTL analyses.

* **[xQTL analysis protocol](https://statfungen.github.io/xqtl-protocol)** gives standardized computational protocols and tutorials for QTL mapping, fine-mapping, colocalization and integrative analyses. Its [xQTL Analysis Workflow Builder](https://statfungen.github.io/xqtl-protocol/xqtl_protocol_workflow_builder.html) selects the modules and commands for your data.
* **[pecotmr](https://github.com/StatFunGen/pecotmr)** implements the companion statistical methods for fine-mapping, enrichment, colocalization, TWAS and Mendelian randomization.

## Data Access

All datasets are available through controlled access.

- Synapse, [variant and gene summaries](https://www.synapse.org/Synapse:syn69865684) (syn69865684)
- Synapse, [xQTL models](https://www.synapse.org/Synapse:syn69670588) (syn69670588)
- Synapse, [raw QTL data](https://www.synapse.org/Synapse:syn69670632) (syn69670632)
- Synapse, [reference files](https://www.synapse.org/Synapse:syn69670634) (syn69670634)
- [NIAGADS](https://www.niagads.org/) for genomics data

---
*The FunGen-AD Analysis Working Group maintains this resource, which reflects data generated through October 2026.*
