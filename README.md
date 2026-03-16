# FunGen-xQTL Resources

This repository contains 100 datasets developed by the ADSP Functional Genomics Consortium (FunGen-AD).

Published at: https://statfungen.github.io/xqtl-resources/

All datasets are hosted on Synapse: [variant & gene summaries (syn69865684)](https://www.synapse.org/Synapse:syn69865684) · [xQTL models (syn69670588)](https://www.synapse.org/Synapse:syn69670588) · [raw QTL data (syn69670632)](https://www.synapse.org/Synapse:syn69670632) · [reference files (syn69670634)](https://www.synapse.org/Synapse:syn69670634)

## Dataset Categories

### Study Information (6 datasets)

- [Knight-ADRC study info](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/study_info/KnightADRC.md): The Memory and Aging Project at the Charles F. And Joanne Knight Alzheimer's Disease Research Center (Knight-ADRC at Washington University in St. Louis) collects plasma, CSF, fibroblast, neuroimaging, clinical and cognition data longitudinally and autopsied brain samples. This clinical information combined with deep molecular phenotyping (i.e. genetic, proteomics, transcriptomics and others) will lead to the identification of novel genetic modifiers, protective variants, molecular biomarkers and novel targets. Participants were recruited by the Knight-ADRC at Washington University in St. Louis (MO).
- [MAGENTA study info](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/study_info/MAGENTA.md): Multi-Ancestry Genomics, Epigenomics, and Transcriptomics of Alzheimer's (MAGENTA) Project: Participants include 465 individuals (AA – 113 with AD, 118 cognitively intact controls; NHW – 116 with AD, 118 controls) ascertained as part of the ADSP Follow-up Study. All participants were adjudicated by a clinical panel with expertise in AD related disorders and classified as AD according to standard criteria developed by the National Institute of Aging and the Alzheimer's Association.
- [MiGA study info](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/study_info/MiGA.md): Microglia Genomic Atlas from the Netherlands Brain Bank (NBB) and the Neuropathology Brain Bank and Research CoRE at Mount Sinai Hospital. The permission to collect human brain material was obtained from the Ethical Committee of the VU University Medical Center, Amsterdam, The Netherlands, and the Mount Sinai Institutional Review Board.
- [MSBB study info](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/study_info/MSBB.md): The Mount Sinai Brain Bank (MSBB) cohort study generated large-scale matched multi-omics data in AD and control brains for exploring novel molecular underpinnings of AD.
- [ROSMAP study info](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/study_info/ROSMAP.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP): longitudinal clinical-pathologic cohort studies of aging and Alzheimer's disease run from Rush University, enrolling participants for longitudinal clinical analysis and brain donation.
- [STARNET study info](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/study_info/STARNET.md): STARNET is an RNA expression study of various disease-relevant tissues obtained from living patients with cardiovascular disease (CVD). The inclusion criterion for patients was eligibility for coronary artery by-pass graft (CABG) surgery.

### GWAS Summary Statistics (6 datasets)

- [ADGC GWAS imputation protocol](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/gwas/ADGC_GWAS_imputation_protocol.md): Adapted from [ADGC GWAS Data QC Protocol](https://bitbucket.org/wanpinglee_penn/gwas_qc/src/master/) to generate imputed genotype data for xQTL analysis in some cohorts.
- [AD GWAS integration (fine-mapping and colocalization)](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/gwas/AD_GWAS.md): Integrated fine-mapping and colocalization analyses of AD GWAS studies including Bellenguez 2022, Jansen 2019, Wightman 2021, and Kunkle 2019 using SuSiE-RSS and ColocBoost.
- [Alzheimer's Disease GWAS Summary Data (Bellenguez)](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/gwas/Bellenguez_AD.md): The SNP-level association testing summary statistics for Alzheimer's disease from Bellenguez et al 2022 Nature Genetics. This study uses UK Biobank (UKBB) proxy AD samples.
- [Alzheimer's Disease GWAS Summary Data (Jansen)](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/gwas/Jansen_AD.md): The SNP-level association testing summary statistics for Alzheimer's disease from Jansen et al 2021 Nature Genetics. This study uses proxy AD individuals from UK Biobank.
- [Alzheimer's Disease GWAS Summary Data (Kunkle)](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/gwas/Kunkle_AD.md): The SNP-level association testing summary statistics for Alzheimer's disease from Kunkle et al 2019 Nature Genetics. Position values were converted from hg19 to hg38 using liftOver.
- [Alzheimer's Disease GWAS Summary Data (Wightman)](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/gwas/Wightman_AD.md): The SNP-level association testing summary statistics for Alzheimer's disease from Wightman et al 2021 Nature Genetics. This file contains the meta-analyzed summary statistics of three cohorts: all individuals, all individuals excluding 23andMe, all individuals excluding 23andMe and UKBB.

### Omics Data (49 datasets)

**Gene Expression (13 datasets)**

- [Knight ADRC brain gene expression](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/expression/Knight_ADRC_brain_expression.md): Lead analysts: **Chunming Liu.**
- [MAGENTA African American blood gene expression](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/expression/MAGENTA_AA_blood_expression.md): Lead analysts: **Makaela Mews.**
- [MAGENTA Non-Hispanic White blood gene expression](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/expression/MAGENTA_NHW_blood_expression.md): Lead analysts: **Makaela Mews.**
- [MetaBrain multi-brain region gene expression](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/expression/MetaBrain_brain_expression.md): A large-scale meta-analysis of brain eQTL data across multiple brain regions and cohorts.
- [MiGA multi-brain region gene expression](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/expression/MiGA_brain_expression.md): A genetic and transcriptomic resource comprised of 255 primary human microglia samples isolated ex vivo from four different brain regions of 100 human subjects with neurodegenerative, neurological, or neuropsychiatric disorders, as well as unaffected controls.
- [MSBB brain gene expression](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/expression/MSBB_brain_expression.md): Lead analysts: **Minghui Wang.**
- [ROSMAP AC gene expression](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/expression/ROSMAP_AC_expression.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) anterior cingulate cortex (AC) gene expression.
- [ROSMAP DLPFC gene expression](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/expression/ROSMAP_DLPFC_expression.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) DLPFC gene expression.
- [ROSMAP PCC gene expression](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/expression/ROSMAP_PCC_expression.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) posterior cingulate cortex (PCC) gene expression.
- [ROSMAP microglia gene expression](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/expression/ROSMAP_microglia_expression.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) microglia RNA-seq dataset.
- [ROSMAP monocyte gene expression](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/expression/ROSMAP_monocyte_expression.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) monocyte RNA-seq dataset.
- [ROSMAP snRNA-seq pseudo-bulk gene expression](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/expression/ROSMAP_snRNAseq_pseudo_bulk.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) snRNA-seq pseudo-bulk gene expression from different cell types in Dorsolateral Prefrontal Cortex (DLPFC).
- [STARNET macrophage gene expression](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/expression/STARNET_macrophage.md): STARNET macrophage RNA expression from patients with cardiovascular disease.

**Alternative Splicing (8 datasets)**

- [Knight ADRC brain alternative splicing](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/splicing/Knight_ADRC_brain_splicing.md): Lead analysts: **Xuanhe Chen.**
- [MAGENTA African American blood alternative splicing](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/splicing/MAGENTA_AA_blood_splicing.md): Lead analysts: **Makaela Mews.**
- [MAGENTA Non-Hispanic White blood alternative splicing](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/splicing/MAGENTA_NHW_blood_splicing.md): Lead analysts: **Makaela Mews.**
- [MSBB brain alternative splicing](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/splicing/MSBB_brain_splicing.md): Lead analysts: **Minghui Wang.**
- [ROSMAP AC alternative splicing](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/splicing/ROSMAP_AC_splicing.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) AC alternative splicing.
- [ROSMAP DLPFC alternative splicing](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/splicing/ROSMAP_DLPFC_splicing.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) DLPFC alternative splicing.
- [ROSMAP PCC alternative splicing](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/splicing/ROSMAP_PCC_splicing.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) PCC alternative splicing.
- [ROSMAP snuc alternative splicing](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/splicing/ROSMAP_snuc_splicing.md): Single-nucleus sQTL data from ROSMAP using the ISSAC method (binomial GLMM with metacell-based approach for splice site usage quantification).

**Proteomics (5 datasets)**

- [EFIGA CSF proteomics](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/proteomics/EFIGA_CSF_proteomics.md): Lead analysts: **Zining Qi.**
- [Knight ADRC brain proteomics](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/proteomics/Knight_ADRC_brain_proteomics.md): Charles F. And Joanne Knight Alzheimer's Disease Research Center (Knight-ADRC).
- [Knight ADRC CSF proteomics](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/proteomics/Knight_ADRC_CSF_proteomics.md): Lead analysts: **Zining Qi.**
- [MSBB brain proteomics](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/proteomics/MSBB_proteomics.md): Lead analysts: **Minghui Wang.**
- [ROSMAP DLPFC protein expression](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/proteomics/ROSMAP_DLPFC_proteomics.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) DLPFC protein expression (TMT mass spectrometry).

**Glycoproteomics (1 dataset)**

- [ROSMAP DLPFC glycoproteomics](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/glycoproteomics/ROSMAP_DLPFC_glycoproteomics.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) DLPFC glycoprotein expression dataset.

**DNA Methylation (3 datasets)**

- [Knight ADRC brain methylation](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/methylation/Knight_ADRC_brain_methylation.md): Lead analysts: **Alexandre Pelletier.**
- [MSBB brain methylation](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/methylation/MSBB_brain_methylation.md): Lead analysts: **Alexandre Pelletier.**
- [ROSMAP DLPFC methylation](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/methylation/ROSMAP_DLPFC_methylation.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) DLPFC DNA methylation dataset.

**Histone ChIP-seq (1 dataset)**

- [ROSMAP DLPFC H3K9ac ChIP-seq](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/histone_ChIPSeq/ROSMAP_DLPFC_ChIPSeq_H3K9ac.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) H3K9ac histone acetylation ChIP-seq dataset.

**snATAC-seq (1 dataset)**

- [ROSMAP snuc chromatin accessibility (snATAC-seq)](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/snATAC/ROSMAP_snuc_caQTL.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) single-nucleus ATAC-seq dataset for chromatin accessibility QTL analysis.

**Metabolomics (5 datasets)**

- [EFIGA plasma metabolomics](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/metabolomics/EFIGA_plasma_metabolomics.md): Lead analysts: **Zining Qi.**
- [Knight ADRC brain metabolomics](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/metabolomics/Knight_ADRC_brain_metabolomics.md): Lead analysts: **Zining Qi.**
- [Knight ADRC CSF metabolomics](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/metabolomics/Knight_ADRC_CSF_metabolomics.md): Lead analysts: **Zining Qi.**
- [ROSMAP DLPFC metabolomics](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/metabolomics/ROSMAP_DLPFC_metabolomics.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) DLPFC metabolomics dataset.
- [WHICAP (pilot) plasma metabolomics](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/metabolomics/WHICAP_plasma_metabolomics.md): Lead analysts: **Zining Qi.**

**Single-nucleus RNA-seq (3 datasets)**

- [ROSMAP snuc RNA-seq (CUIMC cohort)](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/snRNA_seq/ROSMAP_snuc_CUIMC1.md): ROSMAP single-nucleus RNA-seq data from the Columbia University Irving Medical Center (CUIMC) cohort used for cell-type-resolved eQTL and scEEMs analyses.
- [ROSMAP snuc RNA-seq (MIT cohort)](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/snRNA_seq/ROSMAP_snuc_MIT.md): ROSMAP single-nucleus RNA-seq data from the MIT cohort used for cell-type-resolved eQTL and scEEMs analyses.
- [ROSMAP snuc RNA-seq (mega cohort)](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/snRNA_seq/ROSMAP_snuc_mega.md): Mega-cohort single-nucleus RNA-seq combining CUIMC and MIT ROSMAP data for large-scale cell-type-specific eQTL analyses.

**Genotype (8 datasets)**

- [EFIGA genotype data](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/genotype/EFIGA_genotype.md): Lead analysts: **Zining Qi.**
- [Knight ADRC genotype data](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/genotype/Knight_ADRC_genotype.md): Lead analysts: **Zining Qi.**
- [MAGENTA genotype data](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/genotype/MAGENTA_genotype.md): Lead analysts: **Makaela Mews.**
- [MiGA genotype data](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/genotype/MiGA_genotype.md): Microglia Genomic Atlas genotype data from the Netherlands Brain Bank (NBB) and the Neuropathology Brain Bank and Research CoRE at Mount Sinai Hospital.
- [MSBB WGS data](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/genotype/MSBB_WGS.md): Mount Sinai Brain Bank whole-genome sequence data.
- [ROSMAP WGS data](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/genotype/ROSMAP_WGS.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) whole-genome sequence data.
- [STARNET genotype data](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/genotype/STARNET_genotype.md): STARNET genotype data from patients with cardiovascular disease.
- [WHICAP genotype data](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/genotype/WHICAP_genotype.md): Lead analysts: **Zining Qi.**

**Covariates (1 dataset)**

- [ROSMAP covariates data](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/omics/covariates/ROSMAP_covariates.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) covariates dataset for xQTL analysis.

### QTL Results (38 datasets)

**Expression QTLs — eQTL (13 datasets)**

- [FunGen-xQTL protocol data](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/FunGen_xQTL_protocol_data.md): A toy dataset consisting of 49 de-identified samples from ROSMAP, used to illustrate the computational protocols for molecular QTL detection and analysis.
- [Knight ADRC brain gene expression QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/eQTL/Knight_ADRC_brain_expression_qtl.md): Lead analysts: **Chunming Liu.**
- [MAGENTA African American blood gene expression QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/eQTL/MAGENTA_AA_blood_expression_qtl.md): Multi-Ancestry Genomics, Epigenomics, and Transcriptomics of Alzheimer's (MAGENTA) Project, African American cohort. Lead analysts: **Makaela Mews.**
- [MAGENTA Non-Hispanic White blood gene expression QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/eQTL/MAGENTA_NHW_blood_expression_qtl.md): Multi-Ancestry Genomics, Epigenomics, and Transcriptomics of Alzheimer's (MAGENTA) Project, Non-Hispanic White cohort. Lead analysts: **Makaela Mews.**
- [MetaBrain multi-brain region gene expression QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/eQTL/MetaBrain_brain_expression_qtl.md): Large-scale brain eQTL meta-analysis across multiple brain regions and cohorts.
- [MiGA multi-brain region gene expression QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/eQTL/MiGA_brain_expression_qtl.md): A genetic and transcriptomic resource comprised of 255 primary human microglia samples isolated ex vivo from four different brain regions of 100 human subjects.
- [MSBB brain gene expression QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/eQTL/MSBB_brain_expression_qtl.md): Lead analysts: **Minghui Wang.**
- [ROSMAP AC gene expression QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/eQTL/ROSMAP_AC_expression_qtl.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) AC gene expression QTL.
- [ROSMAP DLPFC gene expression QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/eQTL/ROSMAP_DLPFC_expression_qtl.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) DLPFC gene expression QTL.
- [ROSMAP PCC gene expression QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/eQTL/ROSMAP_PCC_expression_qtl.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) PCC gene expression QTL.
- [ROSMAP microglia gene expression QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/eQTL/ROSMAP_microglia_expression_qtl.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) microglia eQTL dataset.
- [ROSMAP monocyte gene expression QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/eQTL/ROSMAP_monocyte_expression_qtl.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) monocyte eQTL dataset.
- [ROSMAP snRNA-seq pseudo-bulk gene expression QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/eQTL/ROSMAP_snRNAseq_pseudo_bulk_qtl.md): Cell-type-specific eQTLs from ROSMAP DLPFC snRNA-seq pseudo-bulk data, analyzed using scEEMs (CatBoost ML model for cell-type-resolved eQTL prediction) and SuSiE fine-mapping.
- [STARNET macrophage gene expression QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/eQTL/STARNET_macrophage_qtl.md): STARNET macrophage eQTL from patients with cardiovascular disease.

**Splicing QTLs — sQTL (8 datasets)**

- [Knight ADRC brain alternative splicing QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/sQTL/Knight_ADRC_brain_splicing_qtl.md): Lead analysts: **Xuanhe Chen.**
- [MAGENTA African American blood alternative splicing QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/sQTL/MAGENTA_AA_blood_splicing_qtl.md): Lead analysts: **Makaela Mews.**
- [MAGENTA Non-Hispanic White blood alternative splicing QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/sQTL/MAGENTA_NHW_blood_splicing_qtl.md): Lead analysts: **Makaela Mews.**
- [MSBB brain alternative splicing QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/sQTL/MSBB_brain_splicing_qtl.md): Lead analysts: **Minghui Wang.**
- [ROSMAP AC alternative splicing QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/sQTL/ROSMAP_AC_splicing_qtl.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) AC sQTL.
- [ROSMAP DLPFC alternative splicing QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/sQTL/ROSMAP_DLPFC_splicing_qtl.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) DLPFC sQTL.
- [ROSMAP PCC alternative splicing QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/sQTL/ROSMAP_PCC_splicing_qtl.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) PCC sQTL.
- [ROSMAP snuc alternative splicing QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/sQTL/ROSMAP_snuc_splicing_qtl.md): Single-nucleus sQTL from ROSMAP using the ISSAC method (binomial GLMM, metacell-based approach, junctools splice site quantification).

**Protein QTLs — pQTL (5 datasets)**

- [EFIGA CSF proteomics QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/pQTL/EFIGA_CSF_proteomics_qtl.md): Lead analysts: **Zining Qi.**
- [Knight ADRC brain proteomics QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/pQTL/Knight_ADRC_brain_proteomics_qtl.md): Charles F. And Joanne Knight Alzheimer's Disease Research Center (Knight-ADRC).
- [Knight ADRC CSF proteomics QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/pQTL/Knight_ADRC_CSF_proteomics_qtl.md): Lead analysts: **Zining Qi.**
- [MSBB brain proteomics QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/pQTL/MSBB_proteomics_qtl.md): Lead analysts: **Minghui Wang.**
- [ROSMAP DLPFC protein expression QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/pQTL/ROSMAP_DLPFC_proteomics_qtl.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) DLPFC proteomics QTL.

**Glycosylation QTLs — gpQTL (1 dataset)**

- [ROSMAP DLPFC glycoproteomics QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/gpQTL/ROSMAP_DLPFC_glycoproteomics_qtl.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) DLPFC glycoproteomics QTL.

**Methylation QTLs — mQTL (3 datasets)**

- [Knight ADRC brain methylation QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/mQTL/Knight_ADRC_brain_methylation_qtl.md): Lead analysts: **Alexandre Pelletier.**
- [MSBB brain methylation QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/mQTL/MSBB_brain_methylation_qtl.md): Lead analysts: **Alexandre Pelletier.**
- [ROSMAP DLPFC methylation QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/mQTL/ROSMAP_DLPFC_methylation_qtl.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) DLPFC mQTL.

**Histone Acetylation QTLs — haQTL (1 dataset)**

- [ROSMAP DLPFC H3K9ac QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/haQTL/ROSMAP_DLPFC_ChIPSeq_H3K9ac_qtl.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) H3K9ac QTL analysis using the FGC xQTL pipeline.

**Chromatin Accessibility QTLs — caQTL (1 dataset)**

- [ROSMAP snuc chromatin accessibility QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/caQTL/ROSMAP_snuc_caQTL_qtl.md): Single-nucleus chromatin accessibility QTL from ROSMAP DLPFC using snATAC-seq, with pairwise SuSiE-COLOC colocalization against eQTLs.

**Metabolome QTLs — metaQTL (5 datasets)**

- [EFIGA plasma metabolomics QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/metaQTL/EFIGA_plasma_metabolomics_qtl.md): Lead analysts: **Zining Qi.**
- [Knight ADRC brain metabolomics QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/metaQTL/Knight_ADRC_brain_metabolomics_qtl.md): Lead analysts: **Zining Qi.**
- [Knight ADRC CSF metabolomics QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/metaQTL/Knight_ADRC_CSF_metabolomics_qtl.md): Lead analysts: **Zining Qi.**
- [ROSMAP DLPFC metabolomics QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/metaQTL/ROSMAP_DLPFC_metabolomics_qtl.md): Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) DLPFC metabolomics QTL.
- [WHICAP (pilot) plasma metabolomics QTL](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/qtl/metaQTL/WHICAP_plasma_metabolomics_qtl.md): Lead analysts: **Zining Qi.**

### Reference Data (1 dataset)

- [Non-Hispanic White Linkage Disequilibrium Reference Panel](https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/reference_data/ld_reference.md): LD matrices calculated from whole genome sequencing data from 16,905 non-Hispanic White individuals from the Alzheimer's Disease Sequencing Project (ADSP). Correlation matrices were calculated between SNPs within 1361 LD blocks. Provides improved coverage of low-frequency variants for fine-mapping relative to 1000 Genomes reference panels ([syn69670651](https://www.synapse.org/Synapse:syn69670651), [syn69670652](https://www.synapse.org/Synapse:syn69670652)).

## Repository Structure

```
.
├── content/                  # Source markdown files
│   ├── xqtl-data/           # xQTL datasets
│   │   ├── study_info/      # Study descriptions (6 cohorts)
│   │   ├── gwas/            # GWAS summary statistics (6 datasets)
│   │   ├── omics/           # Omics data (49 datasets)
│   │   │   ├── expression/      # Bulk & pseudo-bulk RNA-seq
│   │   │   ├── splicing/        # Alternative splicing
│   │   │   ├── proteomics/      # Protein expression (TMT MS)
│   │   │   ├── glycoproteomics/ # Glycoprotein expression
│   │   │   ├── methylation/     # DNA methylation (RRBS/WGBS)
│   │   │   ├── histone_ChIPSeq/ # H3K9ac ChIP-seq
│   │   │   ├── snATAC/          # Single-nucleus ATAC-seq
│   │   │   ├── metabolomics/    # Brain, CSF, and plasma metabolomics
│   │   │   ├── snRNA_seq/       # Single-nucleus RNA-seq
│   │   │   ├── genotype/        # WGS genotype data
│   │   │   └── covariates/      # Covariate files
│   │   ├── qtl/             # QTL results (38 datasets)
│   │   │   ├── eQTL/            # Expression QTLs (13 datasets)
│   │   │   ├── sQTL/            # Splicing QTLs (8 datasets)
│   │   │   ├── pQTL/            # Protein QTLs (5 datasets)
│   │   │   ├── gpQTL/           # Glycosylation QTLs (1 dataset)
│   │   │   ├── mQTL/            # Methylation QTLs (3 datasets)
│   │   │   ├── haQTL/           # Histone acetylation QTLs (1 dataset)
│   │   │   ├── caQTL/           # Chromatin accessibility QTLs (1 dataset)
│   │   │   └── metaQTL/         # Metabolome QTLs (5 datasets)
│   │   └── reference_data/  # LD reference panels (1 dataset)
│   └── *.md                 # Documentation pages
├── scripts/                  # Processing scripts
│   └── hugo_generator.py
└── website/                  # Generated Hugo site (git-ignored)
```

## Contributing

To add or update content:
1. Edit markdown files in `content/` directory
2. Run `make` or `python scripts/hugo_generator.py --serve` to preview locally
3. Submit a pull request

The `website/` directory is automatically generated and should not be edited directly.

## Building the Site

```bash
# Install Hugo (https://gohugo.io/getting-started/installing/)
# Then run:

# Generate and serve locally
python scripts/hugo_generator.py --serve

# Build for production
python scripts/hugo_generator.py --build --minify
```
