SHELL := /bin/bash

all:
	python scripts/toc.py content/xqtl-data/{gwas,omics,qtl,study_info,reference_data}/*.md -o content/xqtl-data/README.md -t "FunGen-xQTL Data Catalog" -b "https://github.com/StatFunGen/xqtl-resources/tree/main/content/xqtl-data/" -c "Lead analysts: "
	python scripts/hugo_generator.py