import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv('C:\\Users\\Pc\\Desktop\\01.Data Cleaning and Preprocessing.csv')
#bar chart by reading from csv file
plt.bar(df1['Y-Kappa'], df1['BlowFlow'],color='blue', edgecolor='black' ) 
plt.xlabel('Y-Kappa')
plt.ylabel('BlowFlow')
plt.title('Y-Kappa vs BlowFlow')
plt.show()

#line chart by reading from csv file
x,y=df1['Y-Kappa'],df1['BlowFlow']
plt.plot(x,y ,color='cyan' ,linewidth=4)
plt.title('Line Chart')
plt.xlabel('Y-Kappa')
plt.ylabel('BlowFlow')
plt.grid()
plt.show()

#bar chart by creating pandas dataframe
df2 = pd.DataFrame({'Product': ['A', 'B', 'C'], 'Sales': [100, 200, 300]})
plt.bar(df2['Product'], df2['Sales'], color=['red', 'green', 'blue'])
plt.xlabel('Product')
plt.ylabel('Sales')
plt.title('Sales by Product')
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.35)
plt.show()

#line chart by creating pandas dataframe
x,y=df2['Product'],df2['Sales']
plt.plot(x,y ,color='k' ,linewidth=4)
plt.title('Line Chart')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.grid()
plt.show()
