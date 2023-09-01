import pickle
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

# with open('random_forest_model2.pkl', 'rb') as model_file:  # 학습한 모델 불러오기
#     loaded_model = pickle.load(model_file)
#
# df = pd.DataFrame({"taking_index":[], "has_taken":[]})
# random_boolean = np.random.choice([True, False], size=(56, 1))
# for idx, value in enumerate(random_boolean.tolist()):
#     df = df._append({"taking_index": idx, "has_taken": value[0]}, ignore_index=True)
#
# df[df["has_taken"] == "True"] = "1"
# df[df["has_taken"] == "False"] = "0"
#
# X_train, y_train = df.drop(["has_taken"], axis=1), df["has_taken"]
#
# with open(r'C:\project_yolov8\MCL\random_forest_model2.pkl', 'wb') as model_file:  # 값 추가한 모델 저장
#     pickle.dump(loaded_model, model_file)

with open('random_forest_model2.pkl', 'rb') as model_file:  # 학습한 모델 불러오기
    loaded_model = pickle.load(model_file)


x = np.arange(1, 57).reshape((-1, 1))
print(loaded_model.predict(x))
