import pickle

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
import pandas as pd
import numpy as np

circle_list = ['K-011845', 'K-012080', 'K-012137', 'K-012192', 'K-012207', 'K-012256', 'K-012266', 'K-012416',
               'K-012420', 'K-012775', 'K-013020', 'K-013135', 'K-013390', 'K-013536', 'K-013829', 'K-013833',
               'K-013905', 'K-014102', 'K-014205', 'K-014224', 'K-014279', 'K-014567', 'K-014733', 'K-015257',
               'K-015499', 'K-015524', 'K-015530', 'K-015759', 'K-015989', 'K-016193', 'K-016222', 'K-016233',
               'K-016251', 'K-016394', 'K-016645', 'K-016722', 'K-016804', 'K-017057', 'K-017220', 'K-017312',
               'K-017479', 'K-017525', 'K-017574', 'K-017714', 'K-018109', 'K-018110', 'K-018114', 'K-018224',
               'K-018641', 'K-018718']
# 타원 시작
ellipse_list = ['K-011982', 'K-012187', 'K-012447', 'K-012501', 'K-012502', 'K-012503', 'K-012914', 'K-013543',
                'K-013828', 'K-013900', 'K-013937', 'K-014280', 'K-015258', 'K-015270', 'K-015279', 'K-016223',
                'K-016224', 'K-016235', 'K-016250', 'K-016551', 'K-016554', 'K-016555', 'K-016736', 'K-017258',
                'K-017506', 'K-017713', 'K-018119', 'K-018203', 'K-018757', 'K-019156', 'K-019299', 'K-019469',
                'K-019699', 'K-019700', 'K-020378', 'K-020379', 'K-020805', 'K-020834', 'K-020877', 'K-021118',
                'K-021426', 'K-022095', 'K-022318', 'K-022319', 'K-022712', 'K-022713', 'K-023092', 'K-023424',
                'K-023425', 'K-023779']
drug_list_all = [circle_list, ellipse_list]

personnel = list()
dl_mapping_code = list()
taking_index = list()
has_taken = list()
p = 0.1
people_index_list = np.arange(1, 10)
taking_index_list = np.arange(1, 57)
for dr_map_list in drug_list_all:
    for dr_map in dr_map_list:
        for people_index in people_index_list:
            random_boolean = np.random.choice(a=[False, True], size=(56, 1), p=[p, 1-p])
            for idx, bool_ in enumerate(random_boolean.tolist()):
                personnel.append(people_index)
                dl_mapping_code.append(dr_map)
                taking_index.append(idx + 1)
                has_taken.append(bool_[0])

data = {"personnel": personnel, "dl_mapping_code": dl_mapping_code, "taking_index": taking_index, "has_taken": has_taken}
df = pd.DataFrame(data)
print(df)
df.to_csv('mcl_data2.csv', index=False)

df = pd.read_csv("mcl_data2.csv")
np.random.seed(0)
# 2) 학습용 데이터와 검증용 데이터, 테스트 데이터를 분리한다.
df = df.drop(["dl_mapping_code", "personnel"], axis=1)

df[df["has_taken"] == "True"] = 1
df[df["has_taken"] == "False"] = 0

data, target = df.drop(["has_taken"], axis=1), df["has_taken"]

ss = StandardScaler()
# scaled_train_white_data = ss.fit_transform(data)

np.random.seed(0)
# kf = StratifiedKFold(n_splits=5, shuffle=True)

model = RandomForestClassifier()
model.fit(data, target)
random_boolean = np.random.choice(a=[False, True], size=(56, 1), p=[p, 1-p])
taking_index_list = np.arange(1, 57).reshape((-1, 1))
probabilities = model.predict_proba(taking_index_list)
with open(r'random_forest_model2.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)
