import pandas as pd
from scipy.stats import pearsonr
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

xls = pd.ExcelFile("DMZ.xlsx")

'''
Relation between sicyos angulatus percentage and shanon diversity index 
'''
graph_df = pd.read_excel(xls, sheet_name='그래프')

correlation_coefficient, p_value = pearsonr(graph_df['가시박%'], graph_df["H'"])
# print(correlation_coefficient, p_value)

plt.figure(figsize=(10, 6))
sns.regplot(x='가시박%', y="H'", data=graph_df, scatter_kws={"color": "blue"}, line_kws={"color": "red"}, ci=None)
plt.xlabel('Sicyos Angulatus Percentage (%)')
plt.ylabel("Shannon Diversity Index (H')")
plt.title('Regression Between Burcucumber Percentage and Shannon Diversity Index')
plt.grid(True)
# plt.show()


'''
Relation between location and shanon diversity index
'''

plt.figure(figsize=(10, 6))
sns.boxplot(x='장소', y="H'", data=graph_df)
plt.xlabel('Location')
plt.ylabel("Shannon Diversity Index (H')")
plt.title('Comparison of Shannon Diversity Index Across Locations')
plt.grid(True)
#plt.show()

temlist = graph_df['가시박%'].tolist()
forestlist = temlist[:3]
riverlist = temlist[3:6]
plainlist = temlist[6:]


# forest_shapiro_test = stats.shapiro(forestlist)


