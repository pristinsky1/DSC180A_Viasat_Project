import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

#Trains, tests, and splits the data up so that RandomForestClassifier can be used 
#to train on the data and then determine how accurate the model is
def ml_model_analysis(X, y):
    model = RandomForestClassifier()
    X_tr, X_ts, y_tr, y_ts = train_test_split(X, y, test_size=0.25, random_state=42)
    model = model.fit(X_tr[['Dir1_ByteCount_0to300_feature','Dir2_ByteCount_1200to1500_feature','max_prominence_feature']],y_tr)
    prediction_test = model.predict(X_ts[['Dir1_ByteCount_0to300_feature','Dir2_ByteCount_1200to1500_feature','max_prominence_feature']])
    prediction_train = model.predict(X_tr[['Dir1_ByteCount_0to300_feature','Dir2_ByteCount_1200to1500_feature','max_prominence_feature']])
    print (("Base test accuracy", metrics.accuracy_score(y_ts, prediction_test)), 
            ("Base Train Accuracy", metrics.accuracy_score(y_tr, prediction_train)))
    return prediction_test, y_ts

  
#Trains the model on all the data found within the GoodData on dsmlp, and then predicts 
#whether streaming or not for the input data chunk entered
def ml_model_train(feature_csv, filename):
    feature_df = pd.read_csv(feature_csv)
    model = RandomForestClassifier()
    model = model.fit(feature_df[['Dir1_ByteCount_0to300_feature','Dir2_ByteCount_1200to1500_feature','max_prominence_feature']], feature_df['labels'])
    # save the model to temp/model folder
    joblib.dump(model, filename)
    return

def classifer(input_df, filename):
    loaded_model = joblib.load(filename)
    prediction = loaded_model.predict(input_df[['Dir1_ByteCount_0to300_feature','Dir2_ByteCount_1200to1500_feature','max_prominence_feature']])
    for i in range(0, len(prediction)):
        if bool(prediction[i]) == bool(input_df['labels'][i]):
            val = "Yes"
        else:
            val = "No"
        print("Input File Name: " + str(input_df['input_file_name'][i]), 
              "is_streaming? Prediction Value: " + str(bool(prediction[i])), 
              "is_streaming? True Value: " + str(bool(input_df['labels'][i])), 
              "classified correctly? : " + val)
    return
