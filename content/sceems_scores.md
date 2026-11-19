# scEEMS (single-cell Enhanced Expression Modifier Scores)

## What scEEMS is

scEEMS is a machine learning model that predicts which variants are causal eQTLs in six brain cell types: astrocytes, excitatory neurons, inhibitory neurons, microglia, oligodendrocytes and oligodendrocyte precursor cells (OPC). Each prediction is a probability for one variant-gene pair. The model uses 4,840 variant, variant-gene pair and gene features, including deep learning-based variant effect prediction (DL-VEP) scores and the GPN-STAR DNA language model score. The six cell types are those of the [ROSMAP snuc-eQTL](xqtl-data/qtl/eQTL/ROSMAP_snRNAseq_pseudo_bulk_qtl) data.

The predictions can be used as priors for fine-mapping. The release includes SuSiE credible sets for each cell type under a uniform prior, Expression Modifier Score (EMS) re-weighting and three scEEMS priors, so the priors can be compared directly.

This is the revised release. Its predictions come from the Weighted (Full) model, which replaces the earlier release that weighted the DL-VEP features tenfold.

## Where to get the data

All files are in the AD Knowledge Portal folder **xQTL_SCEEM_scores** ([syn77875113](https://www.synapse.org/Synapse:syn77875113)). Access is controlled: you need a Synapse account and approved data access on the AD Knowledge Portal. See [How to get the data](how_to_get_data).

| Folder | What it holds | Synapse ID |
|--------|---------------|------------|
| Predictions | Predicted eQTL probabilities for variant-gene pairs, per cell type and chromosome (tabix-indexed TSV) | [syn77875605](https://www.synapse.org/Synapse:syn77875605) |
| Fine-mapping | SuSiE credible sets per cell type under five priors: uniform, EMS, scEEMS Weighted (Full), scEEMS Unweighted (Full) and scEEMS Weighted (Restricted) | [syn77875116](https://www.synapse.org/Synapse:syn77875116) |
| Model training | Trained models (three per cell type and held-out chromosome), feature list and weights, and the training and test data | [syn77875154](https://www.synapse.org/Synapse:syn77875154) |
| Featurization | Inputs used to build the features, including ChromBPNet models and peaks, ABC scores and cell type annotations | [syn77875114](https://www.synapse.org/Synapse:syn77875114) |

Each folder has a README describing its files and columns.

## Cell types

| Cell type | Prediction folder |
|-----------|-------------------|
| Astrocytes | [Ast_mega_eQTL](https://www.synapse.org/Synapse:syn77875606) |
| Excitatory neurons | [Exc_mega_eQTL](https://www.synapse.org/Synapse:syn77875607) |
| Inhibitory neurons | [Inh_mega_eQTL](https://www.synapse.org/Synapse:syn77875608) |
| Microglia | [Mic_mega_eQTL](https://www.synapse.org/Synapse:syn77875609) |
| Oligodendrocyte precursor cells | [OPC_mega_eQTL](https://www.synapse.org/Synapse:syn77875610) |
| Oligodendrocytes | [Oli_mega_eQTL](https://www.synapse.org/Synapse:syn77875611) |
