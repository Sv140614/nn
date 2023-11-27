import pandas as pd
data=pd.read_csv("http://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv", delimiter=";")
pd.set_option('display.max_columns', None)
data["Pros"]=data.apply(lambda x: 100*x[6]/x[7], axis=1) #data["Pros"]=data["UnemployedDisabled"]/data["UnemployedTotal"]*100
data=data[data["Pros"]<2]
data=data.sort_values("Year")
print(data.iloc[0, 2])
