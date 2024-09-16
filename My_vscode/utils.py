import pickle

import os
import config
model_folder_path = config.MODEL_FOLDER_PATH

def get_addition(a,b):
    addition = a + b
    print(f"Addition is {addition}")
    return addition

def predict_class(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm):
    
    clf_model = pickle.load(open(f'{model_folder_path}/model.pkl','rb'))
    print("clf_model",clf_model)

    prediction = clf_model.predict([[SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]])
    collection_analysis.insert_one()
    print("Predicted class is :",prediction[0])
    pred = prediction[0]
    # pred = 1
    return pred

predict_class(2,3,4,5)
