import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

#Trains, tests, and splits the data up so that RandomForestClassifier can be used 
#to train on the data and then determine how accurate the model is
def ml_model_analysis(X, y):
    model = RandomForestClassifier(criterion = 'entropy', max_depth= None, min_samples_split= 3, n_estimators= 20, random_state=42)
    X_tr, X_ts, y_tr, y_ts = train_test_split(X, y, test_size=0.25, random_state=42)
    model = model.fit(X_tr.drop(columns = ["input_file_name", "labels"]),y_tr)
    prediction_test = model.predict(X_ts.drop(columns = ["input_file_name", "labels"]))
    prediction_train = model.predict(X_tr.drop(columns = ["input_file_name", "labels"]))
    print (("Base test accuracy", metrics.accuracy_score(y_ts, prediction_test)), 
            ("Base Train Accuracy", metrics.accuracy_score(y_tr, prediction_train)))
    return prediction_test, y_ts

  
#Trains the model on all the data found within the GoodData on dsmlp, and then predicts 
#whether streaming or not for the input data chunk entered
def ml_model_train(feature_csv, filename):
    feature_df = pd.read_csv(feature_csv)
    model = RandomForestClassifier(criterion = 'entropy', max_depth= None, min_samples_split= 3, n_estimators= 20, random_state=42)
    model = model.fit(feature_df.drop(columns = ["input_file_name", "labels"]), feature_df['labels'])
    # save the model to temp/model folder
    joblib.dump(model, filename)
    return

def final_classifier(input_df, filename, output_file_path):
    loaded_model = joblib.load(filename)
    prediction = loaded_model.predict(input_df.drop(columns = ["input_file_name", "labels"]))
    file_name = []
    pred_val = []
    true_val = []
    correct = []
    for i in range(0, len(prediction)):
        file_name.append(input_df['input_file_name'][i])
        pred_val.append(prediction[i])
        true_val.append(input_df['labels'][i])
        if bool(prediction[i]) == bool(input_df['labels'][i]):
            val = "Yes"
            correct.append(val)
        else:
            val = "No"
            correct.append(val)
        print("Input File Name: " + str(input_df['input_file_name'][i]), 
              "is_streaming? Prediction Value: " + str(bool(prediction[i])), 
              "is_streaming? True Value: " + str(bool(input_df['labels'][i])), 
              "classified correctly? : " + val)
    classifier_tbl = pd.DataFrame({"Input File Name" : file_name, "Prediction Value" : pred_val, "True Value" : true_val, "classified correctly?" : correct})
    classifier_tbl.to_csv(output_file_path)
    return
