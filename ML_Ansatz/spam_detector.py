import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
import csv

spam = pd.read_csv('Datasets/spam.csv')
for i in range(len(spam)):
    if len(spam["Label"][i]) > 4:
        full = spam["Label"][i]
        if "ham" in full: 
            label = "ham"
            spam["Label"][i] = label
            test = full.replace("ham,", "")
            buff = test.replace('"', "")
            spam["EmailText"][i] = buff
        elif "spam" in full:
            label = "spam"
            spam["Label"][i] = label
            test = full.replace("spam,", "")
            buff = test.replace('"', "")
            spam["EmailText"][i] = buff

# spam = pd.read_csv('Datasets/spam_ham_dataset.csv', sep=',',
# header=None, names=['Label', 'EmailText', "num"])
# del spam[spam.columns[2]]

z = spam['EmailText']
y = spam["Label"]

z_train, z_test,y_train, y_test = train_test_split(z,y,test_size = 0.2)

# print(y_test)

cv = CountVectorizer()
features = cv.fit_transform(z_train)

model = svm.SVC()
model.fit(features,y_train)

f = open("testMail.txt", "r")

features_test = cv.transform(f)
# print(model.score(features_test,y_test))
print(model.predict(features_test))