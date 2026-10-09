---
type: gwas
short_title: AD GWAS overview
status:
synapse_ids: [syn69670651, syn69670652, syn69670653, syn69670656, syn69670625, syn69696846, syn69865824]
lead_analysts: []
last_verified:
---

# AD GWAS Summary Statistics

The FunGen-xQTL flagship study uses summary statistics from large Alzheimer's disease (AD) GWAS as the trait input for fine-mapping, TWAS and colocalization.

> All summary statistics were harmonized to **GRCh38** before downstream analysis. The APOE region (chr19:44.4 to 46.5 Mb) was analyzed separately because of its complex LD structure. The LD reference panel was built from **16,905 ADSP whole-genome sequenced samples of European ancestry**.

## Datasets

The study used eight datasets from four AD meta-analyses: Bellenguez, Wightman, Kunkle and Jansen. They cover clinically confirmed late-onset AD, proxy-based AD cases, and broader dementia phenotypes. Lambert et al. 2013 (IGAP stage 1) is cited as a historical reference and is not one of the eight.

| Dataset | Study | Population | N cases | N controls | Phenotype definition |
|---|---|---|---|---|---|
| `AD_Bellenguez_2022` | [Bellenguez et al. 2022](https://doi.org/10.1038/s41588-022-01024-z) *Nat Genet* | European | 111,326 | 677,663 | Clinically confirmed late-onset AD. Primary GWAS, used throughout |
| `AD_Bellenguez_EADB_2022` | Bellenguez et al. 2022, EADB subset | European | n/a | n/a | n/a |
| `AD_Bellenguez_EADI_2022` | Bellenguez et al. 2022, EADI subset | European | n/a | n/a | n/a |
| `AD_Wightman_Full_2021` | [Wightman et al. 2021](https://doi.org/10.1038/s41588-021-00921-z) *Nat Genet* | European | 90,338 | 1,036,225 | AD and proxy-AD (UK Biobank) |
| `AD_Wightman_Excluding23andMe_2021` | Wightman et al. 2021, without 23andMe | European | n/a | n/a | AD and proxy-AD (UK Biobank) |
| `AD_Wightman_ExcludingUKBand23andME_2021` | Wightman et al. 2021, without UK Biobank and 23andMe | European | n/a | n/a | n/a |
| `AD_Kunkle_Stage1_2019` | [Kunkle et al. 2019](https://doi.org/10.1038/s41588-019-0358-2) *Nat Genet* | European | 21,982 | 41,944 | Clinically confirmed late-onset AD (ADGC/IGAP) |
| `AD_Jansen_2021` | [Jansen et al. 2019](https://doi.org/10.1038/s41588-018-0311-9) *Nat Genet* | European | n/a | n/a | AD and proxy-AD (UK Biobank), meta-analysis with IGAP |

## Quality control

Summary statistics passed a QC procedure built around [SLALOM](https://www.medrxiv.org/content/10.1101/2022.03.16.22272457). Manual curation then compared single-effect regression with conditional regression outputs and removed suspicious or unstable loci. After QC, **195 AD-associated loci** were retained for fine-mapping.

## LD reference panel

| Panel | N samples | Population | Build | Synapse ID |
|---|---|---|---|---|
| ADSP WGS | 16,905 | European ancestry | GRCh38 | [syn69670651](https://www.synapse.org/Synapse:syn69670651), subfolder `EUR/` ([syn69670652](https://www.synapse.org/Synapse:syn69670652)) |

## Data access

| Resource | Description | Synapse ID |
|---|---|---|
| ADSP LD reference (EUR) | LD panel for fine-mapping and colocalization | [syn69670652](https://www.synapse.org/Synapse:syn69670652) |
| LDSC reference data | LD scores, munged GWAS, sLDSC annotations | [syn69670653](https://www.synapse.org/Synapse:syn69670653) |
| LDSC munged GWAS | Pre-munged AD GWAS summary statistics | [syn69670656](https://www.synapse.org/Synapse:syn69670656) |
| AD GWAS fine-mapping models | Fine-mapping outputs per GWAS dataset | [syn69670625](https://www.synapse.org/Synapse:syn69670625) |
| AD fine-mapping results | Fine-mapped loci and credible sets | [syn69696846](https://www.synapse.org/Synapse:syn69696846) |
| Top loci unified summary | `AD_GWAS_finemapping_109_blocks_top_loci_unified_any0.8ANDmin0.5.csv.gz` | [syn69865824](https://www.synapse.org/Synapse:syn69865824) |

All resources are in the FunGen-xQTL staging folder, [syn68872650](https://www.synapse.org/Synapse:syn68872650).

## Abbreviations

| Abbreviation | Full name |
|---|---|
| AD | Alzheimer's disease |
| GWAS | Genome-wide association study |
| ADSP | Alzheimer's Disease Sequencing Project |
| IGAP | International Genomics of Alzheimer's Project |
| ADGC | Alzheimer's Disease Genetics Consortium |
| LD | Linkage disequilibrium |
| WGS | Whole-genome sequencing |
| QC | Quality control |
| sLDSC | Stratified linkage disequilibrium score regression |
