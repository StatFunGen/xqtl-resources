# How to get the data

The data are hosted on Synapse and NIAGADS. Each dataset page gives a Synapse ID or public URL, and its access label states what is needed before download.

{{< access-defs >}}

## Synapse and the AD Knowledge Portal

Omics data, QTL results, xQTL models and reference files are on Synapse. Most cohort data are controlled.

{{% steps %}}
1. **Create a Synapse account.** Register at [synapse.org](https://www.synapse.org/) and verify your profile.
2. **Become a certified user.** Pass the short Synapse certification quiz on data governance.
3. **Request access.** For controlled data, submit the data use certificate for the cohort through the [AD Knowledge Portal](https://adknowledgeportal.synapse.org/).
4. **Download.** Use the web interface, the Synapse command-line client, or the Python or R client with the Synapse ID from the dataset page.
{{% /steps %}}

```python
import synapseclient
syn = synapseclient.login()
entity = syn.get("syn69670632", downloadLocation=".")
```

The four top-level FunGen-xQTL folders on Synapse are [variant and gene summaries (syn69865684)](https://www.synapse.org/Synapse:syn69865684), [xQTL models (syn69670588)](https://www.synapse.org/Synapse:syn69670588), [raw QTL data (syn69670632)](https://www.synapse.org/Synapse:syn69670632) and [reference files (syn69670634)](https://www.synapse.org/Synapse:syn69670634).

## NIAGADS

AD GWAS summary statistics and ADSP genomics are distributed by NIAGADS. Summary statistics marked Open can be downloaded from the dataset's public URL. Harmonized xQTL summary statistics and fine-mapping results are open access on NIAGADS DSS as [NG00184.v1](https://dss.niagads.org/datasets/ng00184/) (GRCh38). No application is needed. Individual-level data stay controlled and are requested through DSS under their own accessions.

{{% callout %}}
**NG00184 downloads are packaged archives, one per QTL type and result type, named** `ADSP_FunGen_xQTL.v1.<QTL type>.<result type>.tar`

| Result type | What it holds |
|---|---|
| `hmt_significant` | High-confidence associations (recommended starting point) |
| `bh_significant` | Associations passing the FDR threshold |
| `all` | Every tested association |
| `single_context_finemapping_cs95` | Variants in 95% credible sets |
| `single_context_finemapping_all` | Full fine-mapping output |

NG00184 includes eQTL, snuc-eQTL, sQTL, pQTL, mQTL and haQTL. Each archive holds `.bed.gz` files with tabix indexes, metadata and a manifest.
{{% /callout %}}

The [xQTL Atlas](https://xqtl.niagads.org/) lets you search significant associations by variant, gene or region, view them in a genome browser and download matching rows as TSV.

## Release status

{{< status-defs >}}
