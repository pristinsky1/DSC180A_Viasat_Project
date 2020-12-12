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

3.) **git clone https://github.com/pristinsky1/DSC180A_Viasat_Project.git**

4.) **cd DSC180A_Viasat_Project**


Here are a different ways to use our model:

a.) If you would like to classify your own input file using our model:

    i.) Delete file under input_data folder and add your own. Otherwise, leave as is and use the provided input_dataset.
    
    ii.) run **python run.py features**
    
    iii.) run **python run.py train**
    
    iv.) run **python run.py result**
    
    v.) run **python run.py analysis**
    
    By runningsteps ii-v, you will see return statements that give you more information and details on the accuracy of the model and its performance.
    Another option woulbd be to skip steps ii-v and simply run run **python run.py all**
    
     To see analysis, look within the notebooks folder and click on analysis.ipynb.
    
b.) To run the model on our test data:

    i.) run **python run.py test**
    
    ii.) A print statement will appear letting you know that the model is locally saved in temp/model/
        The predicted  output of the input file will saved locally in your temp/classifier_output
 
