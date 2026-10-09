# ROSMAP Covariates data

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) covariates data

## Data Descriptions
There are couple of versions of covariates files been used for QTL calling, which may lead to inconsistency of data production and downstream integration analysis. 

The following are the files that haven been used:

This should be the complete covariates file, which have 3000+ samples and more covariates, other than sex, death and pmi, than we need for our QTL calling. To accomendate our QTL pipeline, formatting and processing is needed before using. 


This should be the file that have been processed for sQTL calling, which has 853 samples and only have covariates we needed(sex, pmi, death). This file was accomendated to our pipeline. 


This is the one that Hao updated on May, which has 1161 samples. This file has complete covariates information for all samples that in genotype. And this is already formatted to accomendate our pipeline. S0, using this as covariates file is suggested for all QTL calling. 