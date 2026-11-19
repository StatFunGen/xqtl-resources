---
type: qtl
modality: glycoQTL
short_title: ROSMAP DLPFC
cohort: ROSMAP
context: DLPFC
sample_size: 316
status: staged
access: controlled
synapse_ids: [syn69865744, syn70094703, syn76495192, syn77828034, syn76489398, syn76490205, syn75180848]
lead_analysts: [FunGen-xQTL Analysis Working Group]
last_verified:
methods:
  cis-QTL: done
  SuSiE: done
  ColocBoost: done
  TWAS: done
---

# ROSMAP DLPFC glycoproteomics QTL

This page documents the glycoproteomics QTL (glycoQTL) analysis of dorsolateral prefrontal cortex (DLPFC) tissue from the Religious Orders Study (ROS) and the Rush Memory and Aging Project (MAP). The [ROSMAP study page](../../study_info/ROSMAP.md) gives an overview of the cohort.

## Study overview

- **Study name.** ROSMAP glycoproteomics QTL.
- **Description.** Summary statistics from the FGC xQTL pipeline for the ROSMAP glycoproteomics QTL analysis.
- **Samples and features.** 316 participants with matched whole-genome sequencing and glycoproteomics data, and 9,044 glycopeptiforms (unique peptide and glycan combinations) covering N-glycosylation and glycation.
- **Covariates.** Sex, age at death, study (ROS or MAP), 15 genotype principal components, hidden factors (PCA, number chosen with the Marchenko-Pastur limit), β-amyloid load and PHF-tau tangle density.
- **Main result.** SuSiE fine-mapping found cis-glycoQTL for 206 glycopeptiforms (MAF ≥ 5%). Adjusting each glycopeptiform for the abundance of its protein removed 52.9% of them, and 43.0% of glycoQTL colocalize with pQTL. The results folders hold both the unadjusted and the protein-adjusted analyses.
- **Source.** Feng, Wang, Cao et al., *Genetic architecture of the human brain glycoproteome implicates TMEM106B and ACE glycosylation in Alzheimer's disease pathogenesis* (manuscript); see [Companion papers](../../../companion_papers).
- **Sample phenotypes.** Sex, age, race and other sample information are in the ROSMAP metadata, described under "Other information" on the [ROSMAP study page](../../study_info/ROSMAP.md).

## Analysis notebooks

### Association scan with TensorQTL and summary statistics standardization

- [TensorQTL.ipynb](https://github.com/StatFunGen/xqtl-protocol/blob/main/code/SoS/association_scan/TensorQTL/TensorQTL.ipynb) generates the TensorQTL cis association results for all QTL types.
- [ROSMAP_gpQTL](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/cis_association/ROSMAP_gpQTL/command_generator.ipynb) lists the input files for the adjusted and unadjusted glycoproteomics cis association, in the `base_params` variable of `generate_command_1`.

## Where to find the results

- **Cis top loci.** [glycoQTL folder, syn69865744](https://www.synapse.org/Synapse:syn69865744)
- **Trans top loci.** [glycoQTL folder, syn70094703](https://www.synapse.org/Synapse:syn70094703)
- **Fine-mapping models.** [ROSMAP_glycoQTL, syn76495192](https://www.synapse.org/Synapse:syn76495192)
- **TWAS weight models.** [ROSMAP_glycoQTL, syn77828034](https://www.synapse.org/Synapse:syn77828034)
- **Multi-context colocalization models (ColocBoost).** [ROSMAP_glycoQTL, syn76489398](https://www.synapse.org/Synapse:syn76489398)
- **AD GWAS and xQTL colocalization models.** [ROSMAP_glycoQTL, syn76490205](https://www.synapse.org/Synapse:syn76490205)
- **sLDSC LD scores.** [glycoQTL, syn75180848](https://www.synapse.org/Synapse:syn75180848)
