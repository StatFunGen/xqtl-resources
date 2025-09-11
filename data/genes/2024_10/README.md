# Readme for the Gene List (October 2024)

This gene list was compiled using multiple sources, including the primary and companion xQTL papers, as well as genes of interest provided by different PIs or institutions, documented in the `Projects_or_PI_interested` column.

Additionally, we incorporated data from two tables provided by NIAGADS ([https://adsp.niagads.org/gvc-top-hits-list/](https://adsp.niagads.org/gvc-top-hits-list/)):

- **Table 2**: Known as the risk gene list.  
- **Table 1**: Represents risk loci, which NIAGADS annotated to corresponding genes.

We further annotated these loci using the **flatten table** from **FunGen-xQTL**, released in May 2024. This annotation includes only loci with variants in the **95% credible set (CS)** and a minimal absolute correlation greater than **0.8** (`cs_coverage_0.95_min_corr`). We excluded all sQTL contexts and retained **39 relevant contexts**, listed below:

'MiGA_THA_eQTL', 'BM_22_MSBB_eQTL', 'Exc_DeJager_eQTL', 'DLPFC_DeJager_eQTL', 'AC_DeJager_eQTL', 'Exc_mega_eQTL', 'DLPFC_Bennett_pQTL', 'STARNET_eQTL', 'MiGA_GFM_eQTL', 'MiGA_SVZ_eQTL', 'Exc_Kellis_eQTL', 'Knight_eQTL', 'MiGA_GTS_eQTL', 'BM_10_MSBB_eQTL', 'BM_36_MSBB_eQTL', 'BM_44_MSBB_eQTL', 'PCC_DeJager_eQTL', 'Oli_Kellis_eQTL', 'MSBB_BM36_pQTL', 'Ast_DeJager_eQTL', 'Ast_mega_eQTL', 'Oli_mega_eQTL', 'Oli_DeJager_eQTL', 'OPC_DeJager_eQTL', 'OPC_Kellis_eQTL', 'OPC_mega_eQTL', 'Ast_Kellis_eQTL', 'monocyte_ROSMAP_eQTL', 'Inh_DeJager_eQTL', 'Inh_Kellis_eQTL', 'Inh_mega_eQTL', 'Mic_Kellis_eQTL', 'DLPFC_Klein_gpQTL', 'Mic_13_Kellis_eQTL', 'Ast_10_Kellis_eQTL', 'Mic_mega_eQTL', 'Mic_12_Kellis_eQTL', 'Mic_DeJager_eQTL', '10_MSBB_eQTL'

## Annotation and Consistency Checking with NIAGADS

We matched loci from **NIAGADS Table 1** against our flatten table annotations following these rules:

### 1. Consistent Targets
- If the same target is identified by both sources, we label it as **"consistent"** in both the `NIAGADS_debate` and `xQTL_debate` columns.

### 2. Mismatch Cases
- If there is a mismatch, we document the genes from **NIAGADS Table 1** and list our annotated genes (separated by commas if there are multiple) in the `NIAGADS_debate` column.
- We also document the annotated genes from our flatten table in the `xQTL_debate` column, including the original gene name from **NIAGADS Table 1** for reference.

### 3. Unannotated Loci
- If a locus from **NIAGADS Table 1** is not annotated by our flatten table, we leave the corresponding entries in both `NIAGADS_debate` and `xQTL_debate` columns as **NA** (empty).

### 4. Not Applicable Cases
- For genes not included in **NIAGADS Table 1**, we leave both columns **NA** (empty).

Any genes listed in NIAGADS Table 1 but annotated to other genes were also labeled as ‘NIAGADS_1’ in the Projects_or_PI_interested column. This is why the total count for ‘NIAGADS_1’ resources differs from the numbers reported on their website.
