import pandas as pd
import numpy as np
lulus = pd.read_csv("student-mat-pass-or-fail.csv")
lulus.head()
#%%
# Variabel independen
x = lulus.drop(["pass"], axis = 1)
x.head()
#%%
# Variabel dependen
y = lulus["pass"]
y.head()
#%%
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 123)
#%%
from sklearn.naive_bayes import GaussianNB
# Mengaktifkan/memanggil/membuat fungsi klasifikasi Naive Bayes
modelnb = GaussianNB()
# Memasukkan data training pada fungsi klasifikasi Naive Bayes
nbtrain = modelnb.fit(x_train, y_train)
#%%
# Menentukan hasil prediksi dari x_test
y_pred = nbtrain.predict(x_test)
y_pred
#%%
np.array(y_test)
#%%
# Menentukan probabilitas hasil prediksi
nbtrain.predict_proba(x_test)
#%%
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred)

#%%
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))