
import sys
import json
import os
import pandas as pd

sys.path.insert(0, 'src')
from data import get_data modify_data
from analysis import no_streaming_viz streaming_viz pktdir_vs_pktsze_int pktdir_vs_pktsze_vid
from utils import convert_notebook
from features import features_labels input_feature_label binarymean_packetsizes binarymin_packetsizes
from all  import ml_model_analysis
from all import ml_model_train

def main(targets):
    '''
    Given the targets, main runs the main project pipeline logic.
    '''
    
    #grabs the parameters from the data config file
    feature_cfg = json.load(open('config/data-params.json'))
    
    
    if 'test' in targets:
        file_names, file_labels, new_df = features_labels(feature_cfg['input_path'])
        new_df.to_csv(feature_cfg['test_out_path'])
        print("The associated test file names are: ") 
        print(file_names)
        print("The associated test file labels are: ") 
        print(file_labels)
        print("Created the new test features! Check folder test/output/ and observe the output features csv file!")

    if 'result' in targets:
        data_names, data_labels, data_df = features_labels(feature_cfg['train_path'])
        input_names, input_labels, input_df = input_feature_label(feature_cfg['input_path'])
        final_result = ml_model_train(data_df, data_labels, input_df, input_labels)
        print(final_result)

    if 'analysis' in targets:
        data_names, data_labels, data_df = features_labels(feature_cfg['train_path'])
        prediction_labels, test_labels = ml_model_analysis(data_df, data_labels)
        
    return

if __name__=='__main__':
    #run via:
    targets = sys.argv[1:]
    main(targets)
