---
type: reference
short_title: LDSC scores and annotations
cohort: ADSP
sample_size:
access: controlled
status: staged
release:
synapse_ids: [syn69670653, syn69670656, syn75157484]
lead_analysts: []
last_verified:
---

# LDSC Reference Data and Functional Annotations
Reference files for LD score regression (LDSC) and stratified LDSC (sLDSC), computed from the ADSP LD reference instead of the default 1000 Genomes panels. They are used to estimate AD heritability and to test which functional annotations, such as brain cell-type regulatory elements, are enriched for AD heritability.

## Contents

| Resource | What it holds | AD Knowledge Portal ID |
|----------|---------------|------------|
| LDSC reference data | LD scores, sLDSC annotations and munged GWAS, computed from the [in-sample LD reference panel](ld_reference) | [syn69670653](https://www.synapse.org/Synapse:syn69670653) |
| LDSC munged GWAS | AD GWAS summary statistics, pre-processed for LDSC | [syn69670656](https://www.synapse.org/Synapse:syn69670656) |
| sLDSC baseline-LD v2.2 | Stratified LDSC baseline-LD v2.2 reference files, in 1000 Genomes EUR and ADSP-overlap versions | [syn75157484](https://www.synapse.org/Synapse:syn75157484) |

Functional enrichment annotations in UCSC bed format (regulatory elements, cell-type-specific markers and brain-specific annotations relevant to neurodegeneration) are in the LDSC reference data folder.

## Analysis Notebook Link
1. Stratified LDSC enrichment: https://github.com/StatFunGen/xqtl-protocol/blob/main/code/SoS/enrichment/sldsc_enrichment.ipynb
