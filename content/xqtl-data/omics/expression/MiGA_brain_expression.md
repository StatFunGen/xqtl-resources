---
type: omics
modality: expression
short_title: MiGA microglia
cohort: MiGA
context: "microglia, 4 regions"
sample_size:
access: controlled
status: staged
release:
synapse_ids: [syn69670592, syn69670597, syn69670600, syn69670611, syn69670630, syn69865816]
lead_analysts: [Travyse Edwards]
last_verified:
---

# MiGA multi-brain region gene expression

A genetic and transcriptomic resource comprised of 255 primary human microglia samples isolated ex vivo from four different brain regions of 100 human subjects with neurodegenerative, neurological, or neuropsychiatric disorders, as well as unaffected controls.

The human post-mortem brain samples were obtained from the Netherlands Brain Bank (NBB) and the Neuropathology Brain Bank and Research CoRE at Mount Sinai Hospital. The permission to collect human brain material was obtained from the Ethical Committee of the VU University Medical Center, Amsterdam, The Netherlands, and the Mount Sinai Institutional Review Board. For the Netherlands Brain bank, informed consent for autopsy, the use of brain tissue and accompanied clinical information for research purposes was obtained per donor ante-mortem.

## Contact

Travyse Edwards

## Study Overview

- Study information: `descriptor/study_info/MiGA.md`.
- Website&Logo : https://dss.niagads.org/sample-sets/snd10022/

## Dataset Description

### Raw data

- https://dss.niagads.org/datasets/ng00105/
- https://dss.niagads.org/studies/sa000018/


### Molecular phenotype matrices

We have gene expression data for four brain regions: medial frontal gyrus (GFM), superior temporal gyrus (GTS), thalamus (THA), and subventricular zone (SVZ). I have included information about the TPM matrices below for each brain region. The columns are sample names and the rows are gene ids. 

- GFM
  - File: `sample-gfm.trimmed.clean.rnaseqc.low_expression_filtered.outlier_removed.tpm.gct.gz`
  - Columns: 75, Rows: 45814
- GTS
  - File: `sample-gts.trimmed.clean.rnaseqc.low_expression_filtered.outlier_removed.tpm.gct.gz`
  - Columns: 63, Rows: 45472
- THA
  - File: `sample-tha.trimmed.clean.rnaseqc.low_expression_filtered.outlier_removed.tpm.gct.gz`
  - Columns: 61, Rows: 45461
- SVZ
  - File: `sample-svz.trimmed.clean.rnaseqc.low_expression_filtered.outlier_removed.tpm.gct.gz`
  - Columns: 53, Rows: 42086

File Sizes:

### Other Key Files

TBD


## Links to omics data analysis notebooks

1. EDA: https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Marcora_MSSM/MiGA/data_overview.ipynb
2. [Molecular Phenotype Calling](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Marcora_MSSM/MiGA/molecular-phenotype-calling.ipynb)
3. [Genotype Preprocessing](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Marcora_MSSM/MiGA/genotype-preprocessing.ipynb)
4. [Phenotype Preprocessing](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Marcora_MSSM/MiGA/phenotype-preprocessing.ipynb)
5. [Covariate Preprocessing](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Marcora_MSSM/MiGA/covariate-preprocessing-age_sex.ipynb)
6. [Association Scan](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Marcora_MSSM/MiGA/association-scan-preprocessing-template-age_sex.ipynb)

## QTL Analysis
QTL analysis for this dataset is documented in [../../qtl/eQTL/MiGA_brain_expression_qtl.md](../../qtl/eQTL/MiGA_brain_expression_qtl.md).

Flagship paper analyses:
- Fine-mapping (SuSiE-RSS): [syn69670592](https://www.synapse.org/Synapse:syn69670592)
- TWAS weight models: [syn69670600](https://www.synapse.org/Synapse:syn69670600)
- Quantile TWAS (qTWAS) models: [syn69670611](https://www.synapse.org/Synapse:syn69670611)
- Multi-context colocalization (ColocBoost): [syn69670597](https://www.synapse.org/Synapse:syn69670597)
- AD GWAS–xQTL colocalization results: [syn69865816](https://www.synapse.org/Synapse:syn69865816)
- AD GWAS–xQTL colocalization models: [syn69670630](https://www.synapse.org/Synapse:syn69670630)
