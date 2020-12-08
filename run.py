
import sys
import json
import os
import pandas as pd

sys.path.insert(0, 'src')
from data import create_temp_directory, modify_data
from analysis import no_streaming_viz, streaming_viz, pktdir_vs_pktsze_int, pktdir_vs_pktsze_vid
#from utils import convert_notebook
from features import features_labels, input_feature_label, binarymean_packetsizes, binarymin_packetsizes
from MLmodel import ml_model_analysis, ml_model_train, classifier

def main(targets):
    '''
    Given the targets, main runs the main project pipeline logic.
    '''
    
    #grabs the parameters from the data config file
    data_cfg = json.load(open('config/data-params.json'))
    feature_cfg = json.load(open('config/features-params.json'))
    model_cfg = json.load(open('config/model-params.json'))
    
    #creates the local temp directory for intermediate steps to be placed
    create_temp_directory()
    
    if 'test' in targets:
        new_df = features_labels(data_cfg['test_path'], data_cfg['test_out_path'])
        print("The associated test file names are: ") 
        print(new_df['data_file_name'])
        print("The associated test file labels are: ") 
        print(new_df['labels'])
        print("Created the new test features! Check folder test/output/ and observe the output features csv file!")
    
    if 'features' in targets:
        train_df = features_labels(data_cfg['train_path'], feature_cfg['feature_path'])
        input_feature_df = input_feature_label(data_cfg['input_path'], feature_cfg['input_feature_path'])

    if 'train' in targets:
        ml_model_train(feature_cfg['feature_path'], model_cfg['trained_model'])
    
    if 'result' in targets:
        input_df = pd.read_csv(feature_cfg['input_feature_path'])
        classifier(input_df, model_cfg['trained_model'])
        

    if 'analysis' in targets:
        data_df = features_labels(data_cfg['train_path'], feature_cfg['feature_path'])
        prediction_labels, test_labels = ml_model_analysis(data_df[['Dir1_ByteCount_0to300_feature','Dir2_ByteCount_1200to1500_feature',
                                                                    'max_prominence_feature']], data_df['labels'])
        
    return

if __name__=='__main__':
    #run via:
    targets = sys.argv[1:]
    main(targets)
