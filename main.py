import pandas
import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_columns', None)

data=pd.read_csv("https://video.ittensive.com/python-advanced/data-9722-2019-10-14.utf.csv", delimiter=";")
data=data.dropna(axis=1)
data["AdmArea"]=data["AdmArea"].apply(lambda x: x.split(" ")[0]).astype("category")
data["District"]=data["District"].str.replace("район", "").astype("category")
data=data.set_index("YEAR").loc["2018-2019"].reset_index()
print(data)
