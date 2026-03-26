# ROSMAP study info

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) study: ROS is a longitudinal clinical-pathologic cohort study of aging and Alzheimer's disease (AD) run from Rush University that enrolled individuals from religious communities for longitudinal clinical analysis and brain donation. Participants were enrolled from more than 40 groups of religious orders (nuns, priests, brothers) across the United States. MAP is a longitudinal, epidemiologic clinical-pathologic cohort study of common chronic conditions of aging with an emphasis on decline in cognitive and motor function and risk of Alzheimer’s disease that began in 1997 and is run from Rush University.

- PI : Dr. Philip L. De Jager; Dr. David A. Bennett
- Institution : Columbia University Irving Medical Center; Rush University
- Grant number : U01AG061356, RF1AG057473, U01AG046152
- Contact person : Dr. Philip L. De Jager (pld2115@cumc.columbia.edu); Dr. David A. Bennett (david_a_bennett@rush.edu)
- Publication : PMID:35754708
- Acknowledgement : Study data were generated from postmortem brain tissue provided by the Religious Orders Study and Rush Memory and Aging Project (ROSMAP) cohort at Rush Alzheimer’s Disease Center, Rush University Medical Center, Chicago. This work was funded by NIH grants U01AG061356 (De Jager/Bennett), RF1AG057473 (De Jager/Bennett), and U01AG046152 (De Jager/Bennett) as part of the AMP-AD consortium, as well as NIH grants R01AG066831 (Menon) and U01AG072572 (De Jager/St George-Hyslop).
- Study name : Religious Orders Study and Rush Memory and Aging Project (ROSMAP)

- Disease : Alzheimer's disease
- Website&Logo : ROSMAP metadata page, https://www.synapse.org/#!Synapse:syn3157322
- Logo : NR
- Additional study information : NR

## Contact 

Xuanhe Chen (xuanhechenxhc@163.com)

For questions related to infomation on this page please contact the person above

## Other information

CU cluster: `/mnt/mfs/ctcn/datasets/rosmap/phenotypes/2022Feb08/dataset_707_basic_02-08-2022.clean.txt (050a105c617770b1e3a9c789ef3c3f98)`, `/mnt/mfs/ctcn/datasets/rosmap/phenotypes/2022Feb08/RADC_codebook_data_set_707_02-08-2022.pdf (baf4d16c799807b0c45548ccff0cf219)`

FTP: `/ftp_fgc_xqtl/ref-data/ROSMAP_covariates/dataset_707_basic_02-08-2022.clean.txt`, `RADC_codebook_data_set_707_02-08-2022/RADC_codebook_data_set_707_02-08-2022`

Above is a raw ROSMAP metadata contains comprehensive covariate information and the codebook explaining each column. Other than Age at death, Sex and PMI often use in our xQTL analysis, there are also interesting covariates for investigation such as education level, emotional neglect and Financial need etc.

## QTL Analyses

ROSMAP datasets were used in the following xQTL analyses in the FunGen-xQTL flagship paper:

| Dataset | Modality | QTL File |
|---------|----------|----------|
| DLPFC bulk RNA-seq | eQTL | [ROSMAP_DLPFC_expression_qtl](../qtl/eQTL/ROSMAP_DLPFC_expression_qtl.md) |
| PCC bulk RNA-seq | eQTL | [ROSMAP_PCC_expression_qtl](../qtl/eQTL/ROSMAP_PCC_expression_qtl.md) |
| AC bulk RNA-seq | eQTL | [ROSMAP_AC_expression_qtl](../qtl/eQTL/ROSMAP_AC_expression_qtl.md) |
| Monocyte RNA-seq | eQTL | [ROSMAP_monocyte_expression_qtl](../qtl/eQTL/ROSMAP_monocyte_expression_qtl.md) |
| Microglia RNA-seq | eQTL | [ROSMAP_microglia_expression_qtl](../qtl/eQTL/ROSMAP_microglia_expression_qtl.md) |
| snRNA-seq pseudo-bulk | eQTL | [ROSMAP_snRNAseq_pseudo_bulk_qtl](../qtl/eQTL/ROSMAP_snRNAseq_pseudo_bulk_qtl.md) |
| DLPFC RNA splicing | sQTL | [ROSMAP_DLPFC_splicing_qtl](../qtl/sQTL/ROSMAP_DLPFC_splicing_qtl.md) |
| PCC RNA splicing | sQTL | [ROSMAP_PCC_splicing_qtl](../qtl/sQTL/ROSMAP_PCC_splicing_qtl.md) |
| AC RNA splicing | sQTL | [ROSMAP_AC_splicing_qtl](../qtl/sQTL/ROSMAP_AC_splicing_qtl.md) |
| snRNA-seq splicing (ISSAC-seq) | sQTL | [ROSMAP_snuc_splicing_qtl](../qtl/sQTL/ROSMAP_snuc_splicing_qtl.md) |
| DLPFC methylation | mQTL | [ROSMAP_DLPFC_methylation_qtl](../qtl/mQTL/ROSMAP_DLPFC_methylation_qtl.md) |
| DLPFC H3K9ac ChIP-seq | haQTL | [ROSMAP_DLPFC_ChIPSeq_H3K9ac_qtl](../qtl/haQTL/ROSMAP_DLPFC_ChIPSeq_H3K9ac_qtl.md) |
| snATAC-seq (CUIMC + MIT) | caQTL | [ROSMAP_snuc_caQTL_qtl](../qtl/caQTL/ROSMAP_snuc_caQTL_qtl.md) |
| DLPFC proteomics | pQTL | [ROSMAP_DLPFC_proteomics_qtl](../qtl/pQTL/ROSMAP_DLPFC_proteomics_qtl.md) |
| DLPFC glycoproteomics | gpQTL | [ROSMAP_DLPFC_glycoproteomics_qtl](../qtl/gpQTL/ROSMAP_DLPFC_glycoproteomics_qtl.md) |
| Brain metabolomics | metaQTL | [ROSMAP_DLPFC_metabolomics_qtl](../qtl/metaQTL/ROSMAP_DLPFC_metabolomics_qtl.md) |

Flagship paper analyses include fine-mapping ([syn69670592](https://www.synapse.org/Synapse:syn69670592)), TWAS models ([syn69670600](https://www.synapse.org/Synapse:syn69670600)), and colocalization ([syn69670597](https://www.synapse.org/Synapse:syn69670597), [syn69865816](https://www.synapse.org/Synapse:syn69865816)).
