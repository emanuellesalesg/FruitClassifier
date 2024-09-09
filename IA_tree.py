from sklearn import tree

liso = 1
irregular = 0
maca = 5
laranja = 10

X = [[140, liso], [130, liso], [150, irregular], [170, irregular]]
Y = [maca, maca, laranja, laranja]

#Instanciando uma arvore para classificação
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y) #Treinando o computador

#Perguntando ao computador qual é a fruta
print("maca" if clf.predict([[100,1]]) == maca else "laranja")





