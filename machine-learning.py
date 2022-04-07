#Bibiotecas necessárias
from sklearn import svm
import pandas as pd

#Criação de arrays
cachorro = [1, 0, 0] #late? Tem 7 vidas? Mia?
gato = [0, 1, 1]
i = [1, 0, 0]

#Criando as features e classificações
animal = [cachorro, gato]
classif = [0, 1]

#Criando o modelo
model = svm.SVC()
model.fit(animal, classif)
model.predict([i])
