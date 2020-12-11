
import sys
import json
import os
import pandas as pd

sys.path.insert(0, 'src')
from data import create_temp_directory
from analysis import no_streaming_viz, streaming_viz, pktdir_vs_pktsze_int, pktdir_vs_pktsze_vid
#from utils import convert_notebook
from features import features_labels, input_feature_label
from ml_model import ml_model_analysis, ml_model_train
from ml_model import final_classifier

def main(targets):
    '''
    Given the targets, main runs the main project pipeline logic.
    '''
    
    #grabs the parameters from the data config file
    data_cfg = json.load(open('config/data-params.json'))
    feature_cfg = json.load(open('config/features-params.json'))
    model_cfg = json.load(open('config/model-params.json'))
    
    
    if 'test' in targets:
        #creates the local temp directory for intermediate steps to be placed
        create_temp_directory()
        features_labels(data_cfg['test_path'], data_cfg['test_out_path'])
        print("The associated test file names are: ") 
        print(new_df['data_file_name'])
        print("The associated test file labels are: ") 
        print(new_df['labels'])
        print("Created the new test features! Check folder test/output/ and observe the output features csv file!")
        
        train_df = features_labels(data_cfg['train_path'], feature_cfg['feature_path'])
        input_feature_df = input_feature_label(data_cfg['input_path'], feature_cfg['input_feature_path'])
        ml_model_train(feature_cfg['feature_path'], model_cfg['trained_model'])
        data_df = features_labels(data_cfg['train_path'], feature_cfg['feature_path'])
        prediction_labels, test_labels = ml_model_analysis(data_df, data_df['labels'])
        input_df = pd.read_csv(feature_cfg['input_feature_path'])
        final_classifier(input_df, model_cfg['trained_model'], output_file_path)
    
    if 'features' in targets:
        #creates the local temp directory for intermediate steps to be placed
        create_temp_directory()
        
        train_df = features_labels(data_cfg['train_path'], feature_cfg['feature_path'])
        input_feature_df = input_feature_label(data_cfg['input_path'], feature_cfg['input_feature_path'])

    if 'train' in targets:
        ml_model_train(feature_cfg['feature_path'], model_cfg['trained_model'])
    
    if 'result' in targets:
        input_df = pd.read_csv(feature_cfg['input_feature_path'])
        final_classifier(input_df, model_cfg['trained_model'], output_file_path)
        

    if 'analysis' in targets:
        data_df = features_labels(data_cfg['train_path'], feature_cfg['feature_path'])
        prediction_labels, test_labels = ml_model_analysis(data_df, data_df['labels'])
    
    if 'all' in targets:
        #creates the local temp directory for intermediate steps to be placed
        create_temp_directory()
        
        train_df = features_labels(data_cfg['train_path'], feature_cfg['feature_path'])
        input_feature_df = input_feature_label(data_cfg['input_path'], feature_cfg['input_feature_path'])
        ml_model_train(feature_cfg['feature_path'], model_cfg['trained_model'])
        data_df = features_labels(data_cfg['train_path'], feature_cfg['feature_path'])
        prediction_labels, test_labels = ml_model_analysis(data_df, data_df['labels'])
        input_df = pd.read_csv(feature_cfg['input_feature_path'])
        final_classifier(input_df, model_cfg['trained_model'], output_file_path)
    return

if __name__=='__main__':
    #run via:
    targets = sys.argv[1:]
    main(targets)
