---
type: reference
short_title: In-sample LD reference
cohort: ADSP
sample_size: 16571
access: controlled
status: staged
release:
synapse_ids: [syn53171227, syn69670651, syn69670652, syn75082259]
lead_analysts: [Oluwatosin Olayinka]
last_verified:
---

# ADSP In-Sample LD Reference Panel
FunGen-xQTL provides two LD references built from the same ADSP whole genomes. This page is the in-sample panel: LD computed directly from the individual genotypes. The other is the [LD sketch](ld_sketch), a compressed panel that can be shared without individual genotype rows.

LD matrices calculated from whole genome sequencing data from 16571 non-Hispanic white individuals obtained from the Genome Center for Alzheimer's Disease (GCAD). Correlation matrices were calculated between SNPs within 1361 LD blocks which were obtained from [this Github page](https://github.com/jmacdon/LDblocks_GRCh38/) (generated from 1000 Genomes EUR samples).

## Contact
Oluwatosin Olayinka

## Output Format
Each LD block contains two files of interest:
- an xz-compressed file containing the correlation values, suffixed by `.cor.xz`
    - this file is a compressed file where the matrix is encoded in a space-separated format 
    - the data is stored in the upper triangle of the matrix
- a [Plink `.bim`](https://www.cog-genomics.org/plink/1.9/formats#bim) file suffixed by `.cor.xz.bim` containing unique IDs for each variant

```r
ld_block_ref_file = "/path/to/matrix.cor.xz"
var_names = read.table(paste0(ld_block_ref_file, ".bim"), header = F)$V2
ld <- scan(xzfile(ld_block_ref_file))
ld <- matrix(ld, ncol = sqrt(length(ld)), byrow = TRUE)
ld <- ld + t(ld)
diag(ld) = 1
rownames(ld) = var_names
colnames(ld) = var_names
```

## Data Availability
The generated files are on the [AD Knowledge Portal](https://www.synapse.org/#!Synapse:syn53171227).

## Analysis Notebook Link
1. Generating LD Reference Panel: https://github.com/StatFunGen/xqtl-protocol/blob/main/code/SoS/graveyard/ld_reference_generation.ipynb

## ADSP Whole Genome Sequencing LD Reference Panel

The FunGen-xQTL flagship paper used a large LD reference panel derived from the Alzheimer's Disease Sequencing Project (ADSP) whole genome sequencing data for fine-mapping analyses.

- **Samples**: 16,571 individuals of European ancestry
- **Variant call**: WGS, high-quality SNPs and indels
- **Use**: LD reference for SuSiE-RSS fine-mapping of xQTL and AD GWAS loci

| Resource | AD Knowledge Portal ID |
|----------|------------|
| ADSP WGS LD reference (genotype data) | [syn69670651](https://www.synapse.org/Synapse:syn69670651) |
| ADSP WGS LD reference (LD matrices) | [syn69670652](https://www.synapse.org/Synapse:syn69670652) |
| Pre-computed in-sample LD matrices, 1,361 LD blocks | [syn75082259](https://www.synapse.org/Synapse:syn75082259) |
