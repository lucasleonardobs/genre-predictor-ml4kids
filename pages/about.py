import streamlit as st
import pandas as pd

def write():
    st.title('Sobre:')
    st.write('Olá, eu sou uma IA que, infelizmente, não foi criada para dominar o mundo. Assim, minha única e solitária função é advinhar se uma música é um RAP, um FUNK ou um SERTANEJO.')
    st.markdown(
        """
        Antes de começar os trabalhos, acho legal falar um pouco mais sobre mim: 
        > Meus criadores são o [Wesley Alves](https://cin.ufpe.br/~was4/) e o [Lucas Leonardo](https://cin.ufpe.br/~llbs/), fui criada para ser submetida como Projeto de IA da disciplina de [Introdução a Computação no CIn/UFPE](https://www.cin.ufpe.br/~if668/), que é onde os meus dois criadores estudam. 

        > Os dados usados durante o meu treinamento e teste foram coletados de maneira automatizada a partir da criação de um script em Python para raspagem de dados. Esse script foi feito com auxílio da biblioteca [Scrapy](https://scrapy.org/) e aplicado ao site [Letras.mus.br](https://www.letras.mus.br).  

        > Minha implementação foi realizada utilizando a plataforma [Machine Learning For Kids](https://machinelearningforkids.co.uk/), que por sua vez possui integração com a rede pré-treinada IBM Watson Assistant. 

        > Essa minha interface bonita e formosa foi feita utilizando Python com a biblioteca [Streamlit](https://docs.streamlit.io/en/stable/api.html)!

        > Tenho algumas limitações no que tange a minha capacidade preditiva devido a quantidade maxima de amostras para treinamento que a plataforma Machine Learning For Kids impõe. Em um cenário ideal, eu teria acesso a mais letras de mais gêneros diferentes e, com isso, conseguiria atuar bem de uma maneira mais geral, sem ficar restrita a esses três gêneros definidos.
        
        > A fim de contornar esse último ponto, quando tenho menos de 65% de confiança em uma predição prefiro não informá-la ao usuário e solicitar que ele tente com outra letra.
        """
    )

    st.title('Resultados da avaliação')
    st.write('Para esse problema de classificação multi-class, uma forma simples e eficiente de observar os resultados obtidos é através da matriz de confusão. Abaixo podemos visualizar a matriz gerada com os testes realizados aqui:')
    st.image('assets/confusion_matrix.png', use_column_width=True)
    st.write('Ademais, também é importante que olhemos para as métricas de precisão, acurácia e recall.')
    st.markdown(r"""
    > A precisão nos dá a razão $$\frac{\text{verdadeiros positivos(TP)}}{\text{verdadeiros positivos(TP)}+\text{falsos positivos(FP)}}$$ ou, em uma definição intuitiva, a capacidade do classificador de não rotular como positiva uma amostra negativa.

    >O recall nos dóa a razão $$\frac{\text{verdadeiros positivos(TP)}}{\text{verdadeiros positivos(TP)}+\text{falsos negativos(FN)}}$$ ou, de forma intuitiva, a capacidade do classificador de encontrar todas as amostras positivas.

    > O F1 score, definido por $$\frac{\text{2*precisião*recall}}{\text{precisão+recall}}$$ pode ser interpretado como uma média harmônica entre o recall e a precisão, de forma a representar essas informações combinadas apenas um único valor. 
    """)
    df = pd.read_csv('assets/metrics.csv', index_col=0).drop(['accuracy', 'macro avg'])
    st.table(df)

    st.write('Dado o exposto, podemos afirmar que o modelo possui um ótimo desempenho dada a quantidade restrita de dados utilizada durante o treinamento, visto que conseguimos de maneira global bons resultados tanto de precisão quanto de recall.')