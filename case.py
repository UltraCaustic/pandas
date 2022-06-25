import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('StudentsPerformance .csv')
print(df.info())

df['Summa'] = df['math score'] + df['reading score']+df['writing score']

temp = df.pivot_table(index = 'parental level of education', columns = 'test preparation course', values = 'Summa', aggfunc ='mean')
print(temp)

temp.plot(kind ='barh', grid = True)
plt.show()