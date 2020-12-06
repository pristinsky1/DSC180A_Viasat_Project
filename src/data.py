import pandas as pd
import os


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

    # create a convenient hierarchical structure of folders inside /data
    directory1 = "features"
    directory2 = "model"
    directory3 = "classifier_output"
    parent_dir = "./data/"
    
    os.mkdir(os.path.join(parent_dir, directory1))
    os.mkdir(os.path.join(parent_dir, directory2))
    os.mkdir(os.path.join(parent_dir, directory3))
        
    return





def modify_data(raw_data):
    #we are separating the column "packet sizes"
    new_pksize = []
    for i in raw_data["packet_sizes"]:
        arr = i.split(";")
        for j in arr[:-1]:
            new_pksize.append(j)

    #we are separating the column "packet dir"
    new_pkdir = []
    for i in raw_data["packet_dirs"]:
        arr = i.split(";")
        for j in arr[:-1]:
            new_pkdir.append(j)

    modified_data = pd.DataFrame({'packet_sizes': pd.to_numeric(new_pksize), 'packet_dir': pd.to_numeric(new_pkdir)})
    return modified_data
