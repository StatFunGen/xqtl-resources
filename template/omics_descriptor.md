# Dataset name 

Dataset description. Should be one or multiple paragraphs.

(You can also put the link of related study.md here, where the study information `####.md` file for the data source is created based on template `study_descriptor.md` and saved under `study_info` folder. )

## Contact

The lead analysts of the data and also the persons responsible for maintaining this document.

- Contact Name : Name
- Contact Email : Email
- Contact Affiliation : contact affilitation or institution
- Contact Role : contact role, one of principal investigator, submitter, primary contact

## Study Overview

Please include all the **bullet points** below in the exact format as the following. (These bullet points was created according to NIAGADs' submission requirements, that's not a strict format restriction now but we still keep these information for our own reference.)

**NOTE: the "study" here describes the study which the omics data was generated**

- Grant number : NIH sponsoring institution and corresponding grant number(s), e.g., National Institutes of Health [U24 HG009397]
- Publication : (Leave this row blank if not applicable) If the dataset being submitted is published, provide PubMed ID of the article; Preprint DOI can also be provided
- Acknowledgement : (Leave this row blank if not applicable) Acknowledgement/funding section from the publication
- Study name : TEXT (as PI of the study, they can provide a name they want. NIAGADS team can amend that if they overlap with any study names currently have)
- Study Description : TEXT (this is free text written by the PI of the study, or extracted from the study's official website)
- Disease : Disease under study if applicable, for example Alzheimer’s Disease, may be list (// separated)
- Data Citation : (Leave this row blank if not applicable) If submitted dataset was generated from processing published or deposited data (e.g., xQTL from pre-existing RNA-seq), list the data citations (PubMedID, repository and accession number, URL, citation statement and/or acknowledgement) for original data if submitted dataset was generated from processing published or deposited data (e.g., xQTL from pre-existing RNA-seq).  Only include annotations files if data generators require an acknowledgement statement (e.g., ADSP annotations).  If multiple datasources (e.g., ROS/MAP RNA-seq, WGS) are used, provide a single entry for the dataset, containing all citations.
- Additional study information : (Leave this row blank if not applicable)


## Dataset Details

### Raw data

URL to original data, if applicable:

- https://dss.niagads.org/datasets/...

Access:

- Synapse: synapse ID(s) of the data.
- Public source: URL of the original release, if any.
- Do not list cluster, HPC, or local file-system paths.



Report the number of files and total size only.

### Molecular phenotype matrices

Access:

- Synapse: synapse ID(s) of the data.
- Public source: URL of the original release, if any.
- Do not list cluster, HPC, or local file-system paths.


A description of these matrices:

1. What are the columns and what are the rows (eg, columns are sample names, rows are CpG sites)
2. Column and Row counts for a data matrix

### Other key data files (if applicable)

Access:

- Synapse: synapse ID(s) of the data.
- Public source: URL of the original release, if any.
- Do not list cluster, HPC, or local file-system paths.



Report the number of files and total size only.

Although it is not necessary to include all the intermediate files in various stages of phenotype quantification and QC, it is important to include summary of all the "key" data files. Currently we have not decided what are the required list of intermediate files because it differs between different omics data. For the time being we rely on the analysts' discretion to provide the information.  

## Links to omics data analysis notebooks

Please list links to the analysis in the order you performed them:

1. Exploratory data anlaysis (EDA): https://github.com/cumc/brain-xqtl-analysis/blob/main/analysis/Marcora_MSSM/MiGA/data-information.ipynb
2. Molecular phenotype quantification: ...

Alternatively you can also use a somewhat free style as long as it is clear from your write-up where the notebooks are on github and what they are. Check out this section for an example of alternative style: https://github.com/cumc/fungen-xqtl-analysis/blob/main/data/descriptor/omics/ROSMAP_DLPFC_ChIPSeq_H3K9ac.md#links-to-omics-data-analysis-notebooks
