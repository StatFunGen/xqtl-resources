---
type: study
short_title: MetaBrain
cohort: MetaBrain
context: 5 brain regions
status: staged
synapse_ids: [syn69670592, syn69670600, syn69670597, syn69865816]
lead_analysts: []
last_verified:
---

# MetaBrain study info

MetaBrain is a published meta-analysis of brain gene expression QTL (eQTL), built from bulk RNA-seq from many independent brain studies. FunGen-xQTL did not collect these samples: it uses MetaBrain's eQTL summary statistics as an external brain resource, alongside its own cohorts (ROSMAP, MSBB, Knight-ADRC, STARNET and MiGA).

- Study name : MetaBrain
- Brain regions : cortex, hippocampus, basal ganglia, cerebellum and spinal cord
- Data type : bulk brain eQTL summary statistics (no individual-level data)
- Publication : de Klein, N. et al. Brain expression quantitative trait locus and network analyses reveal downstream effects and putative drivers for brain-related diseases. *Nature Genetics* 55, 377–388 (2023)
- Data contributors : Lude Franke, Ellen A. Tsai and Harm-Jan Westra
- Summary statistics : available from the [MetaBrain resource](https://www.metabrain.nl/)

## How FunGen-xQTL uses MetaBrain

- **Gene evidence at AD loci.** The flagship paper fine-mapped the MetaBrain eQTL summary statistics with SuSiE-rRSS, which accounts for differences between the study's LD and the reference LD, using the [ADSP LD sketch](../reference_data/ld_sketch.md) as the LD reference. The results add evidence for which gene an AD locus acts through.
- **Replication.** The FunGen-xQTL Atlas paper compared its significant eQTL with MetaBrain (per-gene FDR < 0.05) and GTEx to measure how often its findings replicate.

## QTL Analyses

| Dataset | Modality | QTL File |
|---------|----------|----------|
| Bulk brain eQTL, 5 regions | eQTL | [MetaBrain_brain_expression_qtl](../qtl/eQTL/MetaBrain_brain_expression_qtl.md) |

The flagship paper's fine-mapping ([syn69670592](https://www.synapse.org/Synapse:syn69670592)), TWAS models ([syn69670600](https://www.synapse.org/Synapse:syn69670600)) and colocalization results ([syn69670597](https://www.synapse.org/Synapse:syn69670597), [syn69865816](https://www.synapse.org/Synapse:syn69865816)) include the MetaBrain contexts.
