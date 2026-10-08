---
type: qtl
modality: gpQTL
cohort: ROSMAP
context: DLPFC
status:
synapse_ids: [syn69865744, syn70094703, syn76495192, syn77828034, syn76489398, syn76490205, syn75180848]
lead_analysts: []
last_verified:
---

# ROSMAP DLPFC glycoproteomics QTL

This page documents the glycoproteomics QTL (gpQTL) analysis of dorsolateral prefrontal cortex (DLPFC) tissue from the Religious Orders Study (ROS) and the Rush Memory and Aging Project (MAP). The [ROSMAP study page](../../study_info/ROSMAP.md) gives an overview of the cohort.

## Study overview

- **Study name.** ROSMAP glycoproteomics QTL.
- **Description.** Summary statistics from the FGC xQTL pipeline for the ROSMAP proteomics QTL analysis.
- **Sample phenotypes.** Sex, age, race and other sample information are in the ROSMAP metadata, described under "Other information" on the [ROSMAP study page](../../study_info/ROSMAP.md).

## Analysis notebooks

### Association scan with TensorQTL and summary statistics standardization

- [TensorQTL.ipynb](https://github.com/cumc/xqtl-protocol/blob/main/code/association_scan/TensorQTL/TensorQTL.ipynb) generates the TensorQTL cis association results for all QTL types.
- [ROSMAP_gpQTL](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/cis_association/ROSMAP_gpQTL/command_generator.ipynb) lists the input files for the adjusted and unadjusted glycoproteomics cis association, in the `base_params` variable of `generate_command_1`.

## Where to find the results

- **Cis-QTL association testing (TensorQTL output).** `s3://statfungen/ftp_fgc_xqtl/analysis_result/cis_association/ROSMAP/pQTL/gpQTL/`
- **Cis top loci.** [glycoQTL folder, syn69865744](https://www.synapse.org/Synapse:syn69865744)
- **Trans top loci.** [glycoQTL folder, syn70094703](https://www.synapse.org/Synapse:syn70094703)
- **Fine-mapping models.** [ROSMAP_glycoQTL, syn76495192](https://www.synapse.org/Synapse:syn76495192)
- **TWAS weight models.** [ROSMAP_glycoQTL, syn77828034](https://www.synapse.org/Synapse:syn77828034)
- **Multi-context colocalization models (ColocBoost).** [ROSMAP_glycoQTL, syn76489398](https://www.synapse.org/Synapse:syn76489398)
- **AD GWAS and xQTL colocalization models.** [ROSMAP_glycoQTL, syn76490205](https://www.synapse.org/Synapse:syn76490205)
- **sLDSC LD scores.** [gpQTL, syn75180848](https://www.synapse.org/Synapse:syn75180848)
