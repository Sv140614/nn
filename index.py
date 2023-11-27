import pandas as pd
data=pd.read_csv("https://video.ittensive.com/python-advanced/data-5283-2019-10-04.utf.csv", delimiter=";")
data=data.set_index(["Year", "Month"])
data2=pd.read_csv("https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv", delimiter=";")
data2=data2.set_index(["Year", "Period"])
data.index.names=["Year", "Period"]
data3=pd.merge(data, data2, left_index=True, right_index=True)
area_indexes=data3[data3["AdmArea"].str.contains("Центральный административный округ")]
area_indexes=area_indexes[area_indexes["Calls"] == area_indexes["Calls"].min()]
area_indexes=area_indexes['UnemployedMen']
print(area_indexes)
