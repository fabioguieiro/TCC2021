from file_reader import  all_data
from movement_plotter import movement_plotter
from scipy.fftpack import fft
from transform_functions import get_fft, get_features
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.metrics import pairwise_distances, davies_bouldin_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix



f = open("extracted_info1002_3picos.txt", "w")
f.write("*Arquivo de dados resumido* \n")
cont_file = 0
cont_var = 0
for file in all_data:
    cont_file += 1
    cont_var = 0
    f.write("\nARQUIVO " + str(cont_file))
    for var in file:
        cont_var += 1
        f.write("\nVARIAVEL " + str(cont_var) + " ")
        for value in var:
            f.write(str(value) + " ")
aux = -1
aux2 =0
vet_aux = []
DATA = []
for file in all_data:
    aux += 1
    for articulacao in file:
        if (aux2 < 96):
            for value in articulacao:
                if value != 0:
                    vet_aux.append(value.astype('float64'))
                else:
                    vet_aux.append(value)
            aux2 += 1
        if aux2 == 96:
            DATA.append(vet_aux)
            aux2 = 0
            vet_aux = []
print(aux)
kmeans = KMeans(n_clusters=3, init='random')
kmeans.fit(DATA)
aux=0




for line in DATA:
    line.append(kmeans.labels_[aux])
    aux = aux + 1
f = open("kmeans_7peaks.txt", "w")
for line in DATA:
    for var in line:
        f.write(str(var)+ " ")
    f.write('\n')


labels = kmeans.labels_

#2.3.10.5. Silhouette Coefficient (quanto maior, melhor)
silhouette = metrics.silhouette_score(DATA, labels, metric='euclidean')
print('Silhouette: ', silhouette)

#k2 - 0.20923849513290843
#k3 - 0.21810293608390202
#k4 - 0.2053636854008845
#k5 - 0.15850376485424572
#k6 - 0.17429917724664926
#k7 - 0.17654586860223653

#2.3.10.6. Calinski-Harabasz Index (quanto maior, melhor)
calinsk = metrics.calinski_harabasz_score(DATA, labels)
print('Calinski-Harabasz: ', calinsk)

#k2 - 23.46235923561628
#k3 - 23.50563589476704
#k4 - 20.159824803054615
#k5 - 17.85519539435309
#k6 - 16.223840807738892
#k7 - 15.49249175527682

#2.3.10.7. Davies-Bouldin Index (quanto menor, melhor)
davies = davies_bouldin_score(DATA, labels)
print('Davies-Bouldin: ', davies)

#k2 - 1.723454097121178
#k3 - 1.5379173554615946
#k4 - 1.6666260527483752
#k5 - 1.7412963920036066
#k6 - 1.6350515518592654
#k7 - 1.5693262561723509

# legal que eu tenha informação de tempo de execução, o quanto a adição de todos marcadores impactou no desempenho 

# interessante gerar grafico com os resultados dessas metricas (enriquecer a apresentação da informação)

X = DATA
print("tamanho de X: ", len(X))
y = [1,
1,
1,
1,
1,
1,
1,
1,
1,
0,
0,
0,
1,
1,
1,
0,
0,
0,
1,
1,
1,
0,
0,
0,
1,
1,
1,
0,
0,
0,
1,
1,
1,
0,
0,
0,
0,
0,
0,
0,
0,
0,
1,
1,
1,
0,
0,
0,
0,
0,
0,
1,
1,
1,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=50)

neigh = KNeighborsClassifier(n_neighbors=11)
neigh.fit(X_train, y_train)
y_pred = neigh.predict(X_test)
print("KNN K = 11")
print(neigh.predict(X_test))
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
# print ("confusion:", confusion_matrix(, ))
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
print (tn, fp, fn, tp)
# print(neigh.predict_proba([[0.9]]))


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=50)

neigh = KNeighborsClassifier(n_neighbors=1)
neigh.fit(X_train, y_train)
y_pred = neigh.predict(X_test)
print("KNN K = 1")
print(neigh.predict(X_test))
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
# print ("confusion:", confusion_matrix(, ))
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
print (tn, fp, fn, tp)
# print(neigh.predict_proba([[0.9]]))


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=50)

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_train, y_train)
y_pred = neigh.predict(X_test)
print("KNN K = 3")
print(neigh.predict(X_test))
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
# print ("confusion:", confusion_matrix(, ))
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
print (tn, fp, fn, tp)
# print(neigh.predict_proba([[0.9]]))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=50)

neigh = KNeighborsClassifier(n_neighbors=5)
neigh.fit(X_train, y_train)
print("KNN K = 5")
y_pred = neigh.predict(X_test)
print(neigh.predict(X_test))
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
# print ("confusion:", confusion_matrix(, ))
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
print (tn, fp, fn, tp)
# print(neigh.predict_proba([[0.9]]))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=50)

neigh = KNeighborsClassifier(n_neighbors=7)
neigh.fit(X_train, y_train)
y_pred = neigh.predict(X_test)
print("KNN K = 7")
print(neigh.predict(X_test))
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
# print ("confusion:", confusion_matrix(, ))
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
print (tn, fp, fn, tp)
# print(neigh.predict_proba([[0.9]]))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=50)

neigh = KNeighborsClassifier(n_neighbors=9)
neigh.fit(X_train, y_train)
y_pred = neigh.predict(X_test)
print("KNN K = 9")
print(neigh.predict(X_test))
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
# print ("confusion:", confusion_matrix(, ))
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
print (tn, fp, fn, tp)
# print(neigh.predict_proba([[0.9]]))