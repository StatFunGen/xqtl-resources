5 Metadata files used to generate [this table](https://github.com/StatFunGen/xqtl-resources/blob/main/data/genes/unified_AD_loci_xQTL_summary.xlsx):

- `metadata_analysis.csv` containing all exported tables paths
- `contexts_metadata.csv` containing contexts (datasets) label mapping between the different analysis/exported tables
- `columns_metadata.tsv` containing all columns to keep for the excel sheets, with associated metadata (column width, coloring..)
- `excel_metadata.tsv` containing some meta information for the excel sheet construction
- `pattern_coloring.tsv` containing all patterns to color in the excel sheet

1 metadata optional:

- `long_table_columns_selection.csv` to generate a long table with selected columns from the table res_allanalysis_ADloci_overlap.csv.gz generated in step III  (in this table, each row is a variant-ADlocus-Method-context-gene_name information, and so facilitate querying informations, see also [this file](https://github.com/StatFunGen/xqtl-paper/blob/main/main_text/6_AD_xQTL_genes/staging/gene_priorization_table/complete_ADlocus_level_summary.R)) 
