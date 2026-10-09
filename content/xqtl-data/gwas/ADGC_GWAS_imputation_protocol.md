---
type: gwas
short_title: ADGC imputation protocol
status:
access:
release:
synapse_ids: []
lead_analysts: [Xuanhe Chen]
last_verified:
---

# ADGC GWAS imputation protocol

This protocol is adapted from the [ADGC GWAS Data QC Protocol](https://bitbucket.org/wanpinglee_penn/gwas_qc/src/master/). It generates imputed genotype data for xQTL analysis in some cohorts.

## Contact

Xuanhe Chen

## Imputation by [TOPMed imputation server](https://imputation.biodatacatalyst.nhlbi.nih.gov/#!)
The TOPMed imputation server returns results on **hg38**.

1. [Register an account](https://imputation.biodatacatalyst.nhlbi.nih.gov/index.html#!pages/register)
2. [Log in](https://imputation.biodatacatalyst.nhlbi.nih.gov/index.html#!pages/login)
3. Click "Run" and "Genotype Imputation (Minimac4)"
4. Fill out the form

	4.1. Name: Assign a job name
	
	4.2. Reference panel: TOPMed r2
	
	4.3. Input Files: File Upload
	
	4.4. Array Build: GRCh37/hg19
	
	4.5. Rsq Filter: Off
	
	4.6. Phasing:  Eagle v2.4 (unphased input)
	
	4.7. QC Frequency Check: keep -- select an option --
	
	4.8. Mode: Quality Control & Imputation
	
	4.9. Check "I will not attempt to re-identify or contact research participants."
	
	4.10. Check "I will report any inadvertent data release, security breach or other data management incident of which I become aware."
	
	4.11. Click "Submit Job"
