import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data=pd.read_csv("http://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv", delimiter=";")
pd.set_option('display.max_columns', None)
data["sr"]=data["UnemployedDisabled"]/data["UnemployedTotal"]*100
data=data.drop("Period", axis = 1)
data_group=data.groupby("Year").filter(lambda x: x["sr"].count()>5)
data_group=data_group.groupby("Year").mean()
x=np.array(data_group.index).reshape(len(data_group.index), 1)
y=np.array(data_group["sr"]).reshape(len(data_group.index), 1)
model=LinearRegression()
model.fit(x, y)
print(model.predict(np.array(2020).reshape(1, 1)).round(2))
