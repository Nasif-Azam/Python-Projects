import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# music_data = pd.read_csv(
#     'D:\\Collection\\Programming Languages\\Phython\\Mechine_Learning2\\music.csv')
# print(music_data)
# # print(music_data.describe())
# X = music_data.drop(columns=["genre"])
# Y = music_data["genre"]
# # print(X)
# # print(Y)

# model = DecisionTreeClassifier()
# model.fit(X, Y)
# predictions = model.predict([[21, 1], [22, 0]])
# print(predictions)

# Calculate The Accuracy
music_data = pd.read_csv(
    'D:\\Collection\\Programming Languages\\Phython\\Mechine_Learning2\\music.csv')
# print(music_data)
# print(music_data.describe())
X = music_data.drop(columns=["genre"])
Y = music_data["genre"]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, Y_train)
predictions = model.predict(X_test)
# print(predictions)

score = accuracy_score(Y_test, predictions)
print(score)
