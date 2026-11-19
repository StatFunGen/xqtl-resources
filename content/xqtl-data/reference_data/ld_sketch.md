---
type: reference
short_title: LD sketch
cohort: ADSP
sample_size: 16571
access: controlled
status: staged
release:
synapse_ids: [syn75082260]
lead_analysts: [Jenny Anak Empawi]
last_verified:
---

# ADSP LD Sketch Panel
A compressed LD reference built from the same ADSP Release 4 whole genomes as the [in-sample LD reference panel](ld_reference) (16,571 European-ancestry individuals). The genotype matrix is multiplied by a random matrix with B = 10,000 columns, so the panel holds 10,000 "pseudo-people" instead of real individuals. LD computed from the sketch matches in-sample LD on average, and the panel is far smaller than the genotypes it comes from.

## When to use it
Use it as the LD reference for summary-statistics fine-mapping (SuSiE-RSS) and TWAS when the in-sample panel cannot be shared or is too large to move. The FGMB Atlas uses it for RWAS association testing and fine-mapping.

## Privacy
No row of the sketch is one person's genotypes. As long as the random projection matrix and its seed are not released, a sketch reveals no more about who is in the cohort than the exact cohort LD would. This compares two ways of sharing LD; it is not an absolute privacy guarantee such as differential privacy (Sun et al., manuscript).

## Format
PLINK 2 genotype files (`.pgen`, `.pvar`, `.psam`) with 10,000 pseudo-samples, in the format made by the protocol's RSS LD sketch pipeline.

## Data Availability

| Resource | AD Knowledge Portal ID |
|----------|------------|
| ADSP LD sketch (PLINK 2) | [syn75082260](https://www.synapse.org/Synapse:syn75082260) |

## Analysis Notebook Link
1. Building the LD sketch: https://github.com/StatFunGen/xqtl-protocol/blob/main/code/SoS/reference_data/rss_ld_sketch.ipynb
2. Fine-mapping with summary statistics: https://github.com/StatFunGen/xqtl-protocol/blob/main/code/SoS/mnm_analysis/mnm_methods/rss_analysis.ipynb

## Reference
Sun, Cao, Zou et al. Robust fine-mapping of molecular and complex traits with shareable LD references. Manuscript.
