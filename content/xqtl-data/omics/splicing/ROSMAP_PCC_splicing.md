---
type: omics
modality: splicing
short_title: ROSMAP PCC
cohort: ROSMAP
context: PCC
access: controlled
status: staged
synapse_ids: [syn3157322, syn3388564, syn69670592, syn69670597, syn69670600, syn69670630, syn69865816]
lead_analysts: [Frank Grenn]
last_verified:
---

# ROSMAP PCC alternative splicing 

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) PCC alternative splicing. 

## Contact 

Frank Grenn

## Study Overview

- Study information: [study_info/ROSMAP.md](../../study_info/ROSMAP.md)
- Website&Logo : [https://www.synapse.org/#!Synapse:syn3157322](https://www.synapse.org/#!Synapse:syn3157322)

## Dataset Details

### Molecular phenotype matrices

1. Columns are sample names and rows are introns. Contains each type of intron usage ratio under each sample (#particular intron in a sample / #total introns classified in the same cluster in a sample).
2. 535 columns (including index) and 389332 rows (including header)

1. Columns are sample names and rows are introns. Contains each type of intron usage count under each sample (#particular intron in a sample).
2. 535 columns (including index) and 389332 rows (including header)

## Links to omics data analysis notebooks

Analysis notebook generation in progress and will be uploaded to [https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Zhang_BU/PCC_AC](https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Zhang_BU/PCC_AC). Steps will be similar to what is found in [https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Zhang_BU/ROSMAP_DLPFC](https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Zhang_BU/ROSMAP_DLPFC).

## Study Metadata

- **PI**: David A. Bennett (Rush University Medical Center, Chicago, IL, USA)
- **Grant numbers**: U01AG046152, R01AG048015, U01AG061356, R01AG15819, U01AG061359
- **Publication**: PMID: 30084846
- **Genetics publication**: PMID: 40407102
- **Acknowledgement**: Study data were generated from postmortem brain tissue provided by the Religious Orders Study and Rush Memory and Aging Project (ROSMAP) cohort at Rush Alzheimer's Disease Center, Rush University Medical Center, Chicago.
- **Omics data**: [syn3388564](https://www.synapse.org/Synapse:syn3388564)
- **Genetics data**: [ng00067](https://dss.niagads.org/datasets/ng00067/)
## QTL Analysis
QTL analysis for this dataset is documented in [../../qtl/sQTL/ROSMAP_PCC_splicing_qtl.md](../../qtl/sQTL/ROSMAP_PCC_splicing_qtl.md).

Flagship paper analyses:
- Fine-mapping (SuSiE-RSS): [syn69670592](https://www.synapse.org/Synapse:syn69670592)
- TWAS weight models: [syn70094771](https://www.synapse.org/Synapse:syn70094771) (this dataset's folder; all models are in [syn69670600](https://www.synapse.org/Synapse:syn69670600))
- Quantile TWAS (qTWAS) models: not available yet
- Multi-context colocalization (ColocBoost): [syn69670597](https://www.synapse.org/Synapse:syn69670597)
- AD GWAS–xQTL colocalization results: [syn69865816](https://www.synapse.org/Synapse:syn69865816)
- AD GWAS–xQTL colocalization models: [syn69670630](https://www.synapse.org/Synapse:syn69670630)
