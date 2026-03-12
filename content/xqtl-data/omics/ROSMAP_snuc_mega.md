# ROSMAP Mega snRNA-seq expression
Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) mega-analysis combining single-nucleus RNA-seq data from CUIMC and MIT.

Please refer to [this document](../study_info/ROSMAP) for an overview of the ROSMAP project.

## Contact
Anjing Liu

Contact Affiliation : Columbia University

Contact Role : Anjing Liu performed pseudo-bulk expression preprocessing and QTL analysis for the combined mega dataset

## Study Overview
Grant number : U01AG061356, RF1AG057473, U01AG046152, R01AG066831, U01AG072572, AG058002, AG062377, NS110453, NS115064, AG062335, AG074003, NS127187, MH119509, HG008155, RF1AG062377, RF1AG054321, RO1AG054012, GM087237, P30AG10161, P30AG72975, R01AG15819, R01AG17917, U01AG46152, U01AG61356

Publication : PMID: 38514782, PMID: 39048816, PMID: 37774677, PMID: 40060644

Acknowledgement : Study data were generated from postmortem brain tissue provided by the Religious Orders Study and Rush Memory and Aging Project (ROSMAP) cohort at Rush Alzheimer's Disease Center, Rush University Medical Center, Chicago. This work was funded by NIH grants U01AG061356 (De Jager/Bennett), RF1AG057473 (De Jager/Bennett), and U01AG046152 (De Jager/Bennett) as part of the AMP-AD consortium, as well as NIH grants R01AG066831 (Menon) and U01AG072572 (De Jager/St George-Hyslop). The results published here are in whole or in part based on data obtained from the AD Knowledge Portal (https://adknowledgeportal.org/). This work was also supported in part by the Cure Alzheimer's Fund, NIH grants AG058002, AG062377, NS110453, NS115064, AG062335, AG074003, NS127187, MH119509, HG008155 (M.K.), RF1AG062377, RF1AG054321, RO1AG054012 (L.-H.T.) and the NIH training grant GM087237 (to C.A.B.). ROSMAP is supported by P30AG10161, P30AG72975, R01AG15819, R01AG17917, U01AG46152, U01AG61356.

Study name : ROSMAP Mega snRNA-seq expression

Study Description : Mega-analysis combining single-nucleus RNA-seq data from the CUIMC (De Jager lab) and MIT (Kellis lab) ROSMAP datasets. The merged dataset integrates nuclei from DLPFC/PFC postmortem brain tissue across a total of approximately 848 ROSMAP donors (with overlapping donors harmonized). This larger combined resource increases statistical power for cell-type-specific cis-eQTL discovery. Cell types covered: Astrocytes (Ast), Excitatory neurons (Exc), Inhibitory neurons (Inh), Microglia (Mic), Oligodendrocytes (Oli), and Oligodendrocyte progenitor cells (OPC). Pseudo-bulk expression matrices were generated per cell type for use in cis-eQTL analysis.

Disease : Alzheimer's Disease

Data Citation : Omics data: https://www.synapse.org/Synapse:syn31512863 (CUIMC), https://www.synapse.org/Synapse:syn52293417 (MIT)

Genetics data: https://dss.niagads.org/datasets/ng00067/

Genetics Publication : PMID: 40407102

PIs : Phil De Jager (Columbia University) and Manolis Kellis (Massachusetts Institute of Technology)

## Dataset Description

### Raw data

Nuclei were isolated from DLPFC/PFC postmortem brain tissue of ROSMAP participants from two complementary datasets: the CUIMC dataset (424 donors, De Jager lab; Synapse [syn31512863](https://www.synapse.org/Synapse:syn31512863)) and the MIT dataset (427 donors, Kellis lab; Synapse [syn52293417](https://www.synapse.org/Synapse:syn52293417)). Overlapping donors between the two datasets were identified and handled appropriately during harmonization. Single-nucleus RNA-seq was performed using the 10x Genomics Chromium platform in both studies. Raw reads were aligned to the GRCh38 reference genome following the respective lab preprocessing workflows.

### Molecular phenotype matrices

Pseudo-bulk count matrices were independently generated for each dataset by aggregating UMI counts across nuclei within each cell type per donor. The two datasets were then harmonized and merged to produce a unified mega pseudo-bulk expression matrix for each of the six major cell types: Astrocytes (Ast), Excitatory neurons (Exc), Inhibitory neurons (Inh), Microglia (Mic), Oligodendrocytes (Oli), and Oligodendrocyte progenitor cells (OPC).

### Phenotype preprocessing

Pseudo-bulk expression matrices from both datasets were normalized and filtered following standard pipelines prior to merging. Batch effects between the CUIMC and MIT datasets were accounted for during covariate modeling. Covariates for eQTL analysis include sex, age at death, postmortem interval (PMI), study (ROS or MAP), dataset (CUIMC or MIT), total genes detected, top genotype principal components, and expression principal components.

## Analysis Status

Pseudo-bulk expression preprocessing: Finished.
