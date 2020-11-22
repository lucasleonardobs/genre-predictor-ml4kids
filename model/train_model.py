from model.mltext import classifyText, storeText
from model.mlmodel import trainModel, checkModel
import pandas as pd
import time

def train_model(API_KEY, train_df):
    for _, row in train_df.iterrows():
        try:
            training_text = row['lyric']
            training_label = row['genre']
            storeText(API_KEY, training_text, training_label)
        except:
            pass
        
    trainModel(API_KEY)

    status = None
    while status != 'ready to use':
        status = checkModel(API_KEY)['status']
        time.sleep(10)