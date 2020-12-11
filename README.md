# Viasat VPN Streaming/No Streaming Classifier 
### Fall 2020 DSC180A - B05 

#### Arely Vasquez and Andrey Pristinsky

In this repository, we have created a machine learning model in order to classify whether a dataset of network stats collected while using a VPN contains streaming or not streaming.

In order to run this model on your own network_stats dataset, follow the steps below.


## Allowing Reproduction Instructions

Note: These instructions assume that the user has access to the DSMLP server to be able to run this project.
Open terminal, run these commands in the associated order: 

1.) **ssh user@dsmlp-login.ucsd.edu** (user refers to your school username). Enter credentials.

2.) **launch-180.sh -G  B05_VPN_XRAY -i apristin99/dsc180a_viasat_project**

3.) **cd DSC180A_Viasat_Project**

4.) Delete file under input_data folder and add your own. Otherwise, leave as is and use the provided input_dataset.

5.) **python run.py result** --> This will run the classifier and have it predict what the input_data file is.

To test out how the features are built on test data, run **python run.py test**

To see the accuracy of how the classifier is performing, run **python run.py analysis**

These instructions are provided to run the entire repository. To see my analysis, look within the notebooks folder and click on analysis.ipynb.
