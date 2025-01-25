import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    'Temperature': [25, 20, 32, 35, 38, 42, 45, 30, 33, 36, 37],
    'Ice_Cream_Sales': [200, 250, 300, 350, 400, 420, 430, 450, 280, 310, 360],
    'Advertising_Budget': [50, 55, 60, 70, 80, 85, 90, 60, 65, 70, 75],
'Customer_Count': [80, 100, 120, 140, 150, 160, 170, 180, 110, 130, 140],
}
df = pd.DataFrame(data)
sns.pairplot(df, diag_kind='kde' , markers="o", plot_kws={'alpha':0.7})
plt.suptitle("Pair Plot Of Ice Cream sales Data", y=1.02, fontsize=16)
plt.show()

