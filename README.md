# Viasat VPN Streaming/No Streaming Classifier 
### Fall 2020 DSC180A - B05 

### Arely Vasquez and Andrey Pristinsky

Our analysis and code is shown under the notebooks folder. They consist of data regarding VPN and its variables in order to perform EDA. It shows graphs regarding different variables and visual representations. 

The code consists of importing pandas, matplotlib as well as using the datasets to display the graphs of the bytes being sent between the source computer and the destination. To run this code, all that is needed is to access the notebooks folder and then run the jupyter notebooks that will display the graphs.


Arely Vasquez developed the EDA(Week 3).ipynb jupyter notebook.
Andrey Pristinsky developed the EDA_Week3_Part2.ipynb jupyter notebook.
Both team members were involved in constructing the format of this repository. 



## Allowing Reproduction Instructions

Note: These instructions assume that the user has access to the DSMLP server to be able to run this project.
Open terminal, run these commands in the associated order: 

1.) *ssh user@dsmlp-login.ucsd.edu* (user refers to your school username). Enter credentials.

2.) *launch-180.sh -G  B05_VPN_XRAY -i apristin99/dsc180domain_ml*

3.) Delete file under input_data folder and add your own. Otherwise, leave as is and use the provided input_dataset.

4.) *python run.py result* --> This will run the classifier and have it predict what the input_data file is.

To test out how the features are built on test data, run *python run.py test*

To see the accuracy of how the classifier is performing, run *python run.py analysis*

These instructions are provided to run the entire repository. To see my analysis, look within the notebooks folder and click on analysis.ipynb.
