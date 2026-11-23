import joblib
import pandas as pd
from sklearn.metrics import confusion_matrix

model = joblib.load("model.joblib")
test = pd.read_csv("test.csv")

X_test = test[["ecg_spread", "age"]]
y_test = test["label"]
predictions = model.predict(X_test)

matrix = confusion_matrix(y_test, predictions, labels=[0, 1])
table = pd.DataFrame(matrix,
                     index=["Actual 0", "Actual 1"],
                     columns=["Predicted 0", "Predicted 1"])
print("Confusion matrix (mock test data):")
print(table)
