# FunGen-xQTL Resource File Format Description

## Overview

This repository provides Quantitative Trait Loci (QTL) analysis and GWAS integration results from the FunGen-xQTL project, across diverse aging human brain regions and cell types. The analyses span multiple cohorts including ROSMAP, Knight ADRC, Mount Sinai Brain Bank, MiGA, MetaBrain, and STARNET.

For comprehensive metadata of all analyses with harmonized context definitions, see our [analysis meta-data table](https://github.com/StatFunGen/xqtl-resources/blob/main/data/all_analysis_summary_tables_metadata.csv).

## Fine-mapping and integrative results for xQTL and AD GWAS

The following table catalogs all fine-mapped QTL and AD GWAS integration results, organized by molecular modality, cohort, tissue context, and analytical method. Each entry represents fine-mapped genetic loci for corresponding molecular phenotypes, with top loci and variants exported in standardized BED format.


| Modality | Cohort | Context | Method | Path |
|-----------|--------|----------|--------|------|
| eQTL | KNIGHT | Brain | single_context_finemapping | analysis_result/single_context/KNIGHT_eQTL/export/summary/context_specific/Knight_eQTL_brain.exported.toploci.bed.gz |
| pQTL | KNIGHT | Brain | single_context_finemapping | analysis_result/single_context/KNIGHT_pQTL/export/summary/context_specific/Knight_pQTL_brain.exported.toploci.bed.gz |
| eQTL | MSBB | BM_10 | single_context_finemapping | analysis_result/single_context/MSBB_eQTL/export/summary/context_specific/BM_10_MSBB_eQTL.exported.toploci.bed.gz |
| eQTL | MSBB | BM_22 | single_context_finemapping | analysis_result/single_context/MSBB_eQTL/export/summary/context_specific/BM_22_MSBB_eQTL.exported.toploci.bed.gz |
| eQTL | MSBB | BM_36 | single_context_finemapping | analysis_result/single_context/MSBB_eQTL/export/summary/context_specific/BM_36_MSBB_eQTL.exported.toploci.bed.gz |
| eQTL | MSBB | BM_44 | single_context_finemapping | analysis_result/single_context/MSBB_eQTL/export/summary/context_specific/BM_44_MSBB_eQTL.exported.toploci.bed.gz |
| pQTL | MSBB | BM_36 | single_context_finemapping | analysis_result/single_context/MSBB_pQTL/export/summary/context_specific/MSBB_BM36_pQTL.exported.toploci.bed.gz |
| eQTL | MetaBrain | Basalganglia | single_context_finemapping | analysis_result/single_context/MetaBrain/export/summary/context_specific/Metabrain_Basalganglia.exported.toploci.bed.gz |
| eQTL | MetaBrain | Cerebellum | single_context_finemapping | analysis_result/single_context/MetaBrain/export/summary/context_specific/Metabrain_Cerebellum.exported.toploci.bed.gz |
| eQTL | MetaBrain | Cortex | single_context_finemapping | analysis_result/single_context/MetaBrain/export/summary/context_specific/Metabrain_Cortex.exported.toploci.bed.gz |
| eQTL | MetaBrain | Hippocampus | single_context_finemapping | analysis_result/single_context/MetaBrain/export/summary/context_specific/Metabrain_Hippocampus.exported.toploci.bed.gz |
| eQTL | MetaBrain | Spinalcord | single_context_finemapping | analysis_result/single_context/MetaBrain/export/summary/context_specific/Metabrain_Spinalcord.exported.toploci.bed.gz |
| eQTL | MiGA | GFM | single_context_finemapping | analysis_result/single_context/MiGA_eQTL/export/summary/context_specific/MiGA_GFM_eQTL.exported.toploci.bed.gz |
| eQTL | MiGA | GTS | single_context_finemapping | analysis_result/single_context/MiGA_eQTL/export/summary/context_specific/MiGA_GTS_eQTL.exported.toploci.bed.gz |
| eQTL | MiGA | SVZ | single_context_finemapping | analysis_result/single_context/MiGA_eQTL/export/summary/context_specific/MiGA_SVZ_eQTL.exported.toploci.bed.gz |
| eQTL | MiGA | THA | single_context_finemapping | analysis_result/single_context/MiGA_eQTL/export/summary/context_specific/MiGA_THA_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | AC | single_context_finemapping | analysis_result/single_context/ROSMAP_eQTL/export/summary/context_specific/AC_CUIMC1_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Ast_10_MIT | single_context_finemapping | analysis_result/single_context/ROSMAP_eQTL/export/summary/context_specific/Ast_10_MIT_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Ast_CUIMC1 | single_context_finemapping | analysis_result/single_context/ROSMAP_eQTL/export/summary/context_specific/Ast_CUIMC1_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Ast_MIT | single_context_finemapping | analysis_result/single_context/ROSMAP_eQTL/export/summary/context_specific/Ast_MIT_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Ast_mega | single_context_finemapping | analysis_result/single_context/ROSMAP_eQTL/export/summary/context_specific/Ast_mega_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | DLPFC | single_context_finemapping | analysis_result/single_context/ROSMAP_eQTL/export/summary/context_specific/DLPFC_CUIMC1_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Exc_CUIMC1 | single_context_finemapping | analysis_result/single_context/ROSMAP_eQTL/export/summary/context_specific/Exc_CUIMC1_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Exc_MIT | single_context_finemapping | analysis_result/single_context/ROSMAP_eQTL/export/summary/context_specific/Exc_MIT_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Exc_mega | single_context_finemapping | analysis_result/single_context/ROSMAP_eQTL/export/summary/context_specific/Exc_mega_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Inh_CUIMC1 | single_context_finemapping | analysis_result/single_context/ROSMAP_eQTL/export/summary/context_specific/Inh_CUIMC1_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Inh_MIT | single_context_finemapping | analysis_result/single_context/ROSMAP_eQTL/export/summary/context_specific/Inh_MIT_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Inh_mega | single_context_finemapping | analysis_result/single_context/ROSMAP_eQTL/export/summary/context_specific/Inh_mega_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Mic_12_MIT | single_context_finemapping | analysis_result/single_context/ROSMAP_eQTL/export/summary/context_specific/Mic_12_MIT_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Mic_13_MIT | single_context_finemapping | analysis_result/single_context/ROSMAP_eQTL/export/summary/context_specific/Mic_13_MIT_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Mic_CUIMC1 | single_context_finemapping | analysis_result/single_context/ROSMAP_eQTL/export/summary/context_specific/Mic_CUIMC1_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Mic_MIT | single_context_finemapping | analysis_result/single_context/ROSMAP_eQTL/export/summary/context_specific/Mic_MIT_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Mic_mega | single_context_finemapping | analysis_result/single_context/ROSMAP_eQTL/export/summary/context_specific/Mic_mega_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | OPC_CUIMC1 | single_context_finemapping | analysis_result/single_context/ROSMAP_eQTL/export/summary/context_specific/OPC_CUIMC1_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | OPC_MIT | single_context_finemapping | analysis_result/single_context/ROSMAP_eQTL/export/summary/context_specific/OPC_MIT_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | OPC_mega | single_context_finemapping | analysis_result/single_context/ROSMAP_eQTL/export/summary/context_specific/OPC_mega_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Oli_CUIMC1 | single_context_finemapping | analysis_result/single_context/ROSMAP_eQTL/export/summary/context_specific/Oli_CUIMC1_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Oli_MIT | single_context_finemapping | analysis_result/single_context/ROSMAP_eQTL/export/summary/context_specific/Oli_MIT_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Oli_mega | single_context_finemapping | analysis_result/single_context/ROSMAP_eQTL/export/summary/context_specific/Oli_mega_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | PCC | single_context_finemapping | analysis_result/single_context/ROSMAP_eQTL/export/summary/context_specific/PCC_CUIMC1_eQTL.exported.toploci.bed.gz |
| pQTL | ROSMAP | DLPFC_Bennett | single_context_finemapping | analysis_result/single_context/ROSMAP_pQTL/export/summary/context_specific/DLPFC_Bennett_pQTL.exported.toploci.bed.gz |
| glycoQTL | ROSMAP | DLPFC_Klein_adjusted | single_context_finemapping | analysis_result/single_context/ROSMAP_pQTL/export/summary/context_specific/DLPFC_Klein_gpQTL_adjusted.exported.toploci.bed.gz |
| glycoQTL | ROSMAP | DLPFC_Klein_unadjusted | single_context_finemapping | analysis_result/single_context/ROSMAP_pQTL/export/summary/context_specific/DLPFC_Klein_gpQTL_unadjusted.exported.toploci.bed.gz |
| eQTL | ROSMAP | monocyte | single_context_finemapping | analysis_result/single_context/ROSMAP_pQTL/export/summary/context_specific/monocyte_ROSMAP_eQTL.exported.toploci.bed.gz |
| sQTL | ROSMAP | AC | single_context_finemapping | analysis_result/single_context/ROSMAP_sQTL/LeafCutter2/export/summary/context_specific/ROSMAP_AC_sQTL.exported.toploci.bed.gz |
| sQTL | ROSMAP | DLPFC | single_context_finemapping | analysis_result/single_context/ROSMAP_sQTL/LeafCutter2/export/summary/context_specific/ROSMAP_DLPFC_sQTL.exported.toploci.bed.gz |
| sQTL | ROSMAP | PCC | single_context_finemapping | analysis_result/single_context/ROSMAP_sQTL/LeafCutter2/export/summary/context_specific/ROSMAP_PCC_sQTL.exported.toploci.bed.gz |
| eQTL | STARNET | Mac | single_context_finemapping | analysis_result/single_context/STARNET_eQTL/export/summary/context_specific/STARNET_eQTL_Mac.exported.toploci.bed.gz |
| Multi | MSBB | All | multi_context_finemapping | analysis_result/multi_context/MSBB/export/summary/MSBB.exported.toploci.bed.gz |
| Multi | ROSMAP | All | multi_context_finemapping | analysis_result/multi_context/ROSMAP/export/summary/ROSMAP.exported.toploci.bed.gz |
| eQTL | MSBB | BM_10 | multi_gene_finemapping | analysis_result/multi_gene/MSBB/export/summary/context_specific/MSBB_BM_10_eQTL.exported.toploci.bed.gz |
| eQTL | MSBB | BM_22 | multi_gene_finemapping | analysis_result/multi_gene/MSBB/export/summary/context_specific/MSBB_BM_22_eQTL.exported.toploci.bed.gz |
| eQTL | MSBB | BM_36 | multi_gene_finemapping | analysis_result/multi_gene/MSBB/export/summary/context_specific/MSBB_BM_36_eQTL.exported.toploci.bed.gz |
| eQTL | MSBB | BM_44 | multi_gene_finemapping | analysis_result/multi_gene/MSBB/export/summary/context_specific/MSBB_BM_44_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | AC | multi_gene_finemapping | analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_AC_CUIMC1_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Ast_CUIMC1 | multi_gene_finemapping | analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_Ast_CUIMC1_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Ast_mega | multi_gene_finemapping | analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_Ast_mega_eQTL.exported.toploci.bed.gz |
| pQTL | ROSMAP | DLPFC_Bennett | multi_gene_finemapping | analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_DLPFC_Bennett_pQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | DLPFC | multi_gene_finemapping | analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_DLPFC_CUIMC1_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Exc_CUIMC1 | multi_gene_finemapping | analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_Exc_CUIMC1_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Exc_mega | multi_gene_finemapping | analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_Exc_mega_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Inh_CUIMC1 | multi_gene_finemapping | analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_Inh_CUIMC1_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Inh_mega | multi_gene_finemapping | analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_Inh_mega_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Mic_CUIMC1 | multi_gene_finemapping | analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_Mic_CUIMC1_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Mic_mega | multi_gene_finemapping | analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_Mic_mega_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | OPC_CUIMC1 | multi_gene_finemapping | analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_OPC_CUIMC1_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | OPC_mega | multi_gene_finemapping | analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_OPC_mega_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Oli_CUIMC1 | multi_gene_finemapping | analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_Oli_CUIMC1_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | Oli_mega | multi_gene_finemapping | analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_Oli_mega_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | PCC | multi_gene_finemapping | analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_PCC_CUIMC1_eQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | monocyte | multi_gene_finemapping | analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_monocyte_ROSMAP_eQTL.exported.toploci.bed.gz |
| eQTL | KNIGHT | Brain | trans_finemapping | analysis_result/trans/export/summary/context_specific/Knight_eQTL.exported.toploci.bed.gz |
| pQTL | KNIGHT | Brain | trans_finemapping | analysis_result/trans/export/summary/context_specific/Knight_pQTL.exported.toploci.bed.gz |
| eQTL | MSBB | BM10 | trans_finemapping | analysis_result/trans/export/summary/context_specific/MSBB_eQTL_BM10.exported.toploci.bed.gz |
| eQTL | MSBB | BM22 | trans_finemapping | analysis_result/trans/export/summary/context_specific/MSBB_eQTL_BM22.exported.toploci.bed.gz |
| eQTL | MSBB | BM36 | trans_finemapping | analysis_result/trans/export/summary/context_specific/MSBB_eQTL_BM36.exported.toploci.bed.gz |
| eQTL | MSBB | BM44 | trans_finemapping | analysis_result/trans/export/summary/context_specific/MSBB_eQTL_BM44.exported.toploci.bed.gz |
| pQTL | MSBB | BM36 | trans_finemapping | analysis_result/trans/export/summary/context_specific/MSBB_pQTL_BM36.exported.toploci.bed.gz |
| eQTL | ROSMAP | CUIMC1_AC | trans_finemapping | analysis_result/trans/export/summary/context_specific/ROSMAP_CUIMC1_eQTL_AC.exported.toploci.bed.gz |
| eQTL | ROSMAP | CUIMC1_Ast | trans_finemapping | analysis_result/trans/export/summary/context_specific/ROSMAP_CUIMC1_eQTL_Ast.exported.toploci.bed.gz |
| eQTL | ROSMAP | CUIMC1_DLPFC | trans_finemapping | analysis_result/trans/export/summary/context_specific/ROSMAP_CUIMC1_eQTL_DLPFC.exported.toploci.bed.gz |
| eQTL | ROSMAP | CUIMC1_Exc | trans_finemapping | analysis_result/trans/export/summary/context_specific/ROSMAP_CUIMC1_eQTL_Exc.exported.toploci.bed.gz |
| eQTL | ROSMAP | CUIMC1_Inh | trans_finemapping | analysis_result/trans/export/summary/context_specific/ROSMAP_CUIMC1_eQTL_Inh.exported.toploci.bed.gz |
| eQTL | ROSMAP | CUIMC1_Mic | trans_finemapping | analysis_result/trans/export/summary/context_specific/ROSMAP_CUIMC1_eQTL_Mic.exported.toploci.bed.gz |
| eQTL | ROSMAP | CUIMC1_OPC | trans_finemapping | analysis_result/trans/export/summary/context_specific/ROSMAP_CUIMC1_eQTL_OPC.exported.toploci.bed.gz |
| eQTL | ROSMAP | CUIMC1_Oli | trans_finemapping | analysis_result/trans/export/summary/context_specific/ROSMAP_CUIMC1_eQTL_Oli.exported.toploci.bed.gz |
| eQTL | ROSMAP | CUIMC1_PCC | trans_finemapping | analysis_result/trans/export/summary/context_specific/ROSMAP_CUIMC1_eQTL_PCC.exported.toploci.bed.gz |
| eQTL | ROSMAP | CUIMC1_monocyte | trans_finemapping | analysis_result/trans/export/summary/context_specific/ROSMAP_CUIMC1_eQTL_monocyte.exported.toploci.bed.gz |
| pQTL | ROSMAP | CUIMC1 | trans_finemapping | analysis_result/trans/export/summary/context_specific/ROSMAP_CUIMC1_pQTL.exported.toploci.bed.gz |
| eQTL | ROSMAP | MIT_Ast | trans_finemapping | analysis_result/trans/export/summary/context_specific/ROSMAP_MIT_eQTL_Ast.exported.toploci.bed.gz |
| eQTL | ROSMAP | MIT_Exc | trans_finemapping | analysis_result/trans/export/summary/context_specific/ROSMAP_MIT_eQTL_Exc.exported.toploci.bed.gz |
| eQTL | ROSMAP | MIT_Inh | trans_finemapping | analysis_result/trans/export/summary/context_specific/ROSMAP_MIT_eQTL_Inh.exported.toploci.bed.gz |
| eQTL | ROSMAP | MIT_Mic | trans_finemapping | analysis_result/trans/export/summary/context_specific/ROSMAP_MIT_eQTL_Mic.exported.toploci.bed.gz |
| eQTL | ROSMAP | MIT_OPC | trans_finemapping | analysis_result/trans/export/summary/context_specific/ROSMAP_MIT_eQTL_OPC.exported.toploci.bed.gz |
| eQTL | ROSMAP | MIT_Oli | trans_finemapping | analysis_result/trans/export/summary/context_specific/ROSMAP_MIT_eQTL_Oli.exported.toploci.bed.gz |
| eQTL | ROSMAP | mega_Ast | trans_finemapping | analysis_result/trans/export/summary/context_specific/ROSMAP_mega_eQTL_Ast.exported.toploci.bed.gz |
| eQTL | ROSMAP | mega_Exc | trans_finemapping | analysis_result/trans/export/summary/context_specific/ROSMAP_mega_eQTL_Exc.exported.toploci.bed.gz |
| eQTL | ROSMAP | mega_Inh | trans_finemapping | analysis_result/trans/export/summary/context_specific/ROSMAP_mega_eQTL_Inh.exported.toploci.bed.gz |
| eQTL | ROSMAP | mega_Mic | trans_finemapping | analysis_result/trans/export/summary/context_specific/ROSMAP_mega_eQTL_Mic.exported.toploci.bed.gz |
| eQTL | ROSMAP | mega_OPC | trans_finemapping | analysis_result/trans/export/summary/context_specific/ROSMAP_mega_eQTL_OPC.exported.toploci.bed.gz |
| eQTL | ROSMAP | mega_Oli | trans_finemapping | analysis_result/trans/export/summary/context_specific/ROSMAP_mega_eQTL_Oli.exported.toploci.bed.gz |
| metabolome | ROSMAP | - | trans_finemapping | analysis_result/trans/export/summary/context_specific/ROSMAP_metabolome.exported.toploci.bed.gz |
| eQTL | STARNET | Mac | trans_finemapping | analysis_result/trans/export/summary/context_specific/STARNET_eQTL.exported.toploci.bed.gz |
| glycoQTL | ROSMAP | DLPFC_Klein_adjusted | trans_finemapping | analysis_result/trans/export/summary/context_specific/ROSMAP_adjusted_gpQTL.exported.toploci.bed.gz |
| glycoQTL | ROSMAP | DLPFC_Klein_unadjusted | trans_finemapping | analysis_result/trans/export/summary/context_specific/ROSMAP_gpQTL.exported.toploci.bed.gz |
| GWAS | AD_Bellenguez_2022 | - | AD_GWAS_finemapping | analysis_result/AD_GWAS_finemapping/export/context_specific/AD_Bellenguez_2022.exported.toploci.bed.gz |
| GWAS | AD_Jansen_2021 | - | AD_GWAS_finemapping | analysis_result/AD_GWAS_finemapping/export/context_specific/AD_Jansen_2021.exported.toploci.bed.gz |
| GWAS | AD_Wightman_Full_2021 | - | AD_GWAS_finemapping | analysis_result/AD_GWAS_finemapping/export/context_specific/AD_Wightman_Full_2021.exported.toploci.bed.gz |
| GWAS | AD_Bellenguez_EADB_2022 | - | AD_GWAS_finemapping | analysis_result/AD_GWAS_finemapping/export/context_specific/AD_Bellenguez_EADB_2022.exported.toploci.bed.gz |
| GWAS | AD_Kunkle_Stage1_2019 | - | AD_GWAS_finemapping | analysis_result/AD_GWAS_finemapping/export/context_specific/AD_Kunkle_Stage1_2019.exported.toploci.bed.gz |
| GWAS | AD_Wightman_Excluding23andMe_2021 | - | AD_GWAS_finemapping | analysis_result/AD_GWAS_finemapping/export/context_specific/AD_Wightman_Excluding23andMe_2021.exported.toploci.bed.gz |
| GWAS | AD_Wightman_ExcludingUKBand23andME_2021 | - | AD_GWAS_finemapping | analysis_result/AD_GWAS_finemapping/export/context_specific/AD_Wightman_ExcludingUKBand23andME_2021.exported.toploci.bed.gz |
| GWAS | AD_Bellenguez_EADI_2022 | - | AD_GWAS_finemapping | analysis_result/AD_GWAS_finemapping/export/context_specific/AD_Bellenguez_EADI_2022.exported.toploci.bed.gz |
| QTL | ROSMAP | xQTL_only_colocalization | multi_context_colocalization | analysis_result/ColocBoost/export/summary/xqtl_only_ROSMAP_colocboost_addend_export_release.bed.gz |
| QTL & GWAS | ROSMAP & AD | AD_xQTL_colocalization | multi_context_colocalization | analysis_result/ColocBoost/export/summary/AD_xQTL_ROSMAP_colocboost_export_release.bed.gz |
| QTL | MSBB | xQTL_only_colocalization | multi_context_colocalization | analysis_result/ColocBoost/export/summary/xqtl_only_MSBB_colocboost_export_release_sorted.bed.gz |
| QTL & GWAS | MSBB & AD | AD_xQTL_colocalization | multi_context_colocalization | analysis_result/ColocBoost/export/summary/AD_xQTL_MSBB_colocboost_export_release_sorted.bed.gz |
| QTL | KNIGHT | xQTL_only_colocalization | multi_context_colocalization | analysis_result/ColocBoost/export/summary/xqtl_only_KNIGHT_colocboost_export_release_sorted.bed.gz |
| QTL & GWAS | KNIGHT & AD | AD_xQTL_colocalization | multi_context_colocalization | analysis_result/ColocBoost/export/summary/AD_xQTL_KNIGHT_colocboost_export_release_sorted.bed.gz |
| QTL | MiGA | xQTL_only_colocalization | multi_context_colocalization | analysis_result/ColocBoost/export/summary/xqtl_only_MIGA_colocboost_export_release_sorted.bed.gz |
| QTL & GWAS | MiGA & AD | AD_xQTL_colocalization | multi_context_colocalization | analysis_result/ColocBoost/export/summary/AD_xQTL_MIGA_colocboost_export_release_sorted.bed.gz |
| GWAS | AD | AD_meta_colocalization | multi_context_colocalization | analysis_result/ColocBoost/export/summary/ad_meta_colocboost_export_filtered.bed.gz |
| Gene & GWAS | ROSMAP & MSBB & AD | - | TWAS | analysis_result/twas/AD/export/summary/FunGen_twas.exported.bed.gz |
| Gene & GWAS | ROSMAP & AD | - | cTWAS | analysis_result/ctwas/export/summary/FunGen_ctwas.exported.bed.gz |
| mQTL & haQTL   | ROSMAP & MSSB & Knight     | Brain       | single_context_finemapping (fSuSiE) | analysis_result/finemapping_twas/fsusie/export/summary/FunGen_xQTL_epi.bulk.exported.bed.gz                  |
| haQTL    | ROSMAP      | DLPFC          | single_context_finemapping (fSuSiE) | analysis_result/finemapping_twas/fsusie/export/summary/context_specific/ROSMAP_DLPFC_haQTL.exported.toploci.bed.gz |
| mQTL     | ROSMAP      | DLPFC          | single_context_finemapping (fSuSiE) | analysis_result/finemapping_twas/fsusie/export/summary/context_specific/ROSMAP_DLPFC_mQTL.exported.toploci.bed.gz  |
| mQTL     | KNIGHT  | Brain             | single_context_finemapping (fSuSiE) | analysis_result/finemapping_twas/fsusie/export/summary/context_specific/KnightADRC_mQTL.exported.toploci.bed.gz    |
| mQTL     | MSBB        | -              | single_context_finemapping (fSuSiE) | analysis_result/finemapping_twas/fsusie/export/summary/context_specific/MSBB_mQTL.exported.toploci.bed.gz         |
| snATAC   | ROSMAP      | MIT_OPC       | single_context_finemapping (fSuSiE) | analysis_result/snatac_fsusie/top_loci/context_specific/ROSMAP_snATAC_MIT_OPC.exported.toploci.bed.gz                  |
| snATAC   | ROSMAP      | MIT_Exc       | single_context_finemapping (fSuSiE) | analysis_result/snatac_fsusie/top_loci/context_specific/ROSMAP_snATAC_MIT_Exc.exported.toploci.bed.gz                  |
| snATAC   | ROSMAP      | MIT_Ast       | single_context_finemapping (fSuSiE) | analysis_result/snatac_fsusie/top_loci/context_specific/ROSMAP_snATAC_MIT_Ast.exported.toploci.bed.gz                  |
| snATAC   | ROSMAP      | MIT_Oli       | single_context_finemapping (fSuSiE) | analysis_result/snatac_fsusie/top_loci/context_specific/ROSMAP_snATAC_MIT_Oli.exported.toploci.bed.gz                  |
| snATAC   | ROSMAP      | MIT_Mic       | single_context_finemapping (fSuSiE) | analysis_result/snatac_fsusie/top_loci/context_specific/ROSMAP_snATAC_MIT_Mic.exported.toploci.bed.gz                  |
| snATAC   | ROSMAP      | MIT_Inh       | single_context_finemapping (fSuSiE) | analysis_result/snatac_fsusie/top_loci/context_specific/ROSMAP_snATAC_MIT_Inh.exported.toploci.bed.gz                  |
| snATAC  & AD   | ROSMAP & AD      | MIT Celltypes      | pairwise_colocalization | analysis_result/coloc/fsusie_AD_coloc/snATAC_MIT_AD_coloc_export_filtered.bed.gz                  |
| Bulk mQTL and haQTL  & AD   | ROSMAP & AD      | Brain      | pairwise_colocalization | analysis_result/coloc/fsusie_AD_coloc/bulk_fsusie_AD_coloc_export_filtered.bed.gz                  |
| snATAC  & Gene   | ROSMAP      | MIT Celltypes      | pairwise_colocalization | analysis_result/coloc/fsusie_AD_coloc/snatac_ROSMAP.coloc.tsv.gz                  |

* AD_xQTL_colocalization results include "AD_Bellenguez_2022", "AD_Wightman_Excluding23andMe_2021", "AD_Wightman_ExcludingUKBand23andME_2021", "AD_Kunkle_Stage1_2019", "AD_Wightman_Full_2021"

### Data Format Specifications

Each exported file follows a standardized BED format with compressed storage (`.gz`), containing top loci from respective QTL analyses. Files are optimized for downstream genomic and transcriptomic research applications.

#### SuSiE/mvSuSiE fine-mapping columns

| Column Name           | Type      | Description                                                                 |
|-----------------------|-----------|-----------------------------------------------------------------------------|
| `chr`                 | integer   | Chromosome number                                                           |
| `start`               | integer   | Genomic start coordinate (0-based, BED convention)                          |
| `end`                 | integer   | Genomic end coordinate (1-based, BED convention)                            |
| `a1`                  | character | Effect allele                                                               |
| `a2`                  | character | Reference allele                                                            |
| `variant_ID`          | character | Unique variant identifier (format: `chr:pos:ref:alt`)                       |
| `gene_ID`             | character | Ensembl gene identifier                                                     |
| `event_ID`            | character | Unique QTL signal identifier (context + gene). Present only for significant signals passing LFSR threshold |
| `cs_coverage_0.95`    | integer   | Credible set index for 95% coverage (purity > 0.8), 0 if not in set       |
| `cs_coverage_0.7`     | integer   | Credible set index for 70% coverage (purity > 0.8), 0 if not in set       |
| `cs_coverage_0.5`     | integer   | Credible set index for 50% coverage (purity > 0.8), 0 if not in set       |
| `cs_coverage_0.95_purity0.5` | integer | Credible set index for 95% coverage (purity > 0.5), when available    |
| `cs_coverage_0.7_purity0.5`  | integer | Credible set index for 70% coverage (purity > 0.5), when available    |
| `cs_coverage_0.5_purity0.5`  | integer | Credible set index for 50% coverage (purity > 0.5), when available    |
| `PIP`                 | double    | Posterior inclusion probability for variant causality                       |
| `conditional_effect`  | double    | Effect size from conditional analysis model                                 |
| `lfsr`                | double    | Local False Sign Rate (multi-context/multi-gene analyses only). Probability of incorrect effect direction. Lower values indicate higher confidence. NA values indicate variants not passing filtering threshold |

#### ColocBoost-specific Columns

| Column Name       | Type      | Description                                                                                                             |
|-------------------|-----------|-------------------------------------------------------------------------------------------------------------------------|
| `event_ID`        | character | Trait combination colocalizing within the same 95% colocalization confidence set (CoS)                                  |
| `cos_ID`          | character | Unique identifier for each 95% colocalization confidence set                                                           |
| `vcp`             | double    | Variant Colocalization Probability - estimated probability of variant sharing among colocalized traits                   |
| `cos_npc`         | double    | Normalized probability of colocalization within CoS, distinguishing shared from trait-specific signals                   |
| `min_npc_outcome` | double    | Minimum normalized probability across traits in the CoS                                                                |
| `coef`            | double    | Regression coefficient from ColocBoost model for each trait                                                            |

#### TWAS-Specific Columns

| Column Name           | Type      | Description                                                                                                                                          |
|-----------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| `TADB_start`          | integer   | Start coordinate of extended TADB window for cis-fine mapping ([TADB BED reference](https://github.com/cumc/xqtl-analysis/blob/main/resource/TADB_enhanced_cis.coding.bed)) |
| `TADB_end`            | integer   | End coordinate of extended TADB window                                                                                                              |
| `is_imputable`        | logical   | Gene-context pair has predictive models with CV R² > 0.01 and p < 0.05 in at least one method                                                       |
| `rsq_cv`              | double    | Cross-validated R² for expression prediction performance                                                                                            |
| `pval_cv`             | double    | Cross-validation p-value for expression prediction performance                                                                                      |
| `is_selected_method`  | logical   | Indicates optimal method (highest CV R² with p < 0.05) for gene-context pair                                                                        |
| `block`               | character | LD block containing gene TSS, based on predefined LD partitions                                                                                     |

#### cTWAS-Specific Columns

| Column Name           | Type      | Description                                                                                          |
|-----------------------|-----------|------------------------------------------------------------------------------------------------------|
| `region_id`           | character | Predefined LD partitions, containing chromosome number, start and end of the genomic position        |
| `susie_pip`           | double    | PIP (posterior inclusion probability) for each molecular trait and variant                           |
| `mu`                  | double    | Effect size (posterior means)                                                                        |
| `cs`                  | character | Credible set identifier                                                                              |
| `type`                | character | Indicates whether the variant is a 'SNP' or a gene/molecular trait ('eQTL', 'pQTL', 'sQTL', etc.)    |

For detailed documentation, please refer to [cTWAS (causal-TWAS)](https://github.com/xinhe-lab/ctwas/tree/main)

#### fSuSiE-Specific Columns

| Column Name          | Type      | Description                                                                 |
|----------------------|-----------|-----------------------------------------------------------------------------|
| `maf`                | numeric   | Minor allele frequency                                                      |
| `grid_resolution`    | integer   | Grid resolution used (typically 512 or 1024 rows)                           |
| `cs_id`              | string    | Credible set identifier within context and TAD                              |
| `cs_root`            | string    | Unified root name for overlapping credible sets in same context             |
| `effect_peak_start`  | integer   | Genomic start position of effect peak                                       |
| `effect_peak_end`    | integer   | Genomic end position of effect peak                                         |
| `effect_peak_index`  | integer   | Index of effect peak in 1024-grid TAD representation                        |
| `grid_positions`     | numeric   | Comma-separated grid positions covered by effect peak                       |
| `grid_effects`       | string    | Comma-separated effect sizes (beta) at each grid position                   |
| `epi_mark_positions` | string    | Comma-separated genomic positions of covered epigenetic marks               |
| `epi_mark_names`     | string    | Comma-separated names of covered epigenetic marks                           |
| `epi_mark_effects`   | string    | Comma-separated interpolated effects for epigenetic marks                   |

#### SuSiE-COLOC Colocalization Columns

Between xQTL and AD, pairwise.

| Column Name   | Type      | Description                                                                                                 |
|---------------|-----------|-------------------------------------------------------------------------------------------------------------|
| `cos_id`      | character | Unique identifier for 95% pairwise colocalization confidence set                                            |
| `coloc_index` | integer   | Index of pairwise colocalization test in SNP-level COLOC results                                            |
| `nsnps`       | integer   | Number of SNPs included in colocalization test                                                            |
| `SNP_PPH4`    | double    | Posterior probability of SNP causality for shared signal given H4 hypothesis                               |
| `TADB_region` | character | TAD boundary identifier where fSuSiE was conducted                                                         |
| `AD`          | character | Alzheimer's disease GWAS dataset name (SuSiE-RSS fine-mapped)                                              |
| `xQTL`        | character | xQTL dataset name (fSuSiE fine-mapped)                                                                     |
| `xQTL_hit`    | character | Lead SNP of fine-mapped effect in xQTL dataset                                                            |
| `AD_hit`      | character | Lead SNP of fine-mapped effect in AD GWAS dataset                                                         |
| `xQTL_L`      | integer   | Fine-mapped effect index in xQTL (from fSuSiE)                                                            |
| `AD_L`        | integer   | Fine-mapped effect index in AD GWAS (from SuSiE-RSS)                                                      |
| `PP.H0.abf`   | double    | Posterior probability of H0: no association in either study                                                |
| `PP.H1.abf`   | double    | Posterior probability of H1: association in xQTL only                                                      |
| `PP.H2.abf`   | double    | Posterior probability of H2: association in AD GWAS only                                                   |
| `L_PP.H3.abf` | double    | Posterior probability of H3: distinct causal variants at effect level                                       |
| `L_PP.H4.abf` | double    | Posterior probability of H4: shared causal variant between xQTL and AD at effect level                      |

Consolidated single context xQTL loci

#### `FunGen_xQTL_single_context_top_loci_integrated.rds`

All single-context SuSiE fine-mapping results in one R data frame: 13,393,657 rows, one per variant and molecular trait. It covers 51 contexts (eQTL, productive and unproductive sQTL, pQTL and glycoQTL), 634,382 molecular traits, 18,638 genes and 5,147,485 variants. Results from fSuSiE (mQTL, haQTL, caQTL) are not in this file.

| Column | Type | Description |
|--------|------|-------------|
| `#chr`, `start`, `end` | integer | Variant position (`start` is 0-based, `end` is 1-based) |
| `a1`, `a2` | character | Alleles |
| `variant_ID` | character | Variant as `chr:pos:a2:a1` |
| `gene_ID` | character | Ensembl gene ID |
| `event_ID` | character | Molecular trait, prefixed with its context |
| `cs_coverage_0.95`, `cs_coverage_0.7`, `cs_coverage_0.5` | integer | Credible set the variant belongs to at 95%, 70% and 50% coverage; 0 means it is in none |
| `PIP` | double | Posterior inclusion probability |
| `conditional_effect` | double | Effect estimate conditional on the other effects in the model |
| `resource` | character | Context (dataset) the result comes from, for example `Knight_eQTL_brain` |
| `pip_sum` | double | Sum of PIP over all variants listed for the molecular trait |
| `event_ID_n_detectable` | integer | Number of detectable 95% credible sets for the molecular trait (all variant pairs with absolute LD correlation ≥ 0.8) |
| `event_ID_n_mappable` | integer | Number of mappable credible sets for the molecular trait (detectable sets with three or fewer variants) |
| `event_ID_detectable_variant_count` | integer | Number of variants considered for the molecular trait's detectable sets |

#### `FunGen_xQTL_AD_loci_context_method_summary.fsusie.rds`

AD GWAS fine-mapped variants with the xQTL evidence found for them, in one R data frame: 47,722 rows, one per variant, AD GWAS, gene and type of xQTL analysis. It covers 1,517 variants in 56 regions, 143 genes, 97 xQTL contexts and eight AD GWAS. Despite the file name, the rows come from all analysis types, not only fSuSiE.

| Column | Type | Description |
|--------|------|-------------|
| `variant_ID`, `variant_id` | character | Variant as `chr:pos:a2:a1` (with and without the `chr` prefix) |
| `#chr`, `start`, `end`, `a1`, `a2` | | Variant position and alleles |
| `gene_ID` | character | Ensembl gene ID of the xQTL target |
| `event_ID` | character | xQTL molecular traits that share the variant, separated by `;` |
| `contexts` | character | xQTL contexts of those traits, separated by `,` |
| `study` | character | AD GWAS, for example `AD_Bellenguez_2022` |
| `region` | character | Fine-mapping region of the AD GWAS |
| `gwas_cs` | character | AD GWAS credible set the variant belongs to (`study:region:set`) |
| `cs_coverage_0.95_min_corr`, `cs_coverage_0.7_min_corr`, `cs_coverage_0.5_min_corr` | double | AD GWAS credible set at 95%, 70% and 50% coverage with the purity filter; -1 means the variant is in none |
| `pip`, `z` | double | AD GWAS posterior inclusion probability and z-score of the variant (missing for 7% of rows) |
| `resource` | character | Type of xQTL analysis: `single_context`, `multi_context`, `multi_gene`, `ColocBoost`, `builk_fsusie_coloc` (bulk fSuSiE colocalization) or `snatac_fsusie_coloc` |

### Usage Guidelines

#### Prioritization Strategies

- **Causal variant identification**: Filter by `cs_coverage_0.95 > 0` or `PIP > 0.1` to identify high-confidence causal variants
- **Significant results only**: Restrict analysis to rows with non-missing `event_ID` values for significance-filtered datasets
- **Gene-level visualization**: Group results by `context` and `gene_ID` to examine credible sets across studies
- **Multi-context analysis**: Rows with missing `event_ID` from multi-context analyses represent variants not passing LFSR threshold but retained for completeness

#### Integration Notes

- All files use standardized variant naming convention for cross-dataset integration
- Credible set columns (`cs_coverage_*`) indicate membership probability thresholds with varying purity requirements
- For epigenetic marks in fSuSiE results, note that `epi_mark_effects` are interpolated from neighboring grid effects rather than direct measurements

## xQTL Association Results Summary

The following table provides paths to marginal QTL association results, including linear regression (LR), quantile regression (QR), and interaction analyses testing for genotype-by-sex, genotype-by-APOE, and other context-dependent effects.


| Data Type | Cohort | Modality | Method | Path |
|-----------|--------|----------|--------|------|
| eQTL | KNIGHT | Brain | LR | analysis_result/marginal_significant_qtl/cis_association/KNIGHT/eQTL/Brain/LR/ |
| eQTL | MiGA | GFM | LR | analysis_result/marginal_significant_qtl/cis_association/MiGA/eQTL/GFM/LR/ |
| eQTL | MiGA | GTS | LR | analysis_result/marginal_significant_qtl/cis_association/MiGA/eQTL/GTS/LR/ |
| eQTL | MiGA | SVZ | LR | analysis_result/marginal_significant_qtl/cis_association/MiGA/eQTL/SVZ/LR/ |
| eQTL | MiGA | THA | LR | analysis_result/marginal_significant_qtl/cis_association/MiGA/eQTL/THA/LR/ |
| eQTL | MSBB | BM_10 | LR | analysis_result/marginal_significant_qtl/cis_association/MSBB/eQTL/BM_10/LR/ |
| eQTL | MSBB | BM_22 | LR | analysis_result/marginal_significant_qtl/cis_association/MSBB/eQTL/BM_22/LR/ |
| eQTL | MSBB | BM_36 | LR | analysis_result/marginal_significant_qtl/cis_association/MSBB/eQTL/BM_36/LR/ |
| eQTL | MSBB | BM_44 | LR | analysis_result/marginal_significant_qtl/cis_association/MSBB/eQTL/BM_44/LR/ |
| eQTL | ROSMAP | AC | LR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/AC/LR/ |
| eQTL | ROSMAP | DLPFC | LR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/DLPFC/LR/ |
| eQTL | ROSMAP | monocyte | LR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/monocyte/LR/ |
| eQTL | ROSMAP | PCC | LR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/PCC/LR/ |
| eQTL | ROSMAP | snuc_CUIMC1/Ast | LR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_CUIMC1/Ast/LR/ |
| eQTL | ROSMAP | snuc_CUIMC1/Exc | LR | analysis_result/marginal_significant_qtl/cisAssociational/ROSMAP/eQTL/snuc_CUIMC1/Exc/LR/ |
| eQTL | ROSMAP | snuc_CUIMC1/Inh | LR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_CUIMC1/Inh/LR/ |
| eQTL | ROSMAP | snuc_CUIMC1/Mic | LR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_CUIMC1/Mic/LR/ |
| eQTL | ROSMAP | snuc_CUIMC1/OPC | LR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_CUIMC1/OPC/LR/ |
| eQTL | ROSMAP | snuc_CUIMC1/Oli | LR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_CUIMC1/Oli/LR/ |
| eQTL | ROSMAP | snuc_MIT/Ast | LR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_MIT/Ast/LR/ |
| eQTL | ROSMAP | snuc_MIT/Exc | LR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_MIT/Exc/LR/ |
| eQTL | ROSMAP | snuc_MIT/Inh | LR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_MIT/Inh/LR/ |
| eQTL | ROSMAP | snuc_MIT/Mic | LR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_MIT/Mic/LR/ |
| eQTL | ROSMAP | snuc_MIT/OPC | LR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_MIT/OPC/LR/ |
| eQTL | ROSMAP | snuc_MIT/Oli | LR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_MIT/Oli/LR/ |
| eQTL | ROSMAP | snuc_mega/Ast | LR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_mega/Ast/LR/ |
| eQTL | ROSMAP | snuc_mega/Exc | LR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_mega/Exc/LR/ |
| eQTL | ROSMAP | snuc_mega/Inh | LR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_mega/Inh/LR/ |
| eQTL | ROSMAP | snuc_mega/Mic | LR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_mega/Mic/LR/ |
| eQTL | ROSMAP | snuc_mega/OPC | LR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_mega/OPC/LR/ |
| eQTL | ROSMAP | snuc_mega/Oli | LR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_mega/Oli/LR/ |
| eQTL | STARNET | - | LR | analysis_result/marginal_significant_qtl/cis_association/STARNET/eQTL/LR/ |
| eQTL | KNIGHT | Brain | msex interaction | analysis_result/marginal_significant_qtl/cis_association/KNIGHT/eQTL/Brain/interaction/msex/ |
| eQTL | MiGA | GFM | msex interaction | analysis_result/marginal_significant_qtl/cis_association/MiGA/eQTL/GFM/interaction/msex/ |
| eQTL | MiGA | GTS | msex interaction | analysis_result/marginal_significant_qtl/cis_association/MiGA/eQTL/GTS/interaction/msex/ |
| eQTL | MiGA | SVZ | msex interaction | analysis_result/marginal_significant_qtl/cis_association/MiGA/eQTL/SVZ/interaction/msex/ |
| eQTL | MiGA | THA | msex interaction | analysis_result/marginal_significant_qtl/cis_association/MiGA/eQTL/THA/interaction/msex/ |
| eQTL | MSBB | BM_10 | msex interaction | analysis_result/marginal_significant_qtl/cis_association/MSBB/eQTL/BM_10/interaction/msex/ |
| eQTL | MSBB | BM_22 | msex interaction | analysis_result/marginal_significant_qtl/cis_association/MSBB/eQTL/BM_22/interaction/msex/ |
| eQTL | MSBB | BM_36 | msex interaction | analysis_result/marginal_significant_qtl/cis_association/MSBB/eQTL/BM_36/interaction/msex/ |
| eQTL | MSBB | BM_44 | msex interaction | analysis_result/marginal_significant_qtl/cis_association/MSBB/eQTL/BM_44/interaction/msex/ |
| eQTL | ROSMAP | AC | msex interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/AC/interaction/msex/ |
| eQTL | ROSMAP | DLPFC | msex interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/DLPFC/interaction/msex/ |
| eQTL | ROSMAP | monocyte | msex interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/monocyte/interaction/msex/ |
| eQTL | ROSMAP | PCC | msex interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/PCC/interaction/msex/ |
| eQTL | ROSMAP | snuc_CUIMC1/Ast | msex interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_CUIMC1/Ast/interaction/msex/ |
| eQTL | ROSMAP | snuc_CUIMC1/Exc | msex interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_CUIMC1/Exc/interaction/msex/ |
| eQTL | ROSMAP | snuc_CUIMC1/Inh | msex interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_CUIMC1/Inh/interaction/msex/ |
| eQTL | ROSMAP | snuc_CUIMC1/Mic | msex interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_CUIMC1/Mic/interaction/msex/ |
| eQTL | ROSMAP | snuc_CUIMC1/OPC | msex interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_CUIMC1/OPC/interaction/msex/ |
| eQTL | ROSMAP | snuc_CUIMC1/Oli | msex interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_CUIMC1/Oli/interaction/msex/ |
| eQTL | ROSMAP | snuc_MIT/Ast | msex interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_MIT/Ast/interaction/msex/ |
| eQTL | ROSMAP | snuc_MIT/Exc | msex interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_MIT/Exc/interaction/msex/ |
| eQTL | ROSMAP | snuc_MIT/Inh | msex interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_MIT/Inh/interaction/msex/ |
| eQTL | ROSMAP | snuc_MIT/Mic | msex interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_MIT/Mic/interaction/msex/ |
| eQTL | ROSMAP | snuc_MIT/OPC | msex interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_MIT/OPC/interaction/msex/ |
| eQTL | ROSMAP | snuc_MIT/Oli | msex interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_MIT/Oli/interaction/msex/ |
| eQTL | ROSMAP | snuc_mega/Ast | msex interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_mega/Ast/interaction/msex/ |
| eQTL | ROSMAP | snuc_mega/Exc | msex interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_mega/Exc/interaction/msex/ |
| eQTL | ROSMAP | snuc_mega/Inh | msex interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_mega/Inh/interaction/msex/ |
| eQTL | ROSMAP | snuc_mega/Mic | msex interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_mega/Mic/interaction/msex/ |
| eQTL | ROSMAP | snuc_mega/OPC | msex interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_mega/OPC/interaction/msex/ |
| eQTL | ROSMAP | snuc_mega/Oli | msex interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_mega/Oli/interaction/msex/ |
| eQTL | STARNET | - | msex interaction | analysis_result/marginal_significant_qtl/cis_association/STARNET/eQTL/interaction/msex/ |
| eQTL | ROSMAP | AC | APOE interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/AC/interaction/APOE/ |
| eQTL | ROSMAP | DLPFC | APOE interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/DLPFC/interaction/APOE/ |
| eQTL | ROSMAP | monocyte | APOE interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/monocyte/interaction/APOE/ |
| eQTL | ROSMAP | PCC | APOE interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/PCC/interaction/APOE/ |
| eQTL | ROSMAP | snuc_CUIMC1/Ast | APOE interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_CUIMC1/Ast/interaction/APOE/ |
| eQTL | ROSMAP | snuc_CUIMC1/Exc | APOE interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_CUIMC1/Exc/interaction/APOE/ |
| eQTL | ROSMAP | snuc_CUIMC1/Inh | APOE interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_CUIMC1/Inh/interaction/APOE/ |
| eQTL | ROSMAP | snuc_CUIMC1/Mic | APOE interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_CUIMC1/Mic/interaction/APOE/ |
| eQTL | ROSMAP | snuc_CUIMC1/OPC | APOE interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_CUIMC1/OPC/interaction/APOE/ |
| eQTL | ROSMAP | snuc_CUIMC1/Oli | APOE interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_CUIMC1/Oli/interaction/APOE/ |
| eQTL | ROSMAP | snuc_MIT/Ast | APOE interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_MIT/Ast/interaction/APOE/ |
| eQTL | ROSMAP | snuc_MIT/Exc | APOE interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_MIT/Exc/interaction/APOE/ |
| eQTL | ROSMAP | snuc_MIT/Inh | APOE interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_MIT/Inh/interaction/APOE/ |
| eQTL | ROSMAP | snuc_MIT/Mic | APOE interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_MIT/Mic/interaction/APOE/ |
| eQTL | ROSMAP | snuc_MIT/OPC | APOE interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_MIT/OPC/interaction/APOE/ |
| eQTL | ROSMAP | snuc_MIT/Oli | APOE interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_MIT/Oli/interaction/APOE/ |
| eQTL | ROSMAP | snuc_mega/Ast | APOE interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_mega/Ast/interaction/APOE/ |
| eQTL | ROSMAP | snuc_mega/Exc | APOE interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_mega/Exc/interaction/APOE/ |
| eQTL | ROSMAP | snuc_mega/Inh | APOE interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_mega/Inh/interaction/APOE/ |
| eQTL | ROSMAP | snuc_mega/Mic | APOE interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_mega/Mic/interaction/APOE/ |
| eQTL | ROSMAP | snuc_mega/OPC | APOE interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_mega/OPC/interaction/APOE/ |
| eQTL | ROSMAP | snuc_mega/Oli | APOE interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_mega/Oli/interaction/APOE/ |
| pQTL | KNIGHT | Brain | LR | analysis_result/marginal_significant_qtl/cis_association/KNIGHT/pQTL/Brain/LR/ |
| pQTL | MSBB | - | LR | analysis_result/marginal_significant_qtl/cis_association/MSBB/pQTL/LR/ |
| pQTL | ROSMAP | DLPFC | LR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/pQTL/DLPFC/LR/ |
| pQTL | KNIGHT | Brain | msex interaction | analysis_result/marginal_significant_qtl/cis_association/KNIGHT/pQTL/Brain/interaction/msex/ |
| pQTL | MSBB | - | msex interaction | analysis_result/marginal_significant_qtl/cis_association/MSBB/pQTL/interaction/msex/ |
| pQTL | ROSMAP | DLPFC | msex interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/pQTL/DLPFC/interaction/msex/ |
| pQTL | ROSMAP | DLPFC | APOE interaction | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/pQTL/DLPFC/interaction/APOE/ |
| eQTL | KNIGHT | Brain | QR | analysis_result/marginal_significant_qtl/cis_association/KNIGHT/eQTL/Brain/QR/ |
| eQTL | MiGA | GFM | QR | analysis_result/marginal_significant_qtl/cis_association/MiGA/eQTL/GFM/QR/ |
| eQTL | MiGA | GTS | QR | analysis_result/marginal_significant_qtl/cis_association/MiGA/eQTL/GTS/QR/ |
| eQTL | MiGA | SVZ | QR | analysis_result/marginal_significant_qtl/cis_association/MiGA/eQTL/SVZ/QR/ |
| eQTL | MiGA | THA | QR | analysis_result/marginal_significant_qtl/cis_association/MiGA/eQTL/THA/QR/ |
| eQTL | MSBB | BM_10 | QR | analysis_result/marginal_significant_qtl/cis_association/MSBB/eQTL/BM_10/QR/ |
| eQTL | MSBB | BM_22 | QR | analysis_result/marginal_significant_qtl/cis_association/MSBB/eQTL/BM_22/QR/ |
| eQTL | MSBB | BM_36 | QR | analysis_result/marginal_significant_qtl/cis_association/MSBB/eQTL/BM_36/QR/ |
| eQTL | MSBB | BM_44 | QR | analysis_result/marginal_significant_qtl/cis_association/MSBB/eQTL/BM_44/QR/ |
| eQTL | ROSMAP | AC | QR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/AC/QR/ |
| eQTL | ROSMAP | DLPFC | QR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/DLPFC/QR/ |
| eQTL | ROSMAP | monocyte | QR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/monocyte/QR/ |
| eQTL | ROSMAP | PCC | QR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/PCC/QR/ |
| eQTL | ROSMAP | snuc_mega/Ast | QR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_mega/Ast/QR/ |
| eQTL | ROSMAP | snuc_mega/Exc | QR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_mega/Exc/QR/ |
| eQTL | ROSMAP | snuc_mega/Inh | QR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_mega/Inh/QR/ |
| eQTL | ROSMAP | snuc_mega/Mic | QR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_mega/Mic/QR/ |
| eQTL | ROSMAP | snuc_mega/OPC | QR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_mega/OPC/QR/ |
| eQTL | ROSMAP | snuc_mega/Oli | QR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/eQTL/snuc_mega/Oli/QR/ |
| pQTL | KNIGHT | Brain | QR | analysis_result/marginal_significant_qtl/cis_association/KNIGHT/pQTL/Brain/QR/ |
| pQTL | MSBB | - | QR | analysis_result/marginal_significant_qtl/cis_association/MSBB/pQTL/QR/ |
| pQTL | ROSMAP | DLPFC | QR | analysis_result/marginal_significant_qtl/cis_association/ROSMAP/pQTL/DLPFC/QR/ |

For detailed methodology and implementation, refer to our [analysis protocol documentation](https://github.com/StatFunGen/xqtl-protocol/blob/main/code/association_scan/TensorQTL/TensorQTL.ipynb).
