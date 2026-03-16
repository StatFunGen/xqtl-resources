# AD GWAS Summary Statistics

Summary statistics from large-scale Alzheimer's disease genome-wide association studies (GWAS) used as primary trait input for fine-mapping, TWAS, and colocalization analyses.

> All summary statistics were harmonized to **GRCh38** prior to downstream analyses. The APOE region (chr19:44.4–46.5 Mb) was handled separately due to its complex LD structure.

## Datasets

| Study | Population | N cases | N controls | Notes |
|---|---|---|---|---|
| [Bellenguez et al. 2022](https://doi.org/10.1038/s41588-022-01024-z) *Nature Genetics* | European | 111,326 | 677,663 | Largest AD GWAS to date; primary GWAS used throughout |
| [Wightman et al. 2021](https://doi.org/10.1038/s41588-021-00921-z) *Nature Genetics* | European | 90,338 | 1,036,225 | Includes proxy-AD phenotype from UK Biobank |
| [Kunkle et al. 2019](https://doi.org/10.1038/s41588-019-0358-2) *Nature Genetics* | European | 21,982 | 41,944 | Clinically diagnosed late-onset AD (ADGC/IGAP) |
| [Lambert et al. 2013](https://doi.org/10.1038/ng.2802) *Nature Genetics* | European | 17,008 | 37,154 | IGAP stage 1; historical reference |
| [Marioni et al. 2018](https://doi.org/10.1038/s41398-018-0150-6) *Translational Psychiatry* | European | — | — | GWAS by proxy (GWAX) from UK Biobank |
| [Naj et al. 2011](https://doi.org/10.1038/ng.801) *Nature Genetics* | European | 8,309 | 7,366 | ADGC; used for replication and sensitivity analyses |

## LD Reference Panels

| Panel | Population | Build | Notes |
|---|---|---|---|
| 1000 Genomes Phase 3 | EUR | GRCh38 | Primary LD reference for European GWAS |
| UK Biobank (subset) | EUR | GRCh38 | Used for large-scale fine-mapping (PolyFun) |
| ROSMAP WGS | EUR-enriched | GRCh38 | In-sample LD where available |

## Abbreviations

| Abbreviation | Full name |
|---|---|
| AD | Alzheimer's disease |
| GWAS | Genome-wide association study |
| IGAP | International Genomics of Alzheimer's Project |
| ADGC | Alzheimer's Disease Genetics Consortium |
| GWAX | Genome-wide association by proxy |
| LD | Linkage disequilibrium |
