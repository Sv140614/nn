import pandas as pd
data=pd.read_csv("https://video.ittensive.com/python-advanced/data-5283-2019-10-04.utf.csv", delimiter=";")
pd.set_option('display.max_columns', None)
a=data["Calls"].mean()
a=round(a)
print(a)
