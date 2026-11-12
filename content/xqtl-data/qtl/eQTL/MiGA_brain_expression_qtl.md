---
type: qtl
modality: expression
short_title: MiGA microglia
cohort: MiGA
context: microglia
sample_size: 255
access: controlled
status: staged
release:
synapse_ids: [syn70095505, syn70095506, syn75134502, syn70094765, syn74987560, syn74986600, syn69865816]
lead_analysts: [Travyse Edwards]
last_verified:
methods:
  cis-QTL: done
  SuSiE: done
  TWAS: done
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

| Region | Samples (columns) | Genes (rows) | File size |
|---|---|---|---|
| GFM | 75 | 45,814 | 11 MB |
| GTS | 63 | 45,472 | 8.8 MB |
| THA | 61 | 45,461 | 8.6 MB |
| SVZ | 53 | 42,086 | 6.8 MB |

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

The flagship paper analyses on the AD Knowledge Portal are listed below.

| Result | MiGA folder | Contents | All datasets |
|---|---|---|---|
| Fine-mapping export | [syn70095506](https://www.synapse.org/Synapse:syn70095506) | cis-QTL results and summary statistics exported for each gene | [syn69670592](https://www.synapse.org/Synapse:syn69670592) |
| Fine-mapping models (SuSiE) | [syn75134502](https://www.synapse.org/Synapse:syn75134502) | `MiGA_eQTL.*.univariate_bvsr.rds` | [syn69670592](https://www.synapse.org/Synapse:syn69670592) |
| TWAS weight models | [syn70094765](https://www.synapse.org/Synapse:syn70094765) | `MiGA_eQTL.*.univariate_bvsr.rds` | [syn69670600](https://www.synapse.org/Synapse:syn69670600) |
| Quantile TWAS (qTWAS) models | not available yet | | |
| Multi-context colocalization models (ColocBoost) | [syn74987560](https://www.synapse.org/Synapse:syn74987560) | `MiGA.*.cb_xqtl.rds` | [syn69670597](https://www.synapse.org/Synapse:syn69670597) |
| AD GWAS and xQTL colocalization models | [syn74986600](https://www.synapse.org/Synapse:syn74986600) | `MiGA.*.cb_xqtl_AD_*.rds` | [syn69670630](https://www.synapse.org/Synapse:syn69670630) |
| AD GWAS and xQTL colocalization results | | | [syn69865816](https://www.synapse.org/Synapse:syn69865816) |

The MiGA fine-mapping export and fine-mapping models sit together under [syn70095505](https://www.synapse.org/Synapse:syn70095505).
