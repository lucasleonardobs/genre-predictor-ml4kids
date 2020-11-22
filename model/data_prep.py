import pandas as pd 
from sklearn.model_selection import train_test_split


def prepare_data():
    raw_data = pd.read_csv('data/raw_data.csv')

    raw_data['lyric'] = raw_data['lyric'].str.slice(stop=999)
    
    df_funk = raw_data.query("genre == 'Funk'")
    df_hip_hop = raw_data.query("genre == 'Hip Hop/Rap'")
    df_sertanejo = raw_data.query("genre == 'Sertanejo'")

    full_df = pd.concat([df_funk.sample(n=206, random_state=777), 
                         df_sertanejo.sample(n=206, random_state=777), 
                         df_hip_hop.sample(n=206, random_state=777)])

    full_df.genre.replace(['Funk', 'Hip Hop/Rap', 'Sertanejo'], ['funk', 'hip_hop', 'sertanejo'], inplace=True)

    df_train, df_test = train_test_split(full_df, test_size=0.2, random_state=777, stratify=full_df.genre)

    return df_train, df_test