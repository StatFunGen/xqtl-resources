# FGMB Atlas: Multi-context RWAS Prediction Models

## About FGMB Atlas

FunGen-xQTL Multi-Brain (FGMB) Atlas is a multi-context regulome-wide association study (RWAS) resource for studying genetic regulation in aging-brain-related disease traits. It provides molecular expression prediction models across brain regions, cell types, cohorts, and molecular modalities, capturing both shared and context-specific regulatory effects.  

The released prediction model database and analysis outputs are available through Synapse. Supporting documentation is available through the FGMB Atlas manuscript resource site, the FunGen `xQTL Analysis Protocol`, and the `pecotmr` software vignettes.

## Available Resources

### FGMB Atlas
The **`FGMB Atlas`** [resource site](https://morgantelab.github.io/FGMB-atlas-paper/) organizes the atlas overview, modeling strategy, workflow examples, figure notebooks, and resource table for the Synapse accessions listed below.

- **[FGMB Atlas Overview](https://morgantelab.github.io/FGMB-atlas-paper/overview/index.html)** - Overview of the FGMB Atlas resource, study design, and major analysis components.
- **[FGMB Atlas Modeling Strategy](https://morgantelab.github.io/FGMB-atlas-paper/modeling_strategy/index.html)** - Modeling design and strategy for the FGMB Atlas RWAS prediction resources.
- **[FGMB Atlas Workflow Examples](https://morgantelab.github.io/FGMB-atlas-paper/workflow_example/index.html)** - Example workflows for building expression predictors, running RWAS association analyses, and multi-group causal TWAS fine-mapping.


### pecotmr
**`pecotmr`** [software](https://github.com/StatFunGen/pecotmr) vignettes for implementation details for weight construction and TWAS Z-score inference:

- **[Learning TWAS Weights from Individual-Level Data and Summary Statistics](https://statfungen.github.io/pecotmr/articles/twas-weights.html)** - Build per-variant prediction weights from individual-level genotype and molecular phenotype data, QTL summary statistics, or multi-context molecular data.
- **[Inferring TWAS Z-Scores from GWAS Summary Statistics](https://statfungen.github.io/pecotmr/articles/twas-zscore.html)** - Apply learned weights to GWAS summary statistics to compute per-gene TWAS/RWAS Z-scores, including harmonization, LD sketch use, and optional missing-variant imputation.

### xQTL Analysis Protocol
**`xQTL Analysis Protocol`** analysis pipeline protocol documentation for model training, association-testing, and fine-mapping
TWAS/RWAS-style weights is also available:

- **[Univariate Fine-Mapping and TWAS with SuSiE](https://statfungen.github.io/xqtl-protocol/code/mnm_analysis/univariate_fine_mapping_twas_vignette.html)** - Protocol workflow for univariate fine-mapping and TWAS weight generation.
- **[Multivariate Fine-Mapping for multiple genes](https://statfungen.github.io/xqtl-protocol/code/mnm_analysis/multivariate_multigene_fine_mapping_vignette.html)** - Protocol workflow for multivariate, multi-gene fine-mapping and TWAS weights.
- **[TWAS, cTWAS and MR](https://statfungen.github.io/xqtl-protocol/code/pecotmr_integration/twas_ctwas.html)** - Protocol workflow for TWAS analysis and cTWAS fine-mapping.


## Data Access

All released FGMB Atlas RWAS model resources are available through
Synapse:

| Resource | Synapse accession | Notes |
| --- | --- | --- |
| RWAS prediction models | [`syn69670600`](https://www.synapse.org/Synapse:syn69670600) | FGMB Atlas prediction model resource for RWAS analyses. |
| Alzheimer disease RWAS association results | [`syn74908416`](https://www.synapse.org/Synapse:syn74908416) | Association results from applying the FGMB Atlas RWAS models to Alzheimer disease. |
| Single-context and multi-context joint variant-gene fine-mapping results | [`syn74908389`](https://www.synapse.org/Synapse:syn74908389) | Fine-mapping outputs for single-context and multi-context analyses. |
| LD reference panel for RWAS association testing and fine-mapping | [`syn75082260`](https://www.synapse.org/Synapse:syn75082260) | LD reference panel built from whole-genome sequencing data from European-ancestry participants in ADSP Release 4. |

## Citation

If you use these models or derived results, please cite the FGMB Atlas manuscript and the relevant Synapse accessions. 
> Liu C, Wang A, Sun H, Luo K, Qian S, Li Y, He X, De Jager PL, Bennett DA, Wang M, Cruchaga C, The Alzheimer’s Disease Functional Genomics Consortium, Wang G, Morgante F. (2026). A multi-context regulome-wide association atlas for genetic studies of aging brain disorders. medRxiv. https://doi.org/10.64898/2026.05.15.26353329
```
@misc{liu_multi-context_2026,
	title = {A {Multi}-{Context} {Regulome}-{Wide} {Association} {Atlas} for {Genetic} {Studies} of {Aging} {Brain} {Disorders}},
	url = {https://www.medrxiv.org/content/10.64898/2026.05.15.26353329v1},
	doi = {10.64898/2026.05.15.26353329},
	urldate = {2026-05-25},
	publisher = {medRxiv},
	author = {Liu, Chunming and Wang, Anqi and Sun, Hao and Luo, Kaixuan and Qian, Sheng and Li, Yining and He, Xin and Jager, Philip De and Bennett, David and Wang, Minghui and Cruchaga, Carlos and Consortium, The Alzheimer’s Disease Functional Genomics and Wang, Gao and Morgante, Fabio},
	month = may,
	year = {2026}
}
```

For workflow-specific methods, please cite the relevant [`FunGen-xQTL protocol`](https://github.com/StatFunGen/xqtl-protocol) documentation and [`pecotmr`](https://github.com/StatFunGen/pecotmr) software documentation.
