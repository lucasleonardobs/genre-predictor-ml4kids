from model.mltext import classifyText, storeText
from model.mlmodel import trainModel, checkModel
from sklearn.metrics import confusion_matrix, classification_report
from mlxtend.plotting import plot_confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score
import logging
import pandas as pd
import matplotlib.pyplot as plt
mpl_logger = logging.getLogger('matplotlib')
mpl_logger.setLevel(logging.WARNING)


def test_model(API_KEY, df_test):
    y_true = df_test.genre
    y_pred = []
    
    for i, row in df_test.reset_index().iterrows():
        demo = classifyText(API_KEY, row['lyric'])
        y_pred.append(demo["class_name"])

    cm = confusion_matrix(y_true, y_pred, labels=["hip_hop", "funk", "sertanejo"])
    plot_confusion_matrix(conf_mat=cm, 
                          show_normed=True, 
                          figsize=(5, 5), 
                          class_names=["hip_hop", "funk", "sertanejo"])
    plt.tight_layout()
    plt.savefig('assets/confusion_matrix.png')
    
    report = classification_report(y_true, y_pred, target_names=["hip_hop", "funk", "sertanejo"], output_dict=True)
    metrics = pd.DataFrame(report).transpose()
    metrics.to_csv('assets/metrics.csv')