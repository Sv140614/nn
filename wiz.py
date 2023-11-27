import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams
import scipy.stats as stats

def convert_time(a):
    return sum(x*int(t) for x, t in zip([3600, 60, 1], a.split(":"))) #функция для изменения времени 00:00:00 в секунды

data=pd.read_csv("https://video.ittensive.com/python-advanced/marathon-data.csv")
pd.set_option('display.max_columns', None)
data["split"]=data["split"].apply(convert_time)
data["final"]=data["final"].apply(convert_time)
sns.pairplot(data, hue="gender", height=4)
plt.show()
sns.jointplot("split", "final", data, height=12, kind="kde").annotate(stats.pearsonr)
plt.show()
print(round(stats.pearsonr(data["split"], data["final"])[0],2))


