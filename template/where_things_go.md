# What goes where: paper, website, Synapse

Draft for review. This page sets what each of the three places should hold so that the catalog is informative for the lab and the public while keeping private details out.

- **Paper**: the scientific claims and aggregate numbers (for example the number of datasets, modalities and participants), plus a Data Availability statement that points to Synapse and NIAGADS.
- **Website** (this repository): the catalog of datasets for readers. It describes what each dataset is and how to get it. It does not describe where files sit on lab machines.
- **Synapse**: the data itself, with its folder structure, file names and access terms. This is the single source for file locations.

| Item | Paper | Website | Synapse |
|------|-------|---------|---------|
| Dataset counts, participant totals, modality list | yes | yes (aggregate only) | no |
| Dataset description, cohort, tissue, modality | summary | yes | in file annotations |
| Sample size per dataset | where needed for results | yes (aggregate only) | in file annotations |
| Methods and pipeline version | yes | link to the public notebook or protocol | no |
| Grant, publication, acknowledgement | yes | yes (study pages) | in study annotations |
| Data location | accession and Data Availability only | Synapse ID or public URL | yes (folder and file names) |
| Access conditions | statement | one line (open, controlled, requested) | yes (access terms) |
| Lead analysts | authors | name only | contributor |
| Cluster, HPC and FTP file-system paths | no | no | no |
| Personal emails and phone numbers | no | no | no |
| Participant-level data, counts under 10 | no | no | controlled access only |
| Internal staging IDs and working notes | no | `internal` front matter field only, no paths | staging project only |

## Rules for page authors

1. Point to data with a Synapse ID or a public URL. Never with a file-system path.
2. Report aggregate counts only.
3. Give names, not contact details, for people.
4. Keep a field empty rather than writing a guess. Mark unknown values as TBD and name who can fill them.
5. When a page and the paper disagree on a number, the paper is the reference until it is revised.

## Open points for the lab

- Whether the `internal` front matter field should stay in the public repository.
- Whether study pages should keep PI names and grant numbers, as the NIAGADS submission fields require.
