# ROSMAP WGS data

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) whole-genome sequence data

## Contact

Hao Sun and Xuanhe Chen

## Data Descriptions

This data is part of WGS done for three AMP-AD supported studies: The ROSMAP study (the data provided here), the MayoRNAseq study, and the MSBB study. Provided are VCF files, consisting of all samples from that study divided by chromosome, for the following analysis.

Information about overlaps of ROSMAP samples and other database can be find [here](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/genotype/WGS_sample_id_map.ipynb)

Information of the preprocessing: https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/genotype/genotype_preprocessing.ipynb 

- Data Location on CU cluster:

The original VCF files of joint-call ROS/MAP WGS is here (N =  1162/4669 of them are ROS/MAP; GRCh38):


The intermediate VCF files for QCing the vcf can be found here:


After processing through our pipeline, the processed plink file is here (N =  1160, MAC = 0, HWE = 1E-8, sample/variants missingness filter = 0.1 ; GRCh38)



The LD matrixes calculated based on **old version of this genotype** () are here




- Data Location on MSSM cluster:
The ROSMAP monocyte WGS data was downloaded in VCF format, with one file per chromosome (plus X, Y, MT). (Path on MSSM to be added)
