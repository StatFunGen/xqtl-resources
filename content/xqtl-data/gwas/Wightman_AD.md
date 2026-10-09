---
type: gwas
short_title: Wightman 2021
status: staged
access:
release:
synapse_ids: [syn69670625, syn69670626, syn69670630, syn69696846, syn69865816, syn69865824, syn70095142, syn70095143]
lead_analysts: [Oluwatosin Olayinka]
last_verified:
---

# Alzheimer's Disease GWAS Summary Data (Wightman)

SNP-level association summary statistics for Alzheimer's disease (AD) from [Wightman et al. 2021](https://doi.org/10.1038/s41588-021-00921-z) in *Nature Genetics*. This page covers three meta-analyzed sets of summary statistics: all individuals, all individuals excluding 23andMe, and all individuals excluding 23andMe and UKBB.

## Contact

Oluwatosin Olayinka


## Path(s) to summary statistics
- NIAGADS FTP
 
- CU
    - original data (in GRCh37)
        - only 23andMe individuals
    - liftover data (in hg38)
        
## Path to SuSiE RSS Fine-mapping Objects
- AD GWAS fine-mapping models (Synapse): [syn69670625](https://www.synapse.org/Synapse:syn69670625)
- Additional fine-mapping objects: [syn69696846](https://www.synapse.org/Synapse:syn69696846)
- Top unified loci summary: [syn69865824](https://www.synapse.org/Synapse:syn69865824)

## AD GWAS–xQTL Integration

AD GWAS–xQTL colocalization results (ColocBoost): [syn69865816](https://www.synapse.org/Synapse:syn69865816)

AD GWAS–xQTL colocalization models: [syn69670630](https://www.synapse.org/Synapse:syn69670630)

AD colocalization models (all GWAS studies): [syn69670626](https://www.synapse.org/Synapse:syn69670626)

### Integrated AD Gene-Level Summary

AD risk genes prioritized by xQTL + GVC: [syn70095142](https://www.synapse.org/Synapse:syn70095142)

AD risk genes prioritized by xQTL + TWAS + GVC: [syn70095143](https://www.synapse.org/Synapse:syn70095143)

 
## Download source
The download source is not public.

## File Schema
- `chromosome`: chromosome ID
- `position`: hg38 position (converted from hg19 with liftOver)
- `variant`: variant ID in the form `chr${chromosome}_${position}_${ref}_${alt}`
- `alt`: alternative effect allele
- `ref`: reference allele
- `z` - z-score of the SNP effect size
- `pvalue`: p-value of `beta`
- `N`:

## Links to GWAS data analysis notebooks
1. Summary statistics preprocessing: https://github.com/floutt/brain-xqtl-analysis/blob/main/analysis/Zhang_BU/susie_rss/summary_stat_qc_all.nb.html

## Cohorts included in this study

- 1,126,563 individuals = 90,338 (46,613 proxy) cases + 1,036,225 (318,246 proxy) controls
 - 77,779 cases + 554,893 controls from Jansen et al.
 - 12,559 cases + 481,332 controls not from Jansen et al: Finngen, GRACE, HUNT, BioVU, 23andme, Gothenburg H70 Birth Cohort Studies and Clinical AD from Sweden (Gothenburg), ANMerge.
- Population: US and Europe (UK, Norway, Sweden, Iceland, Finland, Spain)

*Supplementary Table 1: A list of the datasets included in the meta-analysis. The UKB data was generated with a continous phenotype so the case-control values are estimates where the number of individuals with phenotype values <1 are controls and >=1 are cases.*

| Dataset                                                                      | Population  | Cases  | Controls  | Imputation panel                 |
| ---------------------------------------------------------------------------- | ----------- | ------ | --------- | -------------------------------- |
| Included in Jansen et al. (2019)        ｜  ｜  ｜              ｜                       |
| IGAP\*                                                                       | US & Europe | 21982  | 41944     | 1000G phase 1                    |
| UKB (Proxy)                                                                  | UK          | 46613  | 318246    | HRC, 1000G, UK10k                |
| DemGene                                                                      | Norway      | 1638   | 6059      | HRC                              |
| TwinGene                                                                     | Sweden      | 224    | 6321      | HRC                              |
| STSA                                                                         | Sweden      | 320    | 750       | HRC                              |
| deCODE (partially included)                                                  | Iceland     | 7002   | 181573    | deCODE                           |
| Total                                                                        | \-          | 77779  | 554893    | \-                               |
| Not included in Jansen et al. (2019)                                         |
| Finngen\*                                                                    | Finland     | 1798   | 72206     | SISu v3                          |
| GR@CE                                                                        | Spain       | 4120   | 3289      | HRC                              |
| HUNT                                                                         | Norway      | 1156   | 7157      | HRC+HUNT                         |
| BioVU                                                                        | US          | 600    | 36059     | HRC                              |
| 23andMe                                                                      | US          | 3807   | 359839    | 1000 Genomes Phase 3, UK10K, HRC |
| Gothenburg H70 Birth Cohort Studies and Clinical AD from Sweden (Gothenburg) | Sweden      | 712    | 2523      | HRC                              |
| ANMerge                                                                      | EUR         | 366    | 259       | HRC                              |
| Total                                                                        | \-          | 12559  | 481332    | \-                               |
| Grand total                                                                  | \-          | 90,338 | 1,036,225 |                                  |
| \*=publically available                                                      |             |        |           |                                  |


