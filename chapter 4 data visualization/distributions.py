import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cancer_b_data = pd.read_csv('./dataset/datasets_116573_334386_cancer_b.csv', index_col="Id")
cancer_m_data = pd.read_csv('./dataset/datasets_116573_334386_cancer_m.csv', index_col="Id")

# 直方图
sns.distplot(a=cancer_b_data['Area (mean)'], label='Benign', kde=True) # Your code here (benign tumors)
sns.distplot(a=cancer_m_data['Area (mean)'], label="Malignant", kde=True) # Your code here (malignant tumors)
plt.show()


# 概率分布图
sns.kdeplot(data=cancer_b_data['Radius (worst)'], shade=True, label='Benign')
sns.kdeplot(data=cancer_m_data['Radius (worst)'], shade=True, label="Malignant")
plt.show()



