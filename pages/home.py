import streamlit as st

from model.mltext import classifyText, storeText
from model.mlmodel import trainModel, checkModel
from decouple import config

API_KEY = config('SECRET_KEY')

def write():
    """Used to write the page in the app.py file"""
    st.title('Preditor de generos musicais')

    if checkModel(API_KEY):
        st.success('O modelo está pronto para gerar as prediçoes! Vamos lá.')
    else:
        st.error('Vixxxxx. Algo deu errado, tente novamente mais tarde :(')

    st.header('Cole a letra aqui:')
    test_text = st.text_area('',  height=300)

    if st.button('Gerar predição!'):
        demo = classifyText(API_KEY, test_text)

        label = demo["class_name"]
        confidence = demo["confidence"]

        if confidence < 65:
            st.header(f'Hmmmmmmmmmmmmmmmmm acho que não sei o que é essa letra aí não, hein? Que tal tentar com outra?')
            st.image('assets/wtf.gif', use_column_width=True)
        elif label == 'funk':
            st.header(f'Isso ai é um FUNKZÃO dos brabos, meu patrão! Confia no pai que to com {confidence}% de confiança!')
            st.image('assets/funk.gif', use_column_width=True)
        elif label == 'hip_hop':
            st.header(f'Sabota ta orgulhoso com esse RAP aí! Digo isso com {confidence}% de confiança.')
            st.image('assets/rap.gif', use_column_width=True)
        elif label == 'sertanejo':
            st.header(f'EEEEEE MODÃO BÃO HEIN! Esse é um ótimo SERTANEJO! Tenho {confidence}% de confiança.')
            st.image('assets/sertanejo.gif', use_column_width=True)