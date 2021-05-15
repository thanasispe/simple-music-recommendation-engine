age = int(input("Age? "))
gender = str(input("Male or Female? "))


if (gender.lower() == "male"):
    gender = 1

elif (gender.lower() == "female"):
    gender = 0

else:
    quit(1)

import pandas as pd 
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("music.csv")

X = data.drop(columns="genre")
y = data['genre']

model = DecisionTreeClassifier()
model.fit(X,y)

predictions = model.predict([[age, gender]])
print(f"Do you like {predictions[0]}")
