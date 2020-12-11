
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
        train_df = features_labels(data_cfg['test_path'], feature_cfg['feature_path'])
        input_feature_df = input_feature_label(data_cfg['test_input_path'], feature_cfg['input_feature_path'])
        print("Created the new test features! Check folder temp/features/ and observe the output features csv file!")
        ml_model_train(feature_cfg['feature_path'], model_cfg['trained_model'])
        print("Trained the test data on the model! The model is locally saved in temp/model/")
        #prediction_labels, test_labels = ml_model_analysis(train_df, train_df['labels'])
        input_df = pd.read_csv(feature_cfg['input_feature_path'])
        final_classifier(input_df, model_cfg['trained_model'], model_cfg['output_file_path'])
        print("Predicted the output of the input file! This is saved locally in your temp/classifier_output")
    
    if 'features' in targets:
        #creates the local temp directory for intermediate steps to be placed
        create_temp_directory()
        
        train_df = features_labels(data_cfg['train_path'], feature_cfg['feature_path'])
        input_feature_df = input_feature_label(data_cfg['input_path'], feature_cfg['input_feature_path'])

    if 'train' in targets:
        ml_model_train(feature_cfg['feature_path'], model_cfg['trained_model'])
    
    if 'result' in targets:
        input_df = pd.read_csv(feature_cfg['input_feature_path'])
        final_classifier(input_df, model_cfg['trained_model'], model_cfg['output_file_path'])
        

    if 'analysis' in targets:
        data_df = features_labels(data_cfg['train_path'], feature_cfg['feature_path'])
        prediction_labels, test_labels = ml_model_analysis(data_df, data_df['labels'])
    
    if 'all' in targets:
        #creates the local temp directory for intermediate steps to be placed
        create_temp_directory()
        train_df = features_labels(data_cfg['train_path'], feature_cfg['feature_path'])
        input_feature_df = input_feature_label(data_cfg['input_path'], feature_cfg['input_feature_path'])
        print("Created the new features! Check folder temp/features/ and observe the output features csv file!")
        ml_model_train(feature_cfg['feature_path'], model_cfg['trained_model'])
        print("Trained the data on the model! The model is locally saved in temp/model/")
        #prediction_labels, test_labels = ml_model_analysis(data_df, data_df['labels'])
        input_df = pd.read_csv(feature_cfg['input_feature_path'])
        final_classifier(input_df, model_cfg['trained_model'], model_cfg['output_file_path'])
        print("Predicted the output of the input file! This is saved locally in your temp/classifier_output")
    return

if __name__=='__main__':
    #run via:
    targets = sys.argv[1:]
    main(targets)
