# AD GWAS Summary Statistics

Summary statistics from large-scale Alzheimer's disease GWAS used as primary trait input for fine-mapping, TWAS, and colocalization analyses in the FunGen-xQTL flagship study.

> All summary statistics were harmonized to **GRCh38** prior to downstream analyses. The APOE region (chr19:44.4–46.5 Mb) was handled separately due to its complex LD structure. A custom LD reference panel was constructed from **16,905 ADSP whole-genome sequenced samples of European ancestry**.

## Datasets

Six datasets from four AD meta-analyses were used, encompassing clinically confirmed late-onset AD, proxy-based AD cases, and broader dementia phenotypes.

| Study | Population | N cases | N controls | Phenotype definition | Notes |
|---|---|---|---|---|---|
| [Bellenguez et al. 2022](https://doi.org/10.1038/s41588-022-01024-z) *Nat Genet* | European | 111,326 | 677,663 | Clinically confirmed late-onset AD | Primary GWAS; used throughout |
| [Wightman et al. 2021](https://doi.org/10.1038/s41588-021-00921-z) *Nat Genet* | European | 90,338 | 1,036,225 | AD + proxy-AD (UK Biobank) | Proxy-based phenotype included |
| [Kunkle et al. 2019](https://doi.org/10.1038/s41588-019-0358-2) *Nat Genet* | European | 21,982 | 41,944 | Clinically confirmed late-onset AD | ADGC/IGAP |
| [Jansen et al. 2019](https://doi.org/10.1038/s41588-018-0311-9) *Nat Genet* | European | — | — | AD + proxy-AD (UK Biobank) | Meta-analysis with IGAP |
| [Lambert et al. 2013](https://doi.org/10.1038/ng.2802) *Nat Genet* | European | 17,008 | 37,154 | Clinically confirmed late-onset AD | IGAP stage 1; historical reference |
| Broader dementia phenotype | European | — | — | Broader dementia definition | Fourth meta-analysis source |

## Quality Control

Summary statistics were processed through a QC pipeline built around [SLALOM](https://doi.org/10.1038/s41588-022-01024-z), supplemented by manual curation comparing single-effect regression and conditional regression outputs to exclude suspicious or unstable loci. After QC, **170 AD-associated loci** were retained for fine-mapping.

## LD Reference Panel

| Panel | N samples | Population | Build | Synapse ID |
|---|---|---|---|---|
| ADSP WGS | 16,905 | European ancestry | GRCh38 | [syn69670651](https://www.synapse.org/Synapse:syn69670651) → `EUR/` ([syn69670652](https://www.synapse.org/Synapse:syn69670652)) |

## Data Access

| Resource | Description | Synapse ID |
|---|---|---|
| ADSP LD reference (EUR) | Custom LD panel for fine-mapping and colocalization | [syn69670652](https://www.synapse.org/Synapse:syn69670652) |
| LDSC reference data | LD scores, munged GWAS, sLDSC annotations | [syn69670653](https://www.synapse.org/Synapse:syn69670653) |
| LDSC munged GWAS | Pre-munged AD GWAS summary statistics | [syn69670656](https://www.synapse.org/Synapse:syn69670656) |
| AD GWAS fine-mapping models | Fine-mapping outputs per GWAS dataset | [syn69670625](https://www.synapse.org/Synapse:syn69670625) |
| AD fine-mapping results | Fine-mapped loci and credible sets | [syn69696846](https://www.synapse.org/Synapse:syn69696846) |
| Top loci unified summary | `AD_GWAS_finemapping_109_blocks_top_loci_unified_any0.8ANDmin0.5.csv.gz` | [syn69865824](https://www.synapse.org/Synapse:syn69865824) |

All resources are in the FunGen-xQTL staging folder: [syn68872650](https://www.synapse.org/Synapse:syn68872650) *(staging)*

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
