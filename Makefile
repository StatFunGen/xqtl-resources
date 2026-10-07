SHELL := /bin/bash

all:
	python scripts/toc.py $$(find content/xqtl-data/gwas content/xqtl-data/omics content/xqtl-data/qtl content/xqtl-data/study_info content/xqtl-data/reference_data -name '*.md' ! -name README.md | sort) -o content/xqtl-data/README.md -t "FunGen-xQTL Data Catalog" -b "https://github.com/StatFunGen/xqtl-resources/tree/main/" -c "Lead analysts: " --subfolder-readme
	python scripts/hugo_generator.py --serve