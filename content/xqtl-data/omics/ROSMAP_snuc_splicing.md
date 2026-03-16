# ROSMAP snRNA-seq Splicing (ISSAC)

Single-nucleus RNA-seq splicing QTL analysis using the ISSAC (Integrative Single-cell Splicing Analysis with Context) method, applied to harmonized CUIMC and MIT single-nucleus data from ROSMAP DLPFC.

Please refer to [this document](../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Contact

FunGen-xQTL Analysis Working Group

## Study Overview

- **PI**: Phil De Jager (Columbia University) and Manolis Kellis (Massachusetts Institute of Technology)
- **Grant numbers**: U01AG061356, RF1AG057473, U01AG046152, R01AG066831, U01AG072572, AG058002, AG062377, NS110453, NS115064, AG062335, AG074003, NS127187, MH119509, HG008155, RF1AG062377, RF1AG054321, RO1AG054012, GM087237, P30AG10161, P30AG72975, R01AG15819, R01AG17917, U01AG46152, U01AG61356
- **Publication**: PMID: 38514782, PMID: 39048816, PMID: 37774677, PMID: 40060644
- **Genetics publication**: PMID: 40407102
- **Acknowledgement**: Study data were generated from postmortem brain tissue provided by the Religious Orders Study and Rush Memory and Aging Project (ROSMAP) cohort at Rush Alzheimer's Disease Center, Rush University Medical Center, Chicago. This work was funded by NIH grants U01AG061356 (De Jager/Bennett), RF1AG057473 (De Jager/Bennett), and U01AG046152 (De Jager/Bennett) as part of the AMP-AD consortium, as well as NIH grants R01AG066831 (Menon) and U01AG072572 (De Jager/St George-Hyslop). This work was also supported in part by the Cure Alzheimer's Fund, NIH grants AG058002, AG062377, NS110453, NS115064, AG062335, AG074003, NS127187, MH119509, HG008155 (M.K.), RF1AG062377, RF1AG054321, RO1AG054012 (L.-H.T.) and the NIH training grant GM087237 (to C.A.B.). ROSMAP is supported by P30AG10161, P30AG72975, R01AG15819, R01AG17917, U01AG46152, U01AG61356.
- **Omics data**: [syn31512863](https://www.synapse.org/Synapse:syn31512863) (CUIMC), [syn52293417](https://www.synapse.org/Synapse:syn52293417) (MIT)
- **Genetics data**: [ng00067](https://dss.niagads.org/datasets/ng00067/)
- **Disease**: Alzheimer's Disease

## Dataset Details

### Cohort and Sample Overview

This study utilized single-nucleus RNA sequencing data from the dorsolateral prefrontal cortex (DLPFC, Brodmann Area 9) of post-mortem human brain tissue from two cohorts as part of the FunGen-xQTL harmonized aging brain resource project:

- **CUIMC cohort** (Columbia University Irving Medical Center, also known as CUIMC1 or CUMC): 424 donors
- **MIT cohort**: 298 donors
- **Shared donors**: 192 donors shared between cohorts
- **Total**: 530 unique donors across 722 specimens
- **Final nuclei after QC**: 3,177,748 high-quality nuclei

### Sample Processing

**CUIMC cohort:** Dorsolateral prefrontal cortex tissue specimens were received frozen and processed on ice. Gray matter was carefully dissected to remove white matter and meninges when present. Approximately 50–100 mg of gray matter tissue was transferred into a dounce homogenizer with 2 mL of NP40 Lysis Buffer (0.1% NP40, 10 mM Tris, 146 mM NaCl, 1 mM CaCl2, 21 mM MgCl2, 40 U/mL of RNase inhibitor). Tissue was gently dounced on ice 25 times with Pestle A followed by 25 times with Pestle B, then transferred to a 15 mL conical tube. 3 mL of PBS + 0.01% BSA and 40 U/mL of RNase inhibitor were added for a final volume of 5 mL and immediately centrifuged at 500g for 5 min at 4°C. Nuclei pellets were resuspended in 500 µL of PBS + 0.01% BSA and 40 U/mL of RNase inhibitor and filtered through 20 µm pre-separation filters.

**MIT cohort:** Single nuclei were isolated from frozen tissue following the DroNc-seq protocol (Habib et al. 2017) modified to work on the 10x Genomics Chromium platform.

### Library Batching and Preparation

**CUIMC cohort:** Approximately 5,000 nuclei from each of 8 participants were pooled into one sample (40,000 nuclei total). Libraries were generated from pooled samples: 222 libraries contained samples from 8 donors each; 4 libraries from 7 donors each; and 8 libraries from a single donor each. Libraries were created as two replicates (e.g., B10-A and B10-B), each sequenced twice at different sequencing centers (Broad Institute and NYGC). The pooled nuclei were run on the 10x Genomics Single Cell RNA-Seq Platform using Chromium Single Cell 3' Reagent Kits version 3.

**MIT cohort:** Nuclei from individual samples were loaded on a single channel on the 10x Genomics Chromium chip. Library construction was performed per the Chromium Single Cell 3' Reagent Kit v2 protocol (CG00052).

### Sequencing

**CUIMC:** Libraries from 4 channels were pooled and sequenced on 1 lane of Illumina HiSeqX at the Broad Institute's Genomics Platform or NYGC, targeting approximately 1 million reads per channel.

**MIT:** Sequenced on Illumina HiSeq4000 using paired-end sequencing: Read 1 (UMI + 10x barcode) – 26 cycles; i7 sample index – 8 cycles; Read 2 (transcript) – 98 cycles.

### Data Processing

Raw sequencing reads were processed using CellRanger (v3.0 or later) and aligned to GRCh38 (hg38). Nuclei with fewer than 400 detected genes were excluded. Doublets were identified and removed. The two cohorts were integrated using Harmony batch correction. The final dataset comprised 3,177,748 high-quality nuclei.

### Demultiplexing (CUIMC Pooled Libraries)

Because CUIMC libraries consisted of pooled nuclei from eight individuals, original individuals were inferred from SNPs in snRNA-seq reads. When all eight individuals were genotyped, **demuxlet** was used. When fewer were genotyped, **freemuxlet** was used to cluster droplets into 8 groups, with snRNA-seq-based genotypes compared to WGS using `bcftools gtcheck`.

### Cell Type Annotation

Nuclei were annotated into **7 major cell types**: excitatory neurons, inhibitory neurons, astrocytes, oligodendrocytes, oligodendrocyte progenitor cells (OPC), microglia, and endothelial cells. Further refinement produced **95 subcell types**, of which **67 with >3,000 cells** were retained for sQTL analysis.

### Metacell Generation (ISSAC)

ISSAC's metacell generation module aggregates single nuclei into metacells while preserving cell-state heterogeneity. PCA was performed per donor and cell type, followed by KNN graph construction in PC space and Louvain clustering. Total: **23,143 metacells** for 7 major cell types; **87,936 metacells** for 67 subcell types.

### Splice Site Usage Quantification (ISSAC junctools)

ISSAC's `junctools` module extracts junction reads from aligned BAM files, collapsing PCR duplicates using both cell barcode and UMI information. For each junction, UMI-collapsed read counts are calculated. The splice site usage ratio is calculated as the proportion of reads utilizing the target site relative to total supporting and competing reads. Intron retention events are also incorporated. This approach is robust to 5'/3' read bias in droplet-based data.

### sQTL Mapping (Binomial Mixed-Effect Model)

ISSAC employs a generalized linear mixed-effect model (GLMM) with binomial response distribution for sQTL mapping. Fixed effects include sex, age, genotype PCs, and PEER factors. Random effects are modeled via a genetic relationship matrix (GRM) accounting for repeated metacell measurements and population relatedness. Parameter estimation uses penalized quasi-likelihood (PQL) with restricted maximum likelihood (REML) and preconditioned conjugate gradient (PCG) approximation for scalability. Single-variant score tests are performed for cis-variants within ±1 Mb. Multiple testing correction uses FDR < 0.05.

Context-dependent sQTL analyses include:
- **AD-biased sQTLs**: genotype-by-AD interaction term; FDR < 0.01
- **Sex-biased sQTLs**: genotype-by-sex interaction term; FDR < 0.05
- **Cell state-dependent sQTLs**: genotype-by-PC interaction terms; metacells stratified into tertiles

### Colocalization

Colocalization with GWAS loci for six neurological traits (Alzheimer's disease, ALS, Parkinson's disease, Schizophrenia, Lewy body dementia, Neuroticism) was performed using the COLOC method (H4 > 0.75 = strong colocalization). SMR was used as orthogonal validation. S-LDSC estimated heritability enrichment of cell type-specific sGenes.

### Software

ISSAC is implemented in C++ (sQTL mapping) with Python (metacell generation). Cell type annotation used Seurat (v4.0+) and Scanpy (v1.8+). Batch integration used Harmony. Statistical analyses used R (v4.0+) and Python (v3.7+).

## QTL Analysis

QTL analysis for this dataset is documented in [../qtl/ROSMAP_snuc_splicing_qtl.md](../qtl/ROSMAP_snuc_splicing_qtl.md).

Flagship paper analyses:
- Fine-mapping (SuSiE-RSS): [syn69670592](https://www.synapse.org/Synapse:syn69670592)
- TWAS weight models: [syn69670600](https://www.synapse.org/Synapse:syn69670600)
- Quantile TWAS (qTWAS) models: [syn69670611](https://www.synapse.org/Synapse:syn69670611)
- Multi-context colocalization (ColocBoost): [syn69670597](https://www.synapse.org/Synapse:syn69670597)
- AD GWAS–xQTL colocalization results: [syn69865816](https://www.synapse.org/Synapse:syn69865816)
- AD GWAS–xQTL colocalization models: [syn69670630](https://www.synapse.org/Synapse:syn69670630)
