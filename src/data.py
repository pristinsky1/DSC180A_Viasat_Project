import pandas as pd
import os


def get_data(indir, outdir):
    '''
    Reads the data by creating a symlink between the 
    location of the downloaded data and /data
    '''
    # first create the data directory
    directory = "data"
    parent_dir = "./"
    path = os.path.join(parent_dir, directory)

    os.mkdir(path)

    # create a convenient hierarchical structure of folders inside /data
    directory1 = "raw"
    directory2 = "temp"
    directory3 = "out"
    parent_dir = "./data/"
    
    os.mkdir(os.path.join(parent_dir, directory1))
    os.mkdir(os.path.join(parent_dir, directory2))
    os.mkdir(os.path.join(parent_dir, directory3))
    
    # create the symlink
    os.symlink(indir, outdir) 
        
    return pd.read_csv(outdir)





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
