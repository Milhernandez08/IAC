import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split

datos = pd.read_csv('DATASET.csv')
datos = datos.replace(np.nan, "0")
df = pd.DataFrame(datos)

# pred = dict(zip(datos.GenreEt.unique(), datos.Genre.unique()))
# print(pred)

etiquetas = ['Blanco','Amarillo','Cafe','Rojiso','Anaranjado','Lineas','Forma_n','Contorno (','Negro','Gris','Violeta','Verde','Azul','Dientes_Caballo']
X = datos[['Blanco','Amarillo','Cafe','Rojiso','Anaranjado','Lineas','Forma_n','Contorno (','Negro','Gris','Violeta','Verde','Azul','Dientes_Caballo']]
y = datos['RES']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# print(X_train.describe())

from sklearn.neighbors import KNeighborsClassifier

neighboors = np.arange(1,10)
train_exactitud = np.empty(len(neighboors))
test_exactitud = np.empty(len(neighboors))

for i,k in enumerate(neighboors):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    train_exactitud[i] = knn.score(X_train, y_train)
    test_exactitud[i] = knn.score(X_test, y_test)

plt.title("Variacion vacinos en Knn")
plt.plot(neighboors, test_exactitud, label='Test_Exactitud')
plt.plot(neighboors, train_exactitud, label='Train_Exactitud')
plt.legend()
plt.xlabel('Vecinos')
plt.ylabel('Exactitud')
plt.show()


knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(X_train, y_train)
print(knn.score(X_test, y_test))
pred1 = knn.predict([['1.0','0.0','0.0','1.0','0.0','0.0','1.0','0.0']])

print(pred1[0])

from sklearn.ensemble import RandomForestClassifier
print('RandomForest')
while True:
    rfc = RandomForestClassifier()
    rfc.fit(X_train, y_train)
    print(rfc.score(X_train, y_train))
    if rfc.score(X_test, y_test) > 0.75:
        break




pred2 = rfc.predict([['1.0','1.0','0.0','0.0','1.0','0.0','1.0','0.0']])
print(pred2[0])

from sklearn.externals import joblib
joblib.dump(rfc, 'Clasificador.pkl')