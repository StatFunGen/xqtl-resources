# ROSMAP RNA-seq monocyte gene expression

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) monocyte data-set. 

Please refer to [this document](../../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Contact

Travyse Edwards

## Data descriptions

The ROSMAP monocyte data on MSSM were downloaded from [syn22024496](https://www.synapse.org/#!Synapse:syn22024496) on July 11th, 2022. (path on MSSM to be added)

- Path on MSSM cluster `/sc/arion/projects/load/data-ext/ROSMAP/raw/rnaseq_monocytes_syn23650893/Gene_Expression-RNA-seq-monocyte`

### Preview Monocyte Gene Expression Data

Over all 615 samples in the dataset, 302 samples have diagnosis meta data, 1 sample missing associated sex meta data.

These samplesa ll share the same `library preparation method` and are not `multi-specimen` samples. However, there is variety in `read length`, `sex`, and `platform`. It may be worthwhile to use these as covariates in the downstream analyses. I will remove the two samples that are missing sex information (though I can just impute the sex).

The biospecimen file identifies the individuals that have SNP array data, Whole Genome Sequencing data, or both available. An overlapping check confirmed the monocyte gene expression contains a mix of SNP array and whole genome sequencing data (with a lot of overlap between the two). With in the 614 samples for which we have the expression data for, 246 are overlapped with WGS, 313 are overlapped with SNP array and 239 are overlapped with joint-call WGS.

## Study Metadata

- **PI**: David A. Bennett (Rush University Medical Center, Chicago, IL, USA)
- **Grant numbers**: U01AG046152, R01AG048015, U01AG061356, R01AG15819, U01AG061359
- **Publication**: PMID: 30084846
- **Genetics publication**: PMID: 40407102
- **Acknowledgement**: Study data were generated from postmortem brain tissue provided by the Religious Orders Study and Rush Memory and Aging Project (ROSMAP) cohort at Rush Alzheimer's Disease Center, Rush University Medical Center, Chicago.
- **Omics data**: [syn22024496](https://www.synapse.org/Synapse:syn22024496)
- **Genetics data**: [ng00067](https://dss.niagads.org/datasets/ng00067/)
## QTL Analysis
QTL analysis for this dataset is documented in [../../qtl/eQTL/ROSMAP_monocyte_expression_qtl.md](../../qtl/eQTL/ROSMAP_monocyte_expression_qtl.md).

Flagship paper analyses:
- Fine-mapping (SuSiE-RSS): [syn69670592](https://www.synapse.org/Synapse:syn69670592)
- TWAS weight models: [syn69670600](https://www.synapse.org/Synapse:syn69670600)
- Quantile TWAS (qTWAS) models: [syn69670611](https://www.synapse.org/Synapse:syn69670611)
- Multi-context colocalization (ColocBoost): [syn69670597](https://www.synapse.org/Synapse:syn69670597)
- AD GWAS–xQTL colocalization results: [syn69865816](https://www.synapse.org/Synapse:syn69865816)
- AD GWAS–xQTL colocalization models: [syn69670630](https://www.synapse.org/Synapse:syn69670630)
