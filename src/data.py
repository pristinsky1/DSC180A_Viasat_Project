import pandas as pd
import os
import shutil


def create_temp_directory():
    '''
    Creates the temp directory that will be found on your local machine where the intermediate
    steps will be stored such as the features and the ml model
    '''
    # first create the data directory
    directory = "temp"
    parent_dir = "./"
    path = os.path.join(parent_dir, directory)
    
     #remove temp dir if one already exists
    if (os.path.exists(path) and os.path.isdir(path)):
        shutil.rmtree(path)
    
    os.mkdir(path)

    # create a convenient hierarchical structure of folders inside /temp
    directory1 = "features"
    directory2 = "model"
    directory3 = "classifier_output"
    parent_dir = "./temp/"
    
    os.mkdir(os.path.join(parent_dir, directory1))
    os.mkdir(os.path.join(parent_dir, directory2))
    os.mkdir(os.path.join(parent_dir, directory3))
        
    return
