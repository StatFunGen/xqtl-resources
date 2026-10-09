---
type: gwas
status:
synapse_ids: [syn69670625, syn69670630, syn69865816, syn69865824, syn70095142, syn70095143]
lead_analysts: [Oluwatosin Olayinka, Hao Sun, Rui Dong]
last_verified:
---

# Alzheimer's Disease GWAS Summary Data (Bellenguez)

SNP-level association summary statistics for Alzheimer's disease (AD) from [Bellenguez et al. 2022](https://doi.org/10.1038/s41588-022-01024-z) in *Nature Genetics*. The study includes proxy AD samples from the UK Biobank (UKBB).

## Contact

Oluwatosin Olayinka, Hao Sun and Rui Dong

## Path(s) to summary statistics

- CU
    - a related meta-analysis of GR@ACE, IGAP and UKB, publicly available in [de Rojas 2021, Nature Communications](https://www.nature.com/articles/s41467-021-22491-8).



## Download source

The data are derived from the summary statistics of [Bellenguez et al.](http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90027001-GCST90028000/GCST90027158/).

Rui Dong approved the request for the cohort-specific data in early 2024, and the data were uploaded to the cluster in March 2024.

## File Schema

- `chromosome`: chromosome ID
-  `position`: hg38 position
-  `ref`: hg38 reference allele
-  `alt`: alternative effect allele
-  `variant`: variant ID in the form `chr${chromosome}_${position}_${ref}_${alt}`
-  `beta`: SNP effect size
-  `se`: standard error of `beta`
-  `pvalue`: p-value of `beta` estimate
-  `maf`: minor allele frequency
-  `n_cases`: number of cases for estimate
-  `n_controls`: number of controls for estimate
-  `original_effect_allele_frequency`: allele frequency of the original effect allele

## Links to GWAS data analysis notebooks

1. GWAS summary statistics processing: https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/GWAS/AD_GWAS_processing.ipynb 

## Cohorts included in this study

111,326 clinically diagnosed/proxy AD cases + 677,663 controls
- Stage I: 39,106 clinically diagnosed AD cases + 46,828 proxy-ADD cases + 401,577 controls
- Stage II: 25,392 AD cases + 276,086 controls

cohorts:
- EADB: The European Alzheimer & Dementia Biobank (15 European countries). Also called `EADB-TOPMed` and `EADB-core`. 21,101,680 variants in sum.stats.
- EADI: European Alzheimer's Disease Initiative. 12,540,914 variants in sum.stats.
- UKBB: UK Biobank. We have the genotype and imputed variants ourselves.
- GR@ACE: the Genome Research at Fundació ACE. 61,744,410 variants in sum.stats.
- GERAD/PERADES
- DemGene
- Bonn
- the Rotterdam study
- the CCHS study
- NxC
- FinnGen: 
    - R6 includes 147,061 females and 113,344 males, and the one that Bellenguez paper used should be `R6/AD_WIDE` (N=7,329 cases and N=252,879 controls).
    - R10 is the latest version (until 20240222), including 230,310 females and 181,871 males.

*Supplementary Table 1: Demographic descriptions of the different meta-analyzed GWAS, including a description of EADB per country*

|                               | AD or proxy-ADD cases | |  |  |  |          | Controls   |  |  |  |
| ---------                     |              --       |   --      |   --       |       --     |                  --      | -- |--   |     --      |    -- |                ---          |
|                               | N                     | % females | Age        | Age at onset | APOE e4 allele frequency |    |   N | % females   |   Age | APOE e4 allele frequency |
| **DISCOVERY**                     |                       |           |            |              |                          |  |   |           |     |                          |
| **EADB-TOPMed**                   | 20,301                | 61.7      | 72.0±10.4  | 71.1±10.5 | 32.6 |  | 21,839 | 57.3 | 67.0±14.3 | 13.2 |
| _Belgium_                       | 1,230                 | 64.6      | 78.7±5.9   | 78.3±5.9 | 31.6 |  | 1,474 | 61.8 | 70.1±8.4 | 13.6 |
| _Bulgaria_                      | 164                   | 54.9      | 65.1±8.6   | 65.1±8.6 | 22.9 |  | \- | \- | \- | \- |
| _Switzerland_                   | 182                   | 64.3      | 76.0±6.5   | 76.9±6.0 | 19.2 |  | 388 | 55.9 | 74.8±4.0 | 10.1 |
| _Czech Republic_                | 183                   | 60.7      | 75.8±7.8   | \- | 31.7 |  | 61 | 65.6 | 66.9±7.2 | 10.7 |
| _Denmark_                       | 403                   | 57.1      | 79.6±7.8   | 79.6±7.8 | 33.7 |  | 654 | 54.4 | 73.1±8.5 | 15.4 |
| _Spain_                         | 3,273                 | 67.0      | 75.3±9.0   | 75.2±9.0 | 27.2 |  | 1,685 | 63.3 | 69.3±12.0 | 10.0 |
| _Finland_                       | 1,151                 | 64.0      | 70.9±8.8   | 69.8±8.5 | 42.0 |  | 1,806 | 51.4 | 71.8±7.1 | 15.9 |
| _France_                        | 1,664                 | 60.2      | 67.4±11.9  | 63.2±10.8 | 33.3 |  | 3,106 | 63.8 | 44.9±15.4 | 11.5 |
| _Germany_                       | 1,628                 | 60.3      | 74.8±9.4   | 74.6±9.8 | 33.1 |  | 2,050 | 56.0 | 74.2±8.0 | 12.3 |
| _Greece_                        | 614                   | 63.0      | 73.1±8.0   | 72.9±7.9 | 23.8 |  | 1,246 | 57.3 | 73.1±5.6 | 9.1 |
| _Italy_                         | 3,271                 | 68.1      | 73.7±8.9   | 72.2±8.7 | 25.0 |  | 1,317 | 56.8 | 72.2±10.5 | 8.6 |
| _The Netherlands_               | 2,438                 | 55.8      | 66.2±10.7  | 65.6±10.5 | 41.9 |  | 2,389 | 47.5 | 60.1±12.0 | 17.9 |
| _Portugal_                      | 80                    | 75.0      | 69.9±9.2   | 69.2±8.9 | 30.0 |  | 74 | 75.7 | 67.2±6.8 | 17.6 |
| _Sweden_                        | 1,533                 | 62.9      | 72.8±11.2  | 72.8±11.2 | 40.7 |  | 3,089 | 61.8 | 70.6±9.8 | 15.6 |
| _United Kingdom_                | 2,487                 | 51.1      | 68.0±10.7  | 66.4±10.1 | 34.4 |  | 2,500 | 51.8 | 74.4±7.2 | 12.8 |
|                               |                       |           |            |  |  |  |  |  |  |  |
| **EADB-HRC**                      | 163                   | 54.0      | 71.5±7.9   | 71.5±7.9 | 31.8 |  | 405 | 48.1 | 77.2±2.1 | 14.1 |
|                               |                       |           |            |  |  |  |  |  |  |  |
| **EADI**                          | 2,400                 | 65.6      | 74.3±10.1  | 73.9±10.2 | 29.4 |  | 6,338 | 60.3 | 80.0±7.6 | 10.5 |
|                               |                       |           |            |  |  |  |  |  |  |  |
| **GERAD**                         | 3,030                 | 63.2      | 78.1±9.3   | 78.1±9.3 | 35.1 |  | 7,153 | 52.0 | 50.7±11.7 | 15.4 |
|                               |                       |           |            |  |  |  |  |  |  |  |
| **Bonn**                          | 635                   | 65.5      | 77.8±9.8   | 77.8±9.8 | 30.1 |  | 1,210 | 54.8 | 69.9±9.3 | 12.6 |
|                               |                       |           |            |  |  |  |  |  |  |  |
| **RS1**                           | 1,165                 | 72.9      | 83.7±0.2   | 83.7±0.2 | 33.4 |  | 4,739 | 56.7 | 82.8±0.1 | 12.9 |
| **RS2**                           | 141                   | 59.6      | 82.8±0.6   | 82.8±0.6 | 27.1 |  | 1,961 | 54.1 | 73.3±0.2 | 14.1 |
|                               |                       |           |            |  |  |  |  |  |  |  |
| **GR@ACE/DEGESCO**                | 6,497                 | 64.1      | 81.8±8.8   | 81.8±8.8 | 23.0 |  | 6,785 | 49.1 | 55.9±15.8 | 11.0 |
|                               |                       |           |            |  |  |  |  |  |  |  |
| **DemGene**                       | 1,693                 | 65.5      | 72.2±8.8   | 71.6±8.8 | 39.5 |  | 5,926 | 47.7 | 68.5±11.1 | 18.2 |
|                               |                       |           |            |  |  |  |  |  |  |  |
| **CCHS**                          | 365                   | 68.5      | 82.7±6.9   | 82.7±6.9 | 31.4 |  | 6,106 | 54.3 | 58.5±13.7 | 15.8 |
|                               |                       |           |            |  |  |  |  |  |  |  |
| **NxC**                           | 269                   | 72.4      | 78.7±6.9   | 78.7±6.9 | 26.0 |  | 675 | 44.4 | 51.9±8.9 | 10.0 |
|                               |                       |           |            |  |  |  |  |  |  |  |
| **UKBB-P**                      | 49,275                | 57.3      | 59.3±6.7   | \- | 22.6 |  | 338,440 | 56.0 | 55.8±8.2 | 14.0 |
|                               |                       |           |            |  |  |  |  |  |  |  |
| **REPLICATION**                   |
|                               |                       |           |            |  |  |  |  |  |  |  |
| **ADGC**                          | 17,141                | 57.3      | 78.6±8.1   | 73.4±8.0 | 37.7 |  | 17,627 | 58.8 | 75.8±8.1 | 14.4 |
|                               |                       |           |            |  |  |  |  |  |  |  |
| **CHARGE**                        |                       |           |            |  |  |  |  |  |  |  |
| _CHS_                           | 450                   | 66.0      | \-         | 81.9±5.2 | 34.0 |  | 1,702 | 60.0 | 81.1±5.0 | 20.0 |
| _FHS_                           | 472                   | 68.0      | \-         | 84.5±7.3 | 18.5 |  | 3,878 | 54.0 | 74.4±10.8 | 11.0 |
|                               |                       |           |            |  |  |  |  |  |  |  |
| **FinnGen**                       | 7,329                 | 48.8      | 82.2±7.4\* | 78.0±7.6 | 31.6 |  | 252,879 | 56.7 | 59.3±17.4\* | 17.8 |
|                               |                       |           |            |  |  |  |  |  |  |  |
|                               |                       |           |            |  |  |  |  |  |  |  |
| \*age at death or current age |                       |           |            |  |  |  |  |  |  |  |
|                               |                       |           |            |  |  |  |  |  |  |  |
| total                         | 111,326               |           |            |  |  |  | 677,663 |  |  |  |


## AD GWAS–xQTL Integration

AD GWAS–xQTL colocalization results (ColocBoost): [syn69865816](https://www.synapse.org/Synapse:syn69865816)

AD GWAS–xQTL colocalization models: [syn69670630](https://www.synapse.org/Synapse:syn69670630)

AD fine-mapping models (Synapse): [syn69670625](https://www.synapse.org/Synapse:syn69670625)

Top unified loci summary: [syn69865824](https://www.synapse.org/Synapse:syn69865824)

### Integrated AD Gene-Level Summary

AD risk genes prioritized by xQTL + GVC: [syn70095142](https://www.synapse.org/Synapse:syn70095142)

AD risk genes prioritized by xQTL + TWAS + GVC: [syn70095143](https://www.synapse.org/Synapse:syn70095143)

## Bellenguez 2026 update (noproxy, main, nobiobank)

Three 2026 analysis variants of the Bellenguez AD GWAS are staged on Synapse alongside the 2022 release. Each variant has a top-loci table (`AD_Bellenguez_<variant>_2026.gwas.top_loci.bed.gz`) and per-region SuSiE RSS fine-mapping objects (`AD_Bellenguez_<variant>_2026.*.gwas_finemap.rds`).

| Variant | Description |
| ------- | ----------- |
| `noproxy` | Clinically diagnosed AD cases only; proxy-ADD cases excluded |
| `main` | Primary 2026 analysis |
| `nobiobank` | Primary analysis with biobank cohorts excluded |

The unified AD loci xQTL summary (`unified_AD_loci_xQTL_summary_20261002.xlsx`) integrates the 2026 loci with xQTL colocalization results.

Note: the variant descriptions above are inferred from the file names and need confirmation by the analysts (cohort composition, sample sizes, genome build, source of the 2026 summary statistics).
