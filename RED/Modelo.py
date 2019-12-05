import numpy as np
import pandas as pd

datos = pd.read_csv('./DATASET.csv')

from sklearn.externals import joblib

def Resultado(Caracteristicas):
    detalles =[]
    detalles.append(Caracteristicas)
    clf_from_joblib = joblib.load('./RED_N.pkl')
    pred = clf_from_joblib.predict(detalles)
    # print("Desde la red neuronal: ", pred[0])
    return pred[0]

# print ("DESDE LA FUNCION: ", Resultado([0., 1., 0., 1., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.]))