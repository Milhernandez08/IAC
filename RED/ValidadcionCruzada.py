import numpy as np
import random as rd
import pandas as pd

def train_test_split(X, y):

    X = X.values.tolist()

    y = y.values.tolist()

    X_train = []
    X_test  = []
    y_train = []
    y_test  = []

    numero_De_Pruebas    = int( len( X )/4 )
    numero_De_Entrenados = len( X )-numero_De_Pruebas

    index = []
    for x in range( len( X ) ):
        index.append( x )

    rd.shuffle( index )

    # X  y _train
    for x in range( numero_De_Entrenados ):
        X_train.append( X[ index[x] ] )
        y_train.append( y[ index[x] ] )

    # X y _test
    for x in range( numero_De_Pruebas ):
        X_test.append( X[ index[x] ] )
        y_test.append( y[ index[x] ] )

    return X_train, X_test, y_train, y_test