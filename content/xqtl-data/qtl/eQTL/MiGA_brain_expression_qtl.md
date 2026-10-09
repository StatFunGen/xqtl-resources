---
type: qtl
modality: expression
short_title: MiGA microglia
cohort: MiGA
context: microglia
sample_size: 255
access: controlled
status:
release:
synapse_ids: [syn69670592, syn69670600, syn69670611, syn69670597, syn69865816, syn69670630]
lead_analysts: [Travyse Edwards]
last_verified:
---

# MiGA multi-brain region gene expression

MiGA is a genetic and transcriptomic resource of 255 primary human microglia samples, isolated ex vivo from four brain regions of 100 donors. Donors have neurodegenerative, neurological or neuropsychiatric disorders, or are unaffected controls.

Post-mortem brain samples come from the Netherlands Brain Bank (NBB) and the Neuropathology Brain Bank and Research CoRE at Mount Sinai Hospital. The Ethical Committee of the VU University Medical Center (Amsterdam) and the Mount Sinai Institutional Review Board approved collection of the human brain material. NBB obtained informed consent from each donor before death for autopsy and for research use of brain tissue and clinical information.

## Contact

Travyse Edwards

## Study Overview

- Study information is in [MiGA study info](../../study_info/MiGA.md).
- Sample set and logo are at [dss.niagads.org/sample-sets/snd10022](https://dss.niagads.org/sample-sets/snd10022/).

## Dataset Description

### Raw data

- [NIAGADS dataset ng00105](https://dss.niagads.org/datasets/ng00105/)
- [NIAGADS study sa000018](https://dss.niagads.org/studies/sa000018/)

### Molecular phenotype matrices

Gene expression is available for four brain regions: medial frontal gyrus (GFM), superior temporal gyrus (GTS), thalamus (THA), and subventricular zone (SVZ). Each region has a TPM matrix with gene IDs in rows and sample names in columns. Low-expression genes and outlier samples were removed.

| Region | Samples (columns) | Genes (rows) | File size | Path |
|---|---|---|---|---|
| GFM | 75 | 45,814 | 11 MB | `/sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/rnaseq/GFM/sample-gfm.trimmed.clean.rnaseqc.low_expression_filtered.outlier_removed.tpm.gct.gz` |
| GTS | 63 | 45,472 | 8.8 MB | `/sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/rnaseq/GTS/sample-gts.trimmed.clean.rnaseqc.low_expression_filtered.outlier_removed.tpm.gct.gz` |
| THA | 61 | 45,461 | 8.6 MB | `/sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/rnaseq/THA/sample-tha.trimmed.clean.rnaseqc.low_expression_filtered.outlier_removed.tpm.gct.gz` |
| SVZ | 53 | 42,086 | 6.8 MB | `/sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/rnaseq/SVZ/sample-svz.trimmed.clean.rnaseqc.low_expression_filtered.outlier_removed.tpm.gct.gz` |

### Other key files

None are listed yet.

## Analysis notebooks

1. [Exploratory data analysis](https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Marcora_MSSM/MiGA/data_overview.ipynb)
2. [Molecular phenotype calling](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Marcora_MSSM/MiGA/molecular-phenotype-calling.ipynb)
3. [Genotype preprocessing](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Marcora_MSSM/MiGA/genotype-preprocessing.ipynb)
4. [Phenotype preprocessing](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Marcora_MSSM/MiGA/phenotype-preprocessing.ipynb)
5. [Covariate preprocessing](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Marcora_MSSM/MiGA/covariate-preprocessing-age_sex.ipynb)
6. [Association scan](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Marcora_MSSM/MiGA/association-scan-preprocessing-template-age_sex.ipynb)

## QTL analysis

The QTL analysis of this dataset is documented in [MiGA brain expression QTL](../../qtl/eQTL/MiGA_brain_expression_qtl.md).

The flagship paper analyses on Synapse are listed below.

- Fine-mapping (SuSiE-RSS), [syn69670592](https://www.synapse.org/Synapse:syn69670592)
- TWAS weight models, [syn69670600](https://www.synapse.org/Synapse:syn69670600)
- Quantile TWAS (qTWAS) models, [syn69670611](https://www.synapse.org/Synapse:syn69670611)
- Multi-context colocalization (ColocBoost), [syn69670597](https://www.synapse.org/Synapse:syn69670597)
- AD GWAS and xQTL colocalization results, [syn69865816](https://www.synapse.org/Synapse:syn69865816)
- AD GWAS and xQTL colocalization models, [syn69670630](https://www.synapse.org/Synapse:syn69670630)
